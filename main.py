import csv
import job_scraper, employer_scraper
from scrape import *

JOB_CSV = "/tmp/job_csv.csv"
EMPLOYER_CSV = "/tmp/employer_csv.csv"
RUN_CSV = "/tmp/run_csv.csv" 

def main():
    """Main entry point for the script."""
    
    start = now()
    run_row = [start]
        
    with open(JOB_CSV, 'w+') as csv_handler:
        num_new_jobs = scrape(job_scraper.SEARCH_URL, job_scraper.CLASS_, csv_handler, job_scraper.HEADERS, job_scraper.SCRAPERS)

    run_row.append(num_new_jobs)
    with open(EMPLOYER_CSV, 'w+') as csv_handler:
        num_new_employers = scrape(employer_scraper.SEARCH_URL, employer_scraper.CLASS_, csv_handler, employer_scraper.HEADERS, employer_scraper.SCRAPERS)
        
    run_row.append(num_new_employers)
    run_row.append(now())
    with open(RUN_CSV, 'w') as run_csv_handler:
        csv_writer = csv.writer(run_csv_handler)
        csv_writer.writerow(run_row)
        
        
if __name__ == "__main__":
    main()
