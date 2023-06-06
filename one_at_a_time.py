# Import scrapy
import csv
import scrapy
import json
import re

# Import the CrawlerProcess (for running the spider)
from scrapy.crawler import CrawlerProcess

# Create dictionaries to store job titles and job pages
job_list = []

# Create the Spider class


class Sourceful(scrapy.Spider):
  name = "sourceful"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.sourceful.com/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div#jobs li > a'):
      # Get the job titles
      a = job.xpath('./span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c1 = job.xpath('./div/span[5]//text()').extract_first()
      if c1 == 'Fully Remote':
        c = 'Fully Remote'
      else:
        c = job.xpath('./div/span[3]/text()').extract_first().strip()
      job_list.append({'Company': 'Sourceful', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Run the Spider
process = CrawlerProcess()
process.crawl(Sourceful)
process.start()

# Create a list for the column headers
field_names = ['Company', 'Job Title', 'Job URL', 'Location']

# Write to csv file
with open('scraped_jobs_one_at_a_time.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(job_list)
