from bs4 import BeautifulSoup
from collections import deque
import csv
import datetime
import logging
import sys
import requests
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from globals import (CSV_FILE_NAME, LOG_FILE_NAME, FOUND_MSG, NOT_FOUND_MSG, FOUND, NOT_FOUND, UNABLE_TO_MAKE_REQ_MSG,
                     IGNORE_MSG, PROCESSING_MSG, INIT_PARAM_ERROR_MSG, REQUEST_FAILURE_MSG,
                     CSV_NOT_ENABLED_MSG, CSV_FILE_NAME_NOT_FOUND, CSV_HEADER_VALUES, FINDER_LOG_FORMAT)


class ElementFinder(object):
    """
    A class to represent element finder execution.

    Attributes
    ----------
    element_id : str
        Id to search for in the url and its sites
    url : str
        URL where to look for the element id

    Methods
    -------
    start():
        Requests and crawls url provided and seaches for the element id
    """

    def __init__(self, element_id=None, custom=None, url=None, csv=False, single_site=False, debug=False):
        """
        Constructs all the necessary attributes for the Element Finder object

        Attributes
        ----------
        element_id : str
            HTML element id
        custom : str
            Type of HTML element to search for. Ex: 'a', 'p', 'something'. Defaults to 'id' when
            set to None
        url : str
            Site URL to search for element_id
        csv: bool
            Create csv output file
        debug: bool
            Log level indicator. Debug outout file
        """
        if not element_id or not url:
            sys.exit(INIT_PARAM_ERROR_MSG)
        self.csv_file_name = None
        self.csv_file_name_not_found = None
        self.log_file_name = None
        self.log = None

        self.custom = custom
        if self.custom is not None:
            self.element = self.custom
        else:
            self.element = 'id'
        self.element_id = element_id
        self.custom = custom
        self.single_site = single_site
        self.url = url
        self.csv = csv
        self.debug = debug

        self.session_name = get_unique_name()

        if self.csv:
            self.csv_file_name = CSV_FILE_NAME.format(self.session_name)
            self.csv_file_name_not_found = CSV_FILE_NAME_NOT_FOUND.format(
                self.session_name)
            self.append_to_csv(self.get_csv_file_name(), row=CSV_HEADER_VALUES)
            self.append_to_csv(
                self.get_csv_file_name_not_found(), row=CSV_HEADER_VALUES)
        if self.debug:
            self.log_file_name = LOG_FILE_NAME.format(self.session_name)

        self.log = self.loggger_setup()

    def get_csv_file_name(self):
        """
        Returns csv file name assigned

        Parameters
        ----------
        None

        Returns
        -------
        csv_file_name : str
            Name of the csv file
        """
        return self.csv_file_name

    def get_csv_file_name_not_found(self):
        """
        Returns csv file name assigned for not found

        Parameters
        ----------
        None

        Returns
        -------
        csv_file_name_not_found : str
            Name of the csv file
        """
        return self.csv_file_name_not_found

    def get_log_file_name(self):
        """
        Returns log file name assigned

        Parameters
        ----------
        None

        Returns
        -------
        log_file_name : str
            Name of the log file
        """
        return self.log_file_name

    def append_to_csv(self, file_name=None, row=[]):
        """
        Append row to csv file

        Parameters
        ----------
        file_name: str
            Specify a different file name. Will default to self.csv_file_name
        row : list
            List of values to append for csv row

        Returns
        -------
        None
        """
        if not self.csv or not self.csv_file_name or not self.csv_file_name_not_found:
            # Do nothing when csv is not enabled
            return
        if not file_name:
            file_name = self.csv_file_name
        with open(file_name, 'a') as file:
            writer = csv.writer(file)
            writer.writerow(row)

    def loggger_setup(self):
        """
        Setup logger

        Parameters
        ----------
        is_debug : bool
            Stdout and log file when set to true

        Returns
        -------
        logger : logging
            Log initializer
        """
        handlers = list()

        log_level = logging.INFO
        log_format = FINDER_LOG_FORMAT

        if self.debug:
            log_level = logging.DEBUG
            handlers = [
                logging.FileHandler(self.get_log_file_name()),
                logging.StreamHandler()
            ]

        logging.basicConfig(
            level=log_level,
            format=log_format,
            handlers=handlers
        )
        return logging

    def start(self):
        """
        start element find

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        if not self.element_id or not self.url:
            sys.exit(INIT_PARAM_ERROR_MSG)
        new_urls = deque([self.url])
        processed_urls = set()
        local_urls = set()
        foreign_urls = set()
        broken_urls = set()
        ignored_repeats = set()

        search_attributes = dict()
        # update the soup search attr when custom is provided or default to 'id
        if self.custom:
            search_attributes[self.custom] = self.element_id
        else:
            search_attributes['id'] = self.element_id

        if self.single_site:
            content = self.find_element_in_site(
                element=self.element, element_id=self.element_id)
            self.update_content_log(content, self.url)
            return

        while len(new_urls):
            url = new_urls.popleft()
            processed_urls.add(url)
            self.log.debug(PROCESSING_MSG.format(url))
            try:
                response = requests.get(url)
            except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema) as error:
                # add broken urls to it's own set, then continue
                broken_urls.add(url)
                self.log.debug(REQUEST_FAILURE_MSG.format(url, error))
                continue

            # extract base url to resolve relative links
            parts = urlsplit(url)
            base = "{0.netloc}".format(parts)
            strip_base = base.replace("www.", "")
            base_url = "{0.scheme}://{0.netloc}".format(parts)
            path = url[:url.rfind('/')+1] if '/' in parts.path else url

            soup = BeautifulSoup(response.text, "html.parser")
            links = soup.find_all('a')
            for link in links:
                # extract link url from the anchor
                anchor = link.attrs["href"] if "href" in link.attrs else ''
                # Ignore repeated urls that start with '#'
                if any(ignored_anchor in anchor for ignored_anchor in ignored_repeats):
                    continue
                if anchor.startswith('#'):
                    ignored_repeats.add(anchor)
                if anchor.startswith('/'):
                    local_link = base_url + anchor
                    local_urls.add(local_link)
                elif strip_base in anchor:
                    local_urls.add(anchor)
                elif not anchor.startswith('http'):
                    local_link = path + anchor
                    local_urls.add(local_link)
                else:
                    foreign_urls.add(anchor)

            for i in local_urls:
                if not i in new_urls and not i in processed_urls:
                    new_urls.append(i)

                if not link in new_urls and not link in processed_urls:
                    new_urls.append(link)

            content = soup.find_all(attrs=search_attributes)
            self.update_content_log(content, url)

    def update_content_log(self, content, url):
        """
        Update logs and csv when enabled. Log level is handled when initializing the Finder obj.
        CSV file is only updated when self.csv is set to True

        Parameters
        ----------
        content : BeatifulSoup content obj
            Content to use to update logs
        url : str
            URL where to update log and csv

        Returns
        -------
        None
        """
        content_len = len(content)
        # Assume it was not found
        found = NOT_FOUND
        file_name = self.get_csv_file_name_not_found()
        if not content:
            self.log.info(NOT_FOUND_MSG.format(url))
        else:
            # Update csv and log vars when content available
            self.log.info(FOUND_MSG.format(content_len, url))
            found = FOUND
            file_name = self.get_csv_file_name()

        # Update csv when enabled
        row = [self.element, self.element_id, url,
               content_len, get_current_time(), found]
        self.append_to_csv(file_name=file_name,
                           row=row)

    def find_element_in_site(self, element='id', element_id=None):
        """
        Find an element using its id for the given url

        Parameters
        ----------
        element_id : str
            Id to search for in the url 

        Returns
        -------
        BeatifulSoup content obj
        """
        if not element_id or not self.url:
            sys.exit(INIT_PARAM_ERROR_MSG)

        search_attributes = {element: element_id}

        url = self.url
        self.log.debug(PROCESSING_MSG.format(url))
        try:
            response = requests.get(url)
        except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError, requests.exceptions.InvalidURL, requests.exceptions.InvalidSchema):
            # add broken urls to it's own set, then continue
            self.log.debug(UNABLE_TO_MAKE_REQ_MSG.format(url))
            raise
        soup = BeautifulSoup(response.text, "html.parser")
        content = soup.find_all(attrs=search_attributes)
        return content if content else None


def get_unique_name():
    """
    Get a unique name

    Parameters
    ----------
    None

    Returns
    -------
    String with current time as unique name
    """
    now = datetime.datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    return "V{}".format(dt_string)


def get_current_time():
    """
    Get current time

    Parameters
    ----------
    None

    Returns
    -------
    String with current time. Formatted for csv output
    """
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string
