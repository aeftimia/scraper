__all__ = ["SCRAPERS", "HEADERS", "SEARCH_URL", "CLASS_"]

SEARCH_URL = "https://gradaustralia.com.au/graduate-employers"
CLASS_ = "dg-default node node-ad-organisation node-teaser view-mode-teaser"

import re

HEADERS = ["name", "about", "industry"]
SCRAPERS = {}

def scrape_name(soup):
    return soup.find("div", class_="field field-name-organisation-title field-type-ds field-label-hidden").h1.text

SCRAPERS["name"] = scrape_name

sub1 = re.compile(r"[^a-zA-Z0-9\.\u2019]+")

def scrape_description(soup):
    description = soup.find("div", class_="views-row views-row-1 views-row-odd views-row-first views-row-last").text
    description = sub1.sub(' ', description)
    return description

SCRAPERS["about"] = scrape_description

def scrape_industry(soup):
    return soup.find("div", class_="field field-name-taxonomy-vocabulary-71 field-type-taxonomy-term-reference field-label-hidden").find("div", class_="field-item").text

SCRAPERS["industry"] = scrape_industry
