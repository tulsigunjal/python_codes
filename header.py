"""
 Challenge: Scrape Wikipedia h2 Headers

Use the `requests` and `BeautifulSoup` libraries to fetch the Wikipedia page on Python (programming language).

Your task is to:
1. Download the HTML of the page.
2. Parse all `<h2>` section headers.
3. Store the clean header titles in a list.
4. Print the total count and display the first 10 section titles.

Bonus:
- Remove any trailing "[edit]" from the headers.
- Handle network errors gracefully.
"""

import requests            #requests → Downloads the webpage.
from bs4 import BeautifulSoup       #BeautifulSoup → Reads the HTML and finds the headings.

URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"

def get_h2_headers(url):
    request_headers = { "User-Agent": "PythonWebScraper/1.0 (educational project)" }
    try:
        response = requests.get(url, headers=request_headers,timeout=10)
        response.raise_for_status()    #line checks whether the HTTP response indicates a failed request.
    except requests.RequestException as e:        #requests.RequestException   (A base exception class for errors raised by Requests)
        print(f"Failed to fetch page: \n {e}")
        return []   #if the webpage not downlaod then it return the empty list
    
    soup = BeautifulSoup(response.text, "html.parser")   #response.text The downloaded HTML content.  "html.parser" Python's built-in HTML parser.
    h2_tags = soup.find_all("h2")
    print(h2_tags)
    headers = []    #create aempty lsit named it header
    for tag in h2_tags:
        header_text = tag.get_text(strip=True)    #it remove the html tags from the extracted text
        if header_text and header_text.lower() != "contents":
            headers.append(header_text)
    print(headers)

get_h2_headers(URL)