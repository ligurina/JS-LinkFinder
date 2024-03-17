#!/usr/bin/python3
try:
    import requests
    from urllib.parse import urlparse, urljoin
    from bs4 import BeautifulSoup
    import colorama
    import sys
    colorama.init()
    GREEN = colorama.Fore.GREEN
    GRAY = colorama.Fore.LIGHTBLACK_EX
    RESET = colorama.Fore.RESET
    YELLOW = colorama.Fore.YELLOW
    internal_urls = set()
    external_urls = set()
    def is_valid(url):
        """
        Checks whether `url` is a valid URL.
        """
        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)
    def get_all_website_links(url):
        """
        Returns all URLs that are found on `url` which belong to the same website
        """
        urls = set()
        domain_name = urlparse(url).netloc
        response = requests.get(url)
        response.encoding = 'utf-8'  # Or whatever encoding is appropriate for the website
        soup = BeautifulSoup(response.text, "html.parser")
        for a_tag in soup.findAll("a"):
            href = a_tag.attrs.get("href")
            if href == "" or href is None:
                continue
            href = urljoin(url, href)
            parsed_href = urlparse(href)
            href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
            if not is_valid(href):
                continue
            if href in internal_urls:
                continue
            if domain_name not in href:
                if href not in external_urls:
                    print(f"{GRAY}[!] External link: {href}{RESET}")
                    external_urls.add(href)
                continue
            print(f"{GREEN}[*] Internal link: {href}{RESET}")
            urls.add(href)
            internal_urls.add(href)
        return urls
    total_urls_visited = 0
    def crawl(url, max_urls=30):
        """
        Crawls a web page and extracts all links.
        You'll find all links in `external_urls` and `internal_urls` global set variables.
        params:
            max_urls (int): number of max urls to crawl, default is 30.
        """
        global total_urls_visited
        total_urls_visited += 1
        print(f"{YELLOW}[*] Crawling: {url}{RESET}")
        links = get_all_website_links(url)
        for link in links:
            if total_urls_visited > max_urls:
                break
            crawl(link, max_urls=max_urls)
    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: python script.py <url>")
            sys.exit(1)
        url = sys.argv[1]
        crawl(url)
        print("[+] Total Internal links:", len(internal_urls))
        print("[+] Total External links:", len(external_urls))
        print("[+] Total URLs:", len(external_urls) + len(internal_urls))
except Exception as e:
    print(e)