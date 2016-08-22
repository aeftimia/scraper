__all__ = ["SCRAPERS", "HEADERS", "SEARCH_URL", "CLASS_"]

SEARCH_URL = "https://gradaustralia.com.au/search-jobs"
CLASS_ = "dg-three-col node node-ad-vacancy view-mode-search_result"

import re

HEADERS = ["name", "description", "open", "close", "start", "min_study", "required", "type", "link", "location"]
SCRAPERS = {}

def scrape_name(soup):
    return soup.find("div", class_="field-item", property="dc:title").h1.text

SCRAPERS["name"] = scrape_name

def scrape_start(soup):
    return soup.find("div", class_="field field-name-taxonomy-vocabulary-49 field-type-taxonomy-term-reference field-label-above").find("div", class_="field-item even").text

SCRAPERS["start"] = scrape_start

def scrape_location(soup):
    return soup.find("div", class_="field field-name-field-ad-vac-locations field-type-text field-label-above").find("div", class_="field-item even").text.split(", ")

SCRAPERS["location"] = scrape_location

def scrape_required(soup):
    return soup.find("div", class_="field field-name-taxonomy-vocabulary-51 field-type-taxonomy-term-reference field-label-above").find("div", class_="field-item").text

SCRAPERS["required"] = scrape_required

def scrape_type(soup):
    return soup.find("div", class_="field field-name-taxonomy-vocabulary-46 field-type-taxonomy-term-reference field-label-above").find("div", class_="field-item").text

SCRAPERS["type"] = scrape_type

def scrape_open(soup):
    return soup.find("div", class_="field field-name-field-field-job-apps-open field-type-date field-label-above").find("div", class_="field-item").text

SCRAPERS["open"] = scrape_open

def scrape_close(soup):
    return soup.find("div", class_="field field-name-field-ad-vac-closing-date field-type-date field-label-above").find("div", class_="field-item").text

SCRAPERS["close"] = scrape_close

def scrape_min_study(soup):
    return soup.find("div", class_="field field-name-field-minimum-level-study field-type-taxonomy-term-reference field-label-above").find("div", class_="field-item").text

SCRAPERS["min_study"] = scrape_min_study

def scrape_link(soup):
    return soup.find("div", class_="field field-name-field-ad-vac-url field-type-link-field field-label-hidden").find("a", href=True)['href']

SCRAPERS["link"] = scrape_link

sub1 = re.compile(r"[^a-zA-Z0-9\.\u2019]+")

def scrape_description(soup):
    description = soup.find("div", class_="field field-name-body field-type-text-with-summary field-label-hidden").find("div", class_="field-item").text
    description = sub1.sub(' ', description)
    return description

SCRAPERS["description"] = scrape_description
