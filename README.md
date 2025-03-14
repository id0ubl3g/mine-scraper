<div align="center">
    <img src=".github/magnifying-glass-logo.png" alt="Magnifying Glass Logo" width="130">
    <h1><b>Mine Scraper</b></h1>
    <p>Web scraping for data extraction and processing.</p>
    <p>
        <img src="https://img.shields.io/github/last-commit/id0ubl3g/mine-scraper?style=flat&logo=git&logoColor=white&color=0080ff" alt="Last Commit">
        <img src="https://img.shields.io/github/languages/top/id0ubl3g/mine-scraper?style=flat&color=0080ff" alt="Top Language">
        <img src="https://img.shields.io/github/languages/count/id0ubl3g/mine-scraper?style=flat&color=0080ff" alt="Languages Count">
    </p>
</div>

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)  
    - [Setting Up `venv`](#setting-up-venv)  
    - [Dorks Configuration](#dorks-configuration)  
    - [Proxies Configuration](#proxies-configuration)  
- [Getting Started](#getting-started)
- [Get Ready, Install, Scraping!](#get-ready-install-scraping)
- [License](#license)

## Overview

Mine Scraper is a web scraping tool designed for efficient data extraction and processing. It supports scraping dynamic content with Selenium, uses proxies to avoid blocks, and exports data in CSV format. Its modular structure allows for easy customization and scalability.

## Project Structure

```plaintext
└── mine-scraper/
    ├── .github/
    │   ├── magnifying-glass-logo.png
    ├── src/
    │   ├── modules/
    │   │   ├── export_data.py
    │   │   ├── get_info.py
    │   │   ├── mine_scraper.py
    │   │   └── proxy_manager.py
    │   ├── utils/
    │   │   ├── shared/
    │   │   │   └── shared.py
    │   │   ├── style_outputs.py
    │   │   └── system_utils.py
    ├── config/
    │   ├── colors_config.py
    │   ├── dorks_config.py
    │   ├── path_config.py
    │   └── proxies_config.py
    ├── docs/
    │   └── usage_mine_scraper.py
    ├── .gitignore
    ├── LICENSE
    ├── README.md
    ├── requirements.txt
    └── run.py
```

## Prerequisites

Before using Mine Scraper, ensure that Python's virtual environment (venv) is set up on your system.

### Setting Up `venv`
To install the `python3-venv` package, run the following command:

```sh
sudo apt install python3-venv
```

Ensure Python 3 is installed. You can verify by running:
```sh
python3 --version
```

If Python 3 is not installed, you can install it using the following command:

```sh
sudo apt update
sudo apt install python3 python3-venv
```

For additional information, visit the official Python website: [Download Python](https://www.python.org/downloads/)

### Dorks Configuration

The `dorks_config.py` file allows customization of dorks for web scraping. It is located at:

```plaintext
config/dorks_config.py
```

Example of a dork configuration:

```python
dorks = {
    'dork_example': 'site:site.com inurl:"site.com/" intext:"keyword"',
    'dork_example': 'site:site.com inurl:"site.com/" intext:"keyword"'
}
```

Modify this file to adjust the dorks used in the scraping process according to your needs.

### Proxies Configuration

The `proxies_config.py` file contains the proxy settings to help avoid blocks while scraping. It is located at:

```plaintext
config/proxies_config.py
```

Example of a proxy configuration:

```python
proxies_http = {
    'country': 'ip:port',
    'country': 'ip:port'
}
```

Modify this file to include your own proxies for better scraping performance.

## Getting Started 

To run the scraper, use the following command:

```sh
python3 run.py --localhost <True/False>
```

- --**`localhost True`**: When you pass True, the scraper will run on localhost. This means it will make requests directly from your computer.

- --**`localhost False`**: When you pass False, the scraper will use the proxies defined in the config/proxies_config.py file. This helps avoid blocks or limitations when making too many requests from a single origin.

After running the scraper, the extracted data will be automatically saved in the exports/ directory in CSV format.
Example of the expected output:

```plaintext
└── mine-scraper/
    ├── exports/
    │   └── emails_data_socialmedia.csv
```

To display the help message with available options, use:

```sh
python3 run.py --help
```

## Get Ready, Install, Scraping!

- **Virtual Environment**: Use a virtual environment to manage dependencies and avoid conflicts with system-wide packages.

- **Install Dependencies**: After activating the virtual environment, install the necessary dependencies

- **Use Localhost or Proxies**: The `--localhost` flag determines whether the script should use a direct connection or proxies.

    ```sh
    cd mine-scraper
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python3 run.py --localhost True # or: python3 run.py --localhost False
    ```

## License

This project is licensed under the terms of the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0). See the [LICENSE](./LICENSE) file for details.