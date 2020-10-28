#!/usr/bin/env python3

#web scraper for job serach

import requests
from bs4 import BeautifulSoup


def scrape_jobs(job_title=None, location=None):
    """Scrapes Developer job postings from Monster, optionally by location.
    
    :param location: Where the job is located
    
    :type location: str
    
    :return: all job postings from first page that match the search results
    
    :rtype: BeautifulSoup object
    """
    if job_title and location:

        URL = (

            f"https://www.indeed.co.in/jobs?q={job_title}&l={location}"

        )
    elif job_title:

        URL = (

            f"https://www.indeed.co.in/jobs?q={job_title}&l=Mumbai%2C+Maharashtra"

        )
    
    elif location:

        URL = (

        
            f"https://www.indeed.co.in/jobs?q=&l={location}"

        )

    else:

        URL = (

            f"https://www.indeed.co.in/jobs?q=software"


        )


    page = requests.get(URL)


    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="resultsCol")

    return results


def print_all_jobs(results):
    """Print details of all jobs returned by the search.
    The printed details are title, link, company name and location of the job.
    
    :param results: Parsed HTML container with all job listings
    
    :type results: BeautifulSoup object
    
    :return: None - just meant to print results
    
    :rtype: None
    """
    
    job_elems = results.find_all('div', class_="jobsearch-SerpJobCard unifiedRow row result")

    for job_elem in job_elems:
        
        title_elem = job_elem.find("h2", class_="title")
        
        company_elem = job_elem.find("span", class_="company")
        
        location_elem = job_elem.find("span", class_="location")
        
        summary_elem = job_elem.find("div", class_="summary")
        if None in (title_elem, company_elem, location_elem, summary_elem):
            continue
        
        print(title_elem.text.strip())
        print(company_elem.text.strip())
        print(location_elem.text.strip())
        print("Summary :-")
        print(summary_elem.text.strip())
        print("**************************************************")



result = scrape_jobs("python","navi mumbai")

print_all_jobs(result)