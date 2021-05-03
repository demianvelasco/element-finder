CSV_FILE_NAME = "Found-{}.csv"
CSV_FILE_NAME_NOT_FOUND = "NotFound-{}.csv"
LOG_FILE_NAME = "{}.log"
FOUND_MSG = "FOUND {} elements in URL: {}"
NOT_FOUND_MSG = "NOT FOUND in URL: {}"
FOUND = 'Found'
NOT_FOUND = 'Not Found'
IGNORE_MSG = 'IGNORING {}'
PROCESSING_MSG = "Processing {}"
REQUEST_FAILURE_MSG = "Error while making requests to {}. {}"
FINDER_LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
INIT_PARAM_ERROR_MSG = "Error: Element id and site URL are required to initialize the job. See 'script -h' for more information"
CSV_NOT_ENABLED_MSG = "CSV output is not enabled"
UNABLE_TO_MAKE_REQ_MSG = "ERROR: Unable to make http request to {}"

CSV_HEADER_VALUES = ['Element', 'Element ID', 'URL', 'Total Found', 'Time', 'Status']
# row=[self.element_id, element, url, content_len, get_current_time(), FOUND])

PARSER_INPUT = ['element_id', 'url', 'csv', 'debug', 'single_site']

PARSER = {
    'description': "Web scraper to find elements in all pages of a website",
    'arguments': [{
        'names': ['--url', '-url'],
        'required': True,
        'help': 'URL of the site to search for element id'
    },
        {
        'names': ['--element_id', '-id'],
        'required': True,
        'help': 'id of the element to search for'
    },
        {
        'names': ['--custom', '-c'],
        'required': False,
        'help': 'Type of element to search. Defaults to id is not set'
    },
        {
        'names': ['--csv', '-csv'],
        'required': False,
        'help': 'Create a csv file with execution results',
        'action': 'store_true'
    },
        {
        'names': ['--single_site', '-s'],
        'required': False,
        'help': 'Search only in the provided url. Defaults to False',
        'action': 'store_true'
    },
        {
        'names': ['--debug', '-v'],
        'required': False,
        'help': 'Verbose output and log.debug file output',
        'action': 'store_true'
    }
    ]
}
