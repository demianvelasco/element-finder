
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<br />
<p align="center">
  <a href="https://github.com/demianvelasco/element-finder">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">HTML Element Finder</h3>

  <p align="center">
    Command line tool to find HTML elements using element IDs
    <br />
    <a href="https://github.com/demianvelasco/element-finder"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/demianvelasco/element-finder">View Demo</a>
    ·
    <a href="https://github.com/demianvelasco/element-finder/issues">Report Bug</a>
    ·
    <a href="https://github.com/demianvelasco/element-finder/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#test">Test Execution</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Web scraper to find elements in all pages of a website


### Built With

* [Python](https://www.python.org/)
* [Docker](https://www.docker.com/)

* [html5-templates](https://html5-templates.com/preview/sticky-sidebar.html) website used for testing

## Test:
```sh
python3 finder_tests.py
```
#### Results:
```sh
................
----------------------------------------------------------------------
Ran 16 tests in 0.665s

OK
```



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites


* Python - Install Docs: [Mac](https://docs.python-guide.org/starting/install3/osx/) | [Windows](https://www.python.org/downloads/)
  ```sh
  python --version
  ```
* Docker (optional) - [Install Docs](https://docs.docker.com/get-docker/)
  ```sh
  docker --version
  ```

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/demianvelasco/element-finder.git
   ```
2. Change to project directory
   ```sh
   cd element-finder
   ```
#### Docker:
1. Build docker image
   ```sh
   docker build . -t element-finder
   ```
2. Ready to use
   ```sh
   docker run --rm -i -t element-finder -h
   ```
   Output:
   ```sh
    usage: cmd.py [-h] --url URL --element_id ELEMENT_ID [--custom CUSTOM] [--csv] [--single_site] [--debug]

    Web scraper to find elements in all pages of a website

    optional arguments:
      -h, --help            show this help message and exit
      --url URL, -url URL   URL of the site to search for element id
      --element_id ELEMENT_ID, -id ELEMENT_ID
                            id of the element to search for
      --custom CUSTOM, -c CUSTOM
                            Type of element to search. Defaults to id is not set
      --csv, -csv           Create a csv file with execution results
      --single_site, -s     Search only in the provided url. Defaults to False
      --debug, -v           Verbose output and log.debug file output
   ```
3. Add alias to your terminal profile
   ```sh
   echo "alias element_finder='docker run -it --rm element-finder'" >> ~/.bashrc
   ```
4. Source the newly updated terminal profile
   ```sh
   . ~/.bashrc
   ```
5. Use it
   ```sh
   element-finder -h
   ```


#### Python
1. Install Python packages
   ```sh
   pip3 install -U -r requirements.txt
   ```
2. Ready to use
   ```sh
   python3 cmd.py -h
   ```
   Output:
   ```sh
    usage: cmd.py [-h] --url URL --element_id ELEMENT_ID [--custom CUSTOM] [--csv] [--single_site] [--debug]

    Web scraper to find elements in all pages of a website

    optional arguments:
      -h, --help            show this help message and exit
      --url URL, -url URL   URL of the site to search for element id
      --element_id ELEMENT_ID, -id ELEMENT_ID
                            id of the element to search for
      --custom CUSTOM, -c CUSTOM
                            Type of element to search. Defaults to id is not set
      --csv, -csv           Create a csv file with execution results
      --single_site, -s     Search only in the provided url. Defaults to False
      --debug, -v           Verbose output and log.debug file output
    ```




<!-- USAGE EXAMPLES -->
## Usage

#### Docker Build:
```sh
# Build the docker image
docker build . -t element-finder

# Create an alias
 # make it permanent
 # echo "alias element_finder='docker run -it --rm --name element-finder'" >> ~/.bashrc
alias element-finder='docker run -it --rm element-finder'
element-finder -h
# or
docker run -it --rm element-finder -h
```
#### Python
```sh
python3 cmd.py -h
```

#### Find elements with id:
Website element id `header`
```html
<header>
	<div id="header">
		<div class="socialButtons">
```

```sh
python3 cmd.py -url http://localhost:8000 -id header
```
```sh
INFO:root:FOUND 1 elements in URL: http://localhost:8000
INFO:root:FOUND 1 elements in URL: http://localhost:8000#
INFO:root:FOUND 1 elements in URL: http://localhost:8000/
```
#### Single site instead of all web pages found

```sh
python3 cmd.py -url http://localhost:8000 -id header -s
```

```sh
INFO:root:FOUND 1 elements in URL: http://localhost:8000
```

#### Find elements with name and value (`-c` `--custom`):
Website element `title` with name `Menu`
```html
<div id="mobileMenuToggle" title="Menu">M</div>
```

```sh
python3 cmd.py -url http://localhost:8000 -id Menu -c title
```
```sh
INFO:root:FOUND 1 elements in URL: http://localhost:8000
INFO:root:FOUND 1 elements in URL: http://localhost:8000#
INFO:root:FOUND 1 elements in URL: http://localhost:8000/
```
#### Generate a CSV with the findings `--csv` `-csv`:
```sh
python3 cmd.py -url http://localhost:8000 -id header -csv
```
```sh
INFO:root:FOUND 1 elements in URL: http://localhost:8000
INFO:root:FOUND 1 elements in URL: http://localhost:8000/
INFO:root:FOUND 1 elements in URL: http://localhost:8000#
```

Two CSV files are generated:
```sh
ls
# Found**.csv
# NotFound**.csv
NotFound-V03052021140836.csv
Found-V03052021140836.csv
```
#### CSV Output `Found-V03052021140836.csv`

|Element|Element ID|URL                   |Total Found|Time               |Status|
|-------|----------|----------------------|-----------|-------------------|------|
|id     |header    |http://localhost:8000 |1          |03/05/2021 14:08:36|Found |
|id     |header    |http://localhost:8000/|1          |03/05/2021 14:08:36|Found |
|id     |header    |http://localhost:8000#|1          |03/05/2021 14:08:36|Found |


#### Verbose output:
Using `-v` or `--debug` will output information to stdout and will create a log file
```sh
python3 cmd.py -url http://localhost:8000 -id header -v
```
#### Terminal output
```sh
2021-05-03 14:13:15,841 [DEBUG] Processing http://localhost:8000
2021-05-03 14:13:15,844 [DEBUG] Starting new HTTP connection (1): localhost:8000
2021-05-03 14:13:15,847 [DEBUG] http://localhost:8000 "GET / HTTP/1.1" 200 10250
2021-05-03 14:13:15,855 [INFO] FOUND 1 elements in URL: http://localhost:8000
2021-05-03 14:13:15,855 [DEBUG] Processing http://localhost:8000/
2021-05-03 14:13:15,856 [DEBUG] Starting new HTTP connection (1): localhost:8000
2021-05-03 14:13:15,858 [DEBUG] http://localhost:8000 "GET / HTTP/1.1" 200 10250
2021-05-03 14:13:15,865 [INFO] FOUND 1 elements in URL: http://localhost:8000/
2021-05-03 14:13:15,865 [DEBUG] Processing <a href="https://html5-templates.com/" rel="nofollow" target="_blank">HTML5 Templates</a>
2021-05-03 14:13:15,866 [DEBUG] Error while making requests to <a href="https://html5-templates.com/" rel="nofollow" target="_blank">HTML5 Templates</a>. No connection adapters were found for '<a href="https://html5-templates.com/" rel="nofollow" target="_blank">HTML5\xa0Templates</a>'
2021-05-03 14:13:15,866 [DEBUG] Processing http://localhost:8000#
2021-05-03 14:13:15,867 [DEBUG] Starting new HTTP connection (1): localhost:8000
2021-05-03 14:13:15,869 [DEBUG] http://localhost:8000 "GET / HTTP/1.1" 200 10250
2021-05-03 14:13:15,876 [INFO] FOUND 1 elements in URL: http://localhost:8000#
```
#### Log file output

```sh
cat V03052021141315.log
```
```log
2021-05-03 14:13:15,841 [DEBUG] Processing http://localhost:8000
2021-05-03 14:13:15,844 [DEBUG] Starting new HTTP connection (1): localhost:8000
2021-05-03 14:13:15,847 [DEBUG] http://localhost:8000 "GET / HTTP/1.1" 200 10250
2021-05-03 14:13:15,855 [INFO] FOUND 1 elements in URL: http://localhost:8000
2021-05-03 14:13:15,855 [DEBUG] Processing http://localhost:8000/
2021-05-03 14:13:15,856 [DEBUG] Starting new HTTP connection (1): localhost:8000
2021-05-03 14:13:15,858 [DEBUG] http://localhost:8000 "GET / HTTP/1.1" 200 10250
2021-05-03 14:13:15,865 [INFO] FOUND 1 elements in URL: http://localhost:8000/
2021-05-03 14:13:15,865 [DEBUG] Processing <a href="https://html5-templates.com/" rel="nofollow" target="_blank">HTML5 Templates</a>
2021-05-03 14:13:15,866 [DEBUG] Error while making requests to <a href="https://html5-templates.com/" rel="nofollow" target="_blank">HTML5 Templates</a>. No connection adapters were found for '<a href="https://html5-templates.com/" rel="nofollow" target="_blank">HTML5\xa0Templates</a>'
2021-05-03 14:13:15,866 [DEBUG] Processing http://localhost:8000#
2021-05-03 14:13:15,867 [DEBUG] Starting new HTTP connection (1): localhost:8000
2021-05-03 14:13:15,869 [DEBUG] http://localhost:8000 "GET / HTTP/1.1" 200 10250
2021-05-03 14:13:15,876 [INFO] FOUND 1 elements in URL: http://localhost:8000#
```
<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/demianvelasco/element-finder/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Demian Velasco - [ @demianvelasco ](https://twitter.com/@demianvelasco) - demianvelasco@gmail.com

Project Link: [https://github.com/demianvelasco/element-finder](https://github.com/demianvelasco/element-finder)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements


* [html5-templates](https://html5-templates.com/preview/sticky-sidebar.html) website used for testing
* [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) Python Package




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/demianvelasco/element-finder.svg?style=for-the-badge
[contributors-url]: https://github.com/demianvelasco/element-finder/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/demianvelasco/element-finder.svg?style=for-the-badge
[forks-url]: https://github.com/demianvelasco/element-finder/network/members
[stars-shield]: https://img.shields.io/github/stars/demianvelasco/element-finder.svg?style=for-the-badge
[stars-url]: https://github.com/demianvelasco/element-finder/stargazers
[issues-shield]: https://img.shields.io/github/issues/demianvelasco/element-finder.svg?style=for-the-badge
[issues-url]: https://github.com/demianvelasco/element-finder/issues
[license-shield]: https://img.shields.io/github/license/demianvelasco/element-finder.svg?style=for-the-badge
[license-url]: https://github.com/demianvelasco/element-finder/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/demianvelasco