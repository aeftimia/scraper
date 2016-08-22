__all__ = ["scrape", "get_new_urls", "now"]

import csv, urllib
from bs4 import BeautifulSoup
from time import gmtime, strftime
from urllib.request import urlopen

def now():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def scrape(search_url, class_, csv_handler, headers, scrapers):
    
    new_urls = get_new_urls(search_url, class_)
    csv_reader = csv.reader(csv_handler)
    
    # check for duplicate urls
    # should be replaced with an SQL Query
    current_id = 1
    for row in csv_reader:
        current_id += 1
        if row[1] in new_urls:
            new_urls.remove(row[1])
    
    csv_writer = csv.writer(csv_handler)
    for url in new_urls:
        r = urlopen(url)
        soup = BeautifulSoup(r, "lxml")
   
        current_id += 1
    
        data = [current_id, url]
        for header in headers:
            try:
                datum = scrapers[header](soup)
            except AttributeError:
                datum = ""
        
            data.append(datum)
            
        data.append(now())
        csv_writer.writerow(data)
        
    return len(new_urls)
        

def get_new_urls(search_url, class_):
    urls = []
    page = 1
    while True:
        r = urlopen(search_url + "?page=" + str(page))
        soup = BeautifulSoup(r, "lxml")
        
        done = True
        for div in soup.find_all("div",  typeof="sioc:Item foaf:Document", class_=class_):
            urls.append("https://gradaustralia.com.au" + div["about"])
            new_results = False
            
        if done:
            return urls
        page += 1
