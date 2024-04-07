# JS-LinkFinder

JS-LinkFinder is a Python script designed for crawling web pages and extracting internal and external links. It provides a simple and effective way to gather URLs from a given website.

## Features

- **Link Extraction**: Extracts all URLs from a webpage, distinguishing between internal and external links.
- **Crawling**: Crawls a web page recursively, following internal links up to a specified maximum number of URLs.
- **Validity Check**: Checks the validity of URLs to ensure they are well-formed and accessible.
- **Colorized Output**: Uses color-coding to differentiate between internal and external links for easy visualization.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/ligurina/JS-LinkFinder.git
    ```

2. Navigate to the project directory:

    ```bash
    cd JS-LinkFinder
    ```

3. Run the script with a target URL:

    ```bash
    python JS-LinkFinder.py <url>
    ```

   Replace `<url>` with the target website URL.

4. The script will start crawling the target website and display the internal and external links found.

## Requirements

- Python 3.x
- Required Python packages (install using `pip install -r requirements.txt`):
  - `requests`
  - `beautifulsoup4`
  - `colorama`

## Example

Running the script with a target URL:

```bash
python JSLinkFinder.py https://example.com
