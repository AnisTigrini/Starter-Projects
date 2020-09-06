# Import selenium library
from selenium import webdriver
import time

driver = webdriver.Chrome('/home/anis/Documents/Python/chromedriver.exe')

for i in range(0,10):
    driver.get('https://ca.indeed.com/jobs?q=software&start={}0'.format(i))
    
    # code to get the number of jobs in the market for this specific field
    if i <= 0:
        ids = driver.find_element_by_id('searchCountPages')
        number_of_jobs = str(ids.get_attribute('innerHTML')).split('Page 1 of ')[1]
        print(number_of_jobs)

    #code to get the job description
    job_offers = driver.find_elements_by_class_name('jobsearch-SerpJobCard')
    print(len(job_offers))
    for i in range(0, len(job_offers)):
        individual_job = job_offers[i].find_element_by_tag_name('h2').find_element_by_tag_name('a')
        print(individual_job.get_attribute('href'))


driver.close()

