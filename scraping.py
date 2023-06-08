# Import packages
import csv
import scrapy
import json
import re

# Import the CrawlerProcess (for running the spider)
from scrapy.crawler import CrawlerProcess

# Create dictionary to store job titles, job description URLs, and job locations
job_list = []

# Putting all the LinkedIn organisations at the top

# Create the Spider class


class Anibles(scrapy.Spider):
  name = "anibles"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=85080315&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Anibles', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Business_For_Nature(scrapy.Spider):
  name = "businessfornature"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=51709571&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Business for Nature',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Clean_Growth_Fund(scrapy.Spider):
  name = "cleangrowthfund"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=49135135&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Clean Growth Fund',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Climate_Outreach(scrapy.Spider):
  name = "climateoutreach"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=591140&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Climate Outreach',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Daily_Dose_Juice(scrapy.Spider):
  name = "dailydosejuice"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=10353943&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Daily Dose Juice',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Deep_Meta(scrapy.Spider):
  name = "deepmeta"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=71555220&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Deep Meta', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Denton_Park_Estate(scrapy.Spider):
  name = "dentonparkestate"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=91676887&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Denton Park Estate',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Echion_Technologies(scrapy.Spider):
  name = "echiontechnologies"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=11409858&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip().title()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Echion Technologies',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Ewhurst_Park(scrapy.Spider):
  name = "ewhurstpark"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=75060928&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Ewhurst Park',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Giant_Ventures(scrapy.Spider):
  name = "giantventures"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=38124485&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Giant Ventures',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Giki(scrapy.Spider):
  name = "giki"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=49164184&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Giki', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class HCV_Network(scrapy.Spider):
  name = "hcvnetwork"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=10827722&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append(
          {'Company': 'HCV Network', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Initiative_Earth(scrapy.Spider):
  name = "initiativeearth"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=76110920&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip().title()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Initiative Earth',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Just_Stop_Oil(scrapy.Spider):
  name = "juststopoil"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=79450734&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip().title()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Just Stop Oil',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Kita(scrapy.Spider):
  name = "kita"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=77589995&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Kita', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Mana_Biosystems(scrapy.Spider):
  name = "manabiosystems"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=71685967&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Mana Biosystems',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Materiom(scrapy.Spider):
  name = "materiom"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=42893171&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Materiom', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Measurable_Energy(scrapy.Spider):
  name = "measurableenergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=12641566&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'measurable.energy',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Meatless_Farm(scrapy.Spider):
  name = "meatlessfarm"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=12663898&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip().title()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Meatless Farm',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class MyCarbon(scrapy.Spider):
  name = "mycarbon"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=77197247&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'MyCarbon', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Natcap_Research(scrapy.Spider):
  name = "natcapresearch"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=78708204&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Natcap Research',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Newcleo(scrapy.Spider):
  name = "newcleo"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = [
        'https://www.linkedin.com/jobs/search/?f_C=79700134&location=United%20Kingdom']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Newcleo', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Noughts_Ones(scrapy.Spider):
  name = "noughtsones"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=5049447&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Noughts & Ones',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class On_The_Edge(scrapy.Spider):
  name = "ontheedge"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=71793065&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip().title()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append(
          {'Company': 'On The Edge', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Population_Matters(scrapy.Spider):
  name = "populationmatters"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=Population+Matters&location=United+Kingdom&trk=public_jobs_jobs-search-bar_search-submit']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Population Matters',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Safe_Solvents(scrapy.Spider):
  name = "safesolvents"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=10017784&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip().title()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Safe Solvents',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Space_Intelligence(scrapy.Spider):
  name = "spaceintelligence"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=18502992&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Space Intelligence',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Switch_It_Green(scrapy.Spider):
  name = "switchitgreen"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=42399605&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Switch It Green',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Tangle(scrapy.Spider):
  name = "tangle"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=86714818&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Tangle', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Tenzing_Natural_Energy(scrapy.Spider):
  name = "tenzingnaturalenergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=10207506&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'TENZING Natural Energy',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Too_Good_To_Go(scrapy.Spider):
  name = "toogoodtogo"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=10463013&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Too Good To Go',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Treedom(scrapy.Spider):
  name = "treedom"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=934348&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Treedom', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Trust_For_Sustainable_Living(scrapy.Spider):
  name = "trustforsustainableliving"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search/?f_C=33192220&geoId=92000000']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Trust for Sustainable Living',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Wildlife_And_Countryside_Link(scrapy.Spider):
  name = "wildlifecountrysidelink"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=2533532&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Wildlife and Countryside Link',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Wrap(scrapy.Spider):
  name = "wrap"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=215390&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Wrap', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Zevero(scrapy.Spider):
  name = "zevero"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linkedin.com/jobs/search?keywords=&location=United%20Kingdom&locationId=&geoId=101165590&f_TPR=&f_C=79654686&position=1&pageNum=0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.base-card'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first().strip()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b1 = job.xpath('./a/@href').extract_first()
      b2 = b1.split('?')
      b = b2[0]
      # Get the locations
      c = job.xpath('./div[2]/div/span/text()').extract_first().strip()
      job_list.append({'Company': 'Zevero', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Now all the Workable ATS organisations

# Create the Spider class
class Again(scrapy.Spider):
  name = "again"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/again/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/again/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/again/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Again', 'Job Title': a,
                        'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class AimHi_Earth(scrapy.Spider):
  name = "aimhiearth"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/aimhi-earth/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/aimhi-earth/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/aimhi-earth/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append(
            {'Company': 'AimHi Earth', 'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Breathe_Battery_Technologies(scrapy.Spider):
  name = "breathebatterytechnologies"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/breathecareers/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/breathecareers/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/breathecareers/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Breathe Battery Technologies',
                        'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Brilliant_Planet(scrapy.Spider):
  name = "brilliantplanet"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/brilliantplanet/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/again/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/again/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Brilliant Planet',
                        'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Carbon_Re(scrapy.Spider):
  name = "carbonre"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/carbonre/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/carbonre/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/carbonre/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append(
            {'Company': 'Carbon Re', 'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Climate_Arc(scrapy.Spider):
  name = "climatearc"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/climatearc/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/climatearc/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/climatearc/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      job_list.append(
          {'Company': 'Climate Arc', 'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Climate_Bonds_Initiative(scrapy.Spider):
  name = "climatebondsinitiative"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/climate-bonds-initiative/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/climate-bonds-initiative/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/climate-bonds-initiative/j/' + \
          job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Climate Bonds Initiative',
                        'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Dendra(scrapy.Spider):
  name = "dendra"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/dendra-systems/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/dendra-systems/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/dendra-systems/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Dendra', 'Job Title': a,
                        'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class FareShare(scrapy.Spider):
  name = "fareshare"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/fareshare/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/fareshare/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/fareshare/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append(
            {'Company': 'FareShare', 'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Global_OTEC(scrapy.Spider):
  name = "globalotec"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/global-otec/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/global-otec/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/global-otec/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append(
            {'Company': 'Global OTEC', 'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Hived(scrapy.Spider):
  name = "hived"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/hived/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/hived/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/hived/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Hived', 'Job Title': a,
                        'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Lick(scrapy.Spider):
  name = "lick"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/lick-home-ltd/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/lick-home-ltd/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/lick-home-ltd/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Lick', 'Job Title': a,
                        'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Make_My_House_Green(scrapy.Spider):
  name = "makemyhousegreen"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/switchd-ltd/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/switchd-ltd/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/switchd-ltd/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Make My House Green',
                        'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Onto(scrapy.Spider):
  name = "onto"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/onto/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/onto/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/onto/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Onto', 'Job Title': a,
                        'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Oxwash(scrapy.Spider):
  name = "oxwash"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/oxwash/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/oxwash/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/oxwash/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Oxwash', 'Job Title': a,
                        'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Pangaia(scrapy.Spider):
  name = "pangaia"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/pangaia/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/pangaia/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/pangaia/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Pangaia', 'Job Title': a,
                        'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Pawprint(scrapy.Spider):
  name = "pawprint"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/pawprint/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/pawprint/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/pawprint/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Pawprint', 'Job Title': a,
                        'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Recycleye(scrapy.Spider):
  name = "recycleye"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/recycleye/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/recycleye/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/recycleye/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append(
            {'Company': 'Recycleye', 'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class So_Energy(scrapy.Spider):
  name = "soenergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/so-energy/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/so-energy/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/so-energy/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append(
            {'Company': 'So Energy', 'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Tesseract(scrapy.Spider):
  name = "tesseract"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/tesseract/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/tesseract/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/tesseract/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append(
            {'Company': 'Tesseract', 'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class The_Modern_Milkman(scrapy.Spider):
  name = "modernmilkman"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/the-modern-milkman/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/the-modern-milkman/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/the-modern-milkman/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'The Modern Milkman',
                        'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Tokamak_Energy(scrapy.Spider):
  name = "tokamak"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/tokamak-energy/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/oxwash/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/tokamak-energy/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Tokamak Energy',
                        'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Wallbox(scrapy.Spider):
  name = "wallbox"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/wallbox/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/wallbox/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/wallbox/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Wallbox', 'Job Title': a,
                        'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Wildlife_Works(scrapy.Spider):
  name = "wildlifeworks"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/wildlife-works/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/wildlife-works/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/wildlife-works/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Wildlife Works',
                        'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Zoomo(scrapy.Spider):
  name = "zoomo"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/zoomo/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/zoomo/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/zoomo/j/' + job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Zoomo', 'Job Title': a,
                        'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# Create the Spider class
class Zulu_Forest_Sciences(scrapy.Spider):
  name = "zuluforestsciences"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  url = 'https://apply.workable.com/api/v3/accounts/zulu-forest-sciences/jobs'
  headers = {
      "Accept": "application/json, text/plain, */*",
      "Accept-Encoding": "*",
      "Accept-Language": "en",
      "Cache-Control": "no-cache",
      "Connection": "keep-alive",
      "Content-Type": "application/json",
      "DNT": "1",
      "Host": "apply.workable.com",
      "Origin": "https://apply.workable.com",
      "Pragma": "no-cache",
      "Referer": "https://apply.workable.com/zulu-forest-sciences/",
      "Sec-Fetch-Dest": "empty",
      "Sec-Fetch-Mode": "cors",
      "Sec-Fetch-Site": "same-origin",
      "Sec-GPC": "1",
      "TE": "trailers",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
  }
  payload = {
      "query": "",
      "location": [],
      "department": [],
      "worktype": [],
      "remote": []}

  # start_requests method
  def start_requests(self):
    yield scrapy.Request(url=self.url,
                         method='POST',
                         headers=self.headers,
                         body=json.dumps(self.payload),
                         callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['results']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = 'https://apply.workable.com/zulu-forest-sciences/j/' + \
          job['shortcode']
      # Get the locations
      c1 = job['location']['country']
      c2 = job['location']['region']
      c3 = job['location']['city']
      r = job['remote']
      if r == True:
        c = 'Remote'
      else:
        if c3 != "":
          c = c3
        else:
          c = c1
      # Filter out non-UK jobs
      if 'United Kingdom' in c1:
        job_list.append({'Company': 'Zulu Forest Sciences',
                        'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    if 'nextPage' in data:
      self.payload['token'] = data['nextPage']
      yield scrapy.Request(url=self.url, headers=self.headers, body=json.dumps(self.payload), method="POST")


# End of the Workable ATS organisations

# Create the Spider class
class Three_Fifty_Org(scrapy.Spider):
  name = "threefiftyorg"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards.greenhouse.io/350org']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.opening'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://boards.greenhouse.io' + \
          job.xpath('./a/@href').extract_first()
      # Get the locations
      c1 = job.xpath('./span/text()').extract_first()
      if any(x in c1 for x in ['Remote in 1 of 26 countries', 'countries we are currently operating in', 'Europe', 'Remote in the United Kingdom']):
        c = 'Fully Remote'
        job_list.append({'Company': '350.org', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Abel_Cole(scrapy.Spider):
  name = "abelcole"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://abel-cole.breezy.hr/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.position.transition > a'):
      # Get the job titles
      a = job.xpath('./h2/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://abel-cole.breezy.hr' + job.xpath('./@href').extract_first()
      # Get the locations
      c = job.xpath('./ul/li[1]/span/text()').extract_first()
      job_list.append(
          {'Company': 'Abel & Cole', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Agile_Charging(scrapy.Spider):
  name = "agile_charging"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.agilecharging.com/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.sqs-block-content > h2'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs (these appear as truncated pathnames so need to concatenate with the rest of the URL)
      b = 'https://www.agilecharging.com' + \
          job.xpath('./a/@href').extract_first()
      # Get the location
      c = 'Southwark, Central London'
      job_list.append({'Company': 'Agile Charging',
                      'Job Title': a, 'Job URL': b, 'Location': c})


job_desc_urls_airly = []
# Create the Spider class


class Airly(scrapy.Spider):
  name = "airly"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://airly.org/en/career/job-list/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape links to individual job pages
  def parse(self, response):
    for job in response.css('div.career-tile__content'):
      # Get the URLs for each job listed on the page
      url = 'https://airly.org'+job.xpath('./div[1]/a/@href').extract_first()
      # Add those URLs to a (initially empty) list so we can use them in the next for loop
      job_desc_urls_airly.append(url)
    # Tell it to scrape the job description page for each job
    for job in job_desc_urls_airly:
      yield scrapy.Request(url=job, callback=self.parse_job_desc)

  # Second parsing method to scrape job titles and locations
  def parse_job_desc(self, response):
    # Get the job titles
    a = response.css(
        'div.career-single-hero__inner > h2').xpath('./text()').extract_first()
    # Get the locations
    c = response.css(
        'div.career-content-single__info').xpath('./div/div[1]/p[2]/text()').extract_first()
    job_list.append({'Company': 'Airly', 'Job Title': a,
                    'Job URL': response.url, 'Location': c})


# Create the Spider class
class Allplants(scrapy.Spider):
  name = "allplants"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.allplants.com/en/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.block-grid-item > a'):
      # Get the job titles
      a = job.xpath('./div[2]/span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the location (this is an awkward one where it can be in two different places depending what other info is included)
      c1 = job.xpath('./div[2]/div/span[3]/text()').extract_first()
      c2 = job.xpath('./div[2]/div/span[1]/text()').extract_first()
      if any(x in c1 for x in ['Veg Patch', 'Greenhouse']):
        c = 'London'
      elif any(x in c2 for x in ['Veg Patch', 'Greenhouse']):
        c = 'London'
      else:
        c = 'nooo, scraping error'
      job_list.append({'Company': 'Allplants', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Altruistiq(scrapy.Spider):
  name = "altruistiq"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards.greenhouse.io/altruistiq']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.opening'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://boards.greenhouse.io' + \
          job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./span/text()').extract_first()
      job_list.append({'Company': 'Altruistiq', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Amphibian_Reptile_Conservation(scrapy.Spider):
  name = "amphibian_reptile_conservation"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.arc-trust.org/vacancies']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.content.postContent.pageContent > h2'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # All job descriptions are on the same page
      b = 'https://www.arc-trust.org/vacancies'
      # Get the locations
      c = job.xpath('./following-sibling::p[2]').extract_first()
      # Exclude crap
      if not any(x in a for x in ['Listed below', 'Volunteer']):
        job_list.append({'Company': 'Amphibian & Reptile Conservation Trust',
                        'Job Title': a, 'Job URL': b, 'Location': c})

"""
# Create the Spider class
class Arribada(scrapy.Spider):
  name = "arribada"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://arribada.org/working-for-arribada/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.et_pb_column_0 > div:nth-child(3n+5)'):
      # Get the job titles
      a1 = job.xpath('.//text()').extract()
      a = "".join(a1).strip()
      # Get the URLs for those jobs
      b = job.xpath('./following-sibling::div[2]/a/@href').extract_first()
      # Get the locations
      c = 'London'
      # Exclude crap
      if b != None:
        job_list.append({'Company': 'Arribada', 'Job Title': a,
                        'Job URL': b, 'Location': c})
"""

# Create the Spider class
class Arrival(scrapy.Spider):
  name = "arrival"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://talent.arrival.com/api/vacancies']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for i in range(len(data)):
      # Get the job titles
      a = data[i]['title']
      # Get the URLs for those jobs
      b = "https://talent.arrival.com/vacancy/"+data[i]['id']
      # Get locations
      c = data[i]['location']
      # Exclude non-UK locations
      unwanteds = ["Tbilisi", "Berlin", "Charlotte",
                   "Los Angeles", "Rock Hill", "Turkey"]
      if not any(x in c for x in unwanteds):
        job_list.append({'Company': 'Arrival', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Aura_Power(scrapy.Spider):
  name = "aurapower"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.aurapower.com/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.career-wrapper'):
      # Get the job titles
      a = job.xpath('./h3/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./div[1]/p[2]/text()').extract_first()
      if c == "UK, Remote" or c == "UK based":
        c = "Bristol"
      job_list.append({'Company': 'Aura Power', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Avon_Needs_Trees(scrapy.Spider):
  name = "avonneedstrees"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://avonneedstrees.org.uk/about-us/jobs/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.feature--text__container'):
      # Get the job titles
      a = job.xpath('.//h2//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./a/@href').extract_first()
      # Get the locations
      c = "Bristol area"
      job_list.append({'Company': 'Avon Needs Trees',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class B_Lab_UK(scrapy.Spider):
  name = "blabuk"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://bcorporation.uk/about-b-lab-uk/our-team-and-organisation/uk-team/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.relative.grid-container'):
      # Get the job titles
      a = job.xpath('./div[2]/h5/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./a/@href').extract_first()
      # Get the locations
      c = 'London'
      # Exclude crap
      if b != None:
        job_list.append({'Company': 'B Lab UK', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Ballard_Motive_Solutions(scrapy.Spider):
  name = "ballardmotivesolutions"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://recruitingbypaycor.com/career/CareerHome.action?clientId=8a7883d06937f5f7016978fec55861f7&parentUrl=https%3A%2F%2Fwww.ballard.com%2Fcareers%2Fcurrent-opportunities&gns=']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.gnewtonCareerGroupRowClass'):
      # Get the job titles
      a = job.xpath('./div[1]/a/text()').extract_first().strip()
      # Get the URLs for those jobs
      b = job.xpath('./div[1]/a/@href').extract_first()
      # Get the locations
      c = job.xpath('./div[2]/text()').extract_first().strip()
      # Only UK jobs
      unwanteds = ['Vancouver', 'British Columbia', 'Canada', 'America', 'USA', 'United States', 'Bend',
                   'Oregon', 'China', 'Guangzhou', 'Shenzhen', 'Burnaby', 'OR', 'Shanghai', 'Flexible Location']
      if not any(x in c for x in unwanteds):
        job_list.append({'Company': 'Ballard Motive Solutions',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Bat_Conservation_Trust(scrapy.Spider):
  name = "batconservationtrust"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.bats.org.uk/the-trust/jobs-careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.col.a6-12.c12-12 > a'):
      # Get the job titles
      a = job.xpath('./p/span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # No consistent way to get locations. Either needs to be manual or extracted from job title
      c = "unknown"
      job_list.append({'Company': 'Bat Conservation Trust',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Baukjen(scrapy.Spider):
  name = "baukjen"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.baukjen.com/pages/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.cms-content > div > u > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'London'
      job_list.append({'Company': 'Baukjen', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Beaver_Trust(scrapy.Spider):
  name = "beavertrust"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://beavertrust.org/vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.elementor-container.elementor-column-gap-default'):
      # Get the job titles
      a = job.xpath('./div[2]/div/div[1]/div/p/a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://beavertrust.org/vacancies/'
      # Get the locations
      c = 'Fully Remote'
      # Exclude crap
      if a != None:
        job_list.append({'Company': 'Beaver Trust',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class BeZero(scrapy.Spider):
  name = "bezero"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://bezerocarbon.teamtailor.com/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li > a.focus-visible-company'):
      # Get the job titles
      a = job.xpath('./span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c1 = job.xpath('./div/span[3]//text()').extract_first()
      # That works most of the time, but some jobs don't have the department listed, so there's not always another span before the location span
      if 'Remote' not in c1:
        c2 = c1
      else:
        c2 = job.xpath('./div/span[1]/text()').extract_first().strip()
      # Weird indentations and spaces sometimes
      c = c2.strip()
      job_list.append({'Company': 'BeZero', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Bike_Club(scrapy.Spider):
  name = "bikeclub"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://bikeclub.bamboohr.com/jobs/embed2.php?version=1.0.0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.BambooHR-ATS-Jobs-Item'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https:'+job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./span/text()').extract_first().strip()
      if c == 'John Lewis':
        c = 'London'
      job_list.append({'Company': 'Bike Club', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Biophilica(scrapy.Spider):
  name = "biophilica"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.biophilica.co.uk/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h2'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # The URL for every job description is the same
      b = 'https://www.biophilica.co.uk/careers'
      # Get the locations
      c = "London"
      job_list.append({'Company': 'Biophilica', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Biorecro(scrapy.Spider):
  name = "biorecro"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.biorecro.com/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('section.elementor-section > div.elementor-container'):
      # Get the job titles (need to remove white space from beginning and end for this one)
      a = job.xpath('./div[1]/div/div[2]//h2/text()').extract_first()
      # All job descriptions are on the same URL
      b = "https://www.biorecro.com/careers/"
      # Get the locations
      c = job.xpath('./div[1]/div/div[1]/div/p/text()').extract_first()
      # Filter out Swedish jobs and cut out the non-job results
      if a != None:
        if 'Sweden' not in c:
          job_list.append(
              {'Company': 'Biorecro', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Birdlife(scrapy.Spider):
  name = "birdlife"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.birdlife.org/careers-hub/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.c-careers-search-result'):
      # Get the job titles (need to trim whitespace here)
      a = job.xpath('./div[1]/h3/a/text()').extract_first().strip()
      # Get the URLs for those jobs
      b = job.xpath('./div[1]/h3/a/@href').extract_first()
      # Get the location
      c = job.xpath('./div[2]/text()').extract_first().strip()
      if 'UK' in c:
        job_list.append({'Company': 'BirdLife International',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Blue_Marine_Foundation(scrapy.Spider):
  name = "bluemarine"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.bluemarinefoundation.com/contact/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.content-links > p > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      if 'Solent' in a:
        c = 'London, Solent'
      else:
        c = 'London'
      # Exclude the crap that gets scraped
      if 'mailto' not in b:
        job_list.append({'Company': 'Blue Marine Foundation',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Blue_Ventures(scrapy.Spider):
  name = "blueventures"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://api.teamtailor.com/v1/jobs?&api_key=fc17-ZWKzsKAZSJMn_69XbdaqvTSLSMXz2BjhBo3&api_version=20161108&include=department,role,regions,locations&fields[departments]=name&fields[roles]=name&fields[locations]=name,city&fields[regions]=name&page[size]=30&filter[feed]=public&']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['data']:
      # Get the job titles
      a = job['attributes']['title']
      # Get the URLs for those jobs
      b = job['links']['careersite-job-url']
      # Get the location. This one is messy with a self-referencing API with optional fields
      # Check if the city is filled in
      c0 = job['relationships']['locations']['data']
      # If the city is filled in, store it in c. Otherwise, set c to be an empty string
      if c0 != []:
        c1 = job['relationships']['locations']['data'][0]['id']
        c2 = data['included']
        for item in c2:
          if item['id'] == c1:
            c3 = item['attributes']['name']
      else:
        c3 = ""
      # Check if the job is remote (this seems to always be filled in, hopefully it stays that way), then append that status to the location (unless it's not remote)
      remote = job['attributes']['remote-status']
      if remote != "none":
        c = c3 + " - " + remote + " remote"
      else:
        c = c3
      # Filter out non-UK jobs
      if 'American Friends' not in a:
        job_list.append({'Company': 'Blue Ventures',
                        'Job Title': a, 'Job URL': b, 'Location': c})


job_desc_urls_bonsucro = []
# Create the Spider class


class Bonsucro(scrapy.Spider):
  name = "bonsucro"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://bonsucro.com/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape links to individual job pages
  def parse(self, response):
    for job in response.css('div.row > div.column > h4 > a'):
      # Get the URLs for each job listed on the page
      url = job.xpath('./@href').extract_first()
      # Add those URLs to a (initially empty) list so we can use them in the next for loop
      job_desc_urls_bonsucro.append(url)
    # Tell it to scrape the job description page for each job
    for job in job_desc_urls_bonsucro:
      yield scrapy.Request(url=job, callback=self.parse_job_desc)

  # Second parsing method to scrape job titles and locations
  def parse_job_desc(self, response):
    # Get the job titles
    a = response.css('h1').xpath('./text()').extract_first()
    # Get the locations
    c = response.css('tbody').xpath('./tr[2]/td[2]/text()').extract_first()
    if 'Remote. International' in c:
      c = 'Fully Remote'
    if c == "":
      c = 'London'
    job_list.append({'Company': 'Bonsucro', 'Job Title': a,
                    'Job URL': response.url, 'Location': c})


# Create the Spider class
class Born_Free_Foundation(scrapy.Spider):
  name = "bornfreefoundation"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.bornfree.org.uk/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.segment.grey h3'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first().strip().title()
      # Get the URLs for those jobs
      b = 'https://www.bornfree.org.uk/careers'
      # Get the locations
      c = 'West Sussex'
      job_list.append({'Company': 'Born Free Foundation',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class British_Ecological_Society(scrapy.Spider):
  name = "britishecologicalsociety"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.britishecologicalsociety.org/about/vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.bleed-area > p > a'):
      # Get the job titles (some of them appear split into two strings here)
      titles = job.xpath('.//text()').extract()
      # Turn list of strings into a single concatenated string
      a = "".join(titles)
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = "London"
      job_list.append({'Company': 'British Ecological Society',
                      'Job Title': a, 'Job URL': b, 'Location': c})


'''

# Create the Spider class
class Buglife(scrapy.Spider):
  name = "buglife"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  
  # start_requests method
  def start_requests(self):
    urls = ['https://www.buglife.org.uk/jobs/']
    for url in urls:
      yield scrapy.Request(url = url,
                        callback = self.parse)
    
  #First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.job_listing > a'):
      #Get the job titles
      a = job.xpath('.//h3/text()').extract_first()
      #Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      #Get the locations
      c = job.xpath('.//div[contains(@class,"location")]//text()').extract_first()
      job_list.append({'Company':'Buglife', 'Job Title':a, 'Job URL':b, 'Location':c})

'''

# Create the Spider class


class Bulb(scrapy.Spider):
  name = "bulb"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://bulb.co.uk/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.LeverJobs__JobGroup-sc-19g9okf-1 > div > div'):
      # Get the job titles
      a = job.xpath('./button/div/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./div/div//a/@href').extract_first()
      # Get the locations
      c = "London"
      job_list.append({'Company': 'Bulb', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Butterfly_Conservation(scrapy.Spider):
  name = "butterflyconservation"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    # Note that this is scraping an iframe within the careers page
    urls = ['https://butterflyconservation.livevacancies.co.uk/jobsIframe']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('table#jobsTable > tbody > tr'):
      # Get the job titles
      a = job.xpath('./td[1]/a//text()').extract_first().strip()
      # Get the URLs for those jobs
      b = job.xpath('./td[1]/a/@href').extract_first()
      # Get the locations
      c = job.xpath('./td[2]/a//text()').extract_first().strip()
      job_list.append({'Company': 'Butterfly Conservation',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Byway(scrapy.Spider):
  name = "byway"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.byway.travel/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h3 > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Sometimes this includes the whole URL, but sometimes it doesn't
      if 'http' not in b:
        b = 'https://www.byway.travel' + job.xpath('./@href').extract_first()
      # Get the locations
      c = "Hybrid remote with 2 days per month in London"
      job_list.append({'Company': 'Byway', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class CABI(scrapy.Spider):
  name = "cabi"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://cabi.ciphr-irecruit.com/templates/CIPHR/job_list.aspx']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('tr'):
      # Get the job titles
      a = job.xpath('./td[1]/a/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./td[1]/a/@href').extract_first()
      # Get the locations
      c = job.xpath('./td[2]/text()').extract_first()
      if a != None:
        job_list.append({'Company': 'CABI', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Cairngorms_National_Park(scrapy.Spider):
  name = "cairngormsnp"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.cairngorms.co.uk/Cairngorms/Home']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.job-summary > h3 > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://careers.cairngorms.co.uk' + \
          job.xpath('./@href').extract_first()
      # Get the locations
      c = "Scotland"
      job_list.append({'Company': 'Cairngorms National Park',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Carbon_Chain(scrapy.Spider):
  name = "carbonchain"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards-api.greenhouse.io/v1/boards/carbonchain/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['jobs']:
      # Get the job titles
      a = job['title']
      # All job descriptions are on the same URL
      b = job['absolute_url']
      # Get the locations
      c = job['location']['name']
      job_list.append({'Company': 'Carbon Chain',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class CAT(scrapy.Spider):
  name = "cat"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://cat.org.uk/vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('article.block--people__person'):
      # Get the job titles
      a = job.xpath('./a/h1/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./a/@href').extract_first()
      # Get the locations
      c = "Machynlleth, Powys, Wales"
      job_list.append({'Company': 'Centre for Alternative Technology',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Cenex(scrapy.Spider):
  name = "cenex"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.cenex.co.uk/join-us/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li > article.block'):
      # Get the job titles
      a = job.xpath('./h2/a/text()').extract_first()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b = job.xpath('./h2/a/@href').extract_first()
      # Get the locations
      c = job.xpath('./dl/dd[2]/text()').extract_first()
      job_list.append({'Company': 'Cenex', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Centre_Climate_Engagement(scrapy.Spider):
  name = "centreclimateengagement"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://climatehughes.org/join-our-climate-governance-initiative-team/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('article.join-our-climate-governance-initiative-team > p > strong'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # All job descriptions hosted on same URL
      b = 'https://www.hughes.cam.ac.uk/about/vacancies/'
      # Get the locations
      c = 'Cambridge'
      job_list.append({'Company': 'Centre for Climate Engagement',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Centre_Sustainable_Energy(scrapy.Spider):
  name = "centresustainableenergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.cse.org.uk/about-us/jobs-at-cse']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h2 > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.cse.org.uk'+job.xpath('./@href').extract_first()
      # Get the locations
      c = 'Bristol'
      job_list.append({'Company': 'Centre for Sustainable Energy',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Cervest(scrapy.Spider):
  name = "cervest"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards.greenhouse.io/cervest']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.opening'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first().title().strip()
      # Get the URLs for those jobs
      b = 'https://boards.greenhouse.io' + \
          job.xpath('./a/@href').extract_first()
      # Get the locations
      c = 'Fully Remote'
      # Get rid of US jobs
      if not any(x in a for x in ["- Us", "US"]):
        job_list.append({'Company': 'Cervest', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Changeworks(scrapy.Spider):
  name = "changeworks"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.changeworksrecycling.co.uk/recruitment/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.post-entry-content'):
      # Get the job titles
      a = job.xpath(
          './h4[contains(@class,"ele-entry-title")]/a/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath(
          './h4[contains(@class,"ele-entry-title")]/a/@href').extract_first()
      # Get the locations (includes a bunch of other stuff unfortunately but should be fine)
      c = job.xpath('./div/p/text()').extract_first()
      job_list.append({'Company': 'Changeworks Recycling',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Chargy(scrapy.Spider):
  name = "chargy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://chargy.bamboohr.com/jobs/embed2.php?version=1.0.0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.BambooHR-ATS-Jobs-Item'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https:'+job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./span/text()').extract_first().strip()
      job_list.append({'Company': 'char.gy', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Circa5000(scrapy.Spider):
  name = "circa5000"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://circa5000.com/team']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.w-full'):
      # Get the job titles
      a = job.xpath('./div[1]//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./div[4]/a/@href').extract_first()
      # Get the locations
      c = job.xpath('./div[2]//text()').extract_first()
      job_list.append({'Company': 'Circa5000', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class City_Of_Trees(scrapy.Spider):
  name = "cityoftrees"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.cityoftrees.org.uk/job-vacancies']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.field-name-body div.field-item.even > p > strong'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.cityoftrees.org.uk/job-vacancies'
      # Get the locations
      c = 'Greater Manchester'
      # Exclude crap (there's a lot of it)
      if a != None:
        unwanted = ['City of Trees Next Trustee', 'Interested in joining', 'For more information',
                    'have a full board', 'qualifications', 'For more information', 'week beginning', 'CLOSING DATE']
        if not any(x in a for x in unwanted):
          job_list.append({'Company': 'City of Trees',
                          'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Clean_Air_Fund(scrapy.Spider):
  name = "cleanairfund"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://cleanairfundcareers.org/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.job-card > div'):
      # Get the job titles
      a = job.xpath('./a/h4/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://cleanairfundcareers.org/' + \
          job.xpath('./a/@href').extract_first()
      # Filter out jobs not in London (alternatives are Delhi and Accra)
      c1 = job.xpath('./div/p[1]//text()').extract()
      # The line above produces a list of strings, so need to pick out the list item that contains the location
      c = c1[2].strip()
      if "London" in c:
        job_list.append({'Company': 'Clean Air Fund',
                        'Job Title': a, 'Job URL': b, 'Location': c})


'''

# Create the Spider class
class Client_Earth(scrapy.Spider):
  name = "clientearth"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  
  # start_requests method
  def start_requests(self):
    urls = ['https://jobs.clientearth.org/jobs/ajaxaction/posbrowser_gridhandler/?pagestamp=09bf0fd3-115f-4f8e-badb-6f2ada34f550&pageWidthInput=1000&availableWidthInput=NaN&gadgetsWidthInput=0&viewMode=null&inDialog=false']
    for url in urls:
      yield scrapy.Request(url = url,
                        callback = self.parse)
    
  #First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.rowContainer'):
      #Get the job titles
      a = job.xpath('./div[1]//a/text()').extract_first()
      #Get the URLs for those jobs
      b = 'https://jobs.clientearth.org' + job.xpath('./div[1]//a/@href').extract_first()
      #Get the locations
      c = job.xpath('.//div[contains(@class,"rowItemsInnerContainer2")]/span[1]/text()').extract_first()
      job_list.append({'Company':'Client Earth', 'Job Title':a, 'Job URL':b, 'Location':c})

'''

# Create the Spider class


class Climate_Change_Committee(scrapy.Spider):
  name = "climatechangecommittee"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.theccc.org.uk/about/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('article#careers > p a'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      c = 'London'
      # Exclude crap
      if b != None and a != None:
        if "Equality, Diversity and Inclusion Strategy" not in a:
          job_list.append({'Company': 'Climate Change Committee',
                          'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Climate_Connect_Digital(scrapy.Spider):
  name = "climateconnectdigital"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://climateconnect-1637733040080.freshteam.com/hire/widgets/jobs.json']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['jobs']:
      # Get the job titles
      a = job['title']
      # Get the URLs for those jobs
      b = job['url']
      # Get locations (only one is in the UK so also exclude the rest)
      c1 = job['branch_id']
      if c1 == 25000011811:
        c = "London"
        job_list.append({'Company': 'Climate Connect Digital',
                        'Job Title': a, 'Job URL': b, 'Location': c})


job_desc_urls_climpart = []
# Create the Spider class


class Climate_Impact_Partners(scrapy.Spider):
  name = "climateimpactpartners"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.climateimpact.com/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape links to individual job pages
  def parse(self, response):
    for job in response.css('div#jobs > div > ul > li > a'):
      # Get the URLs for each job listed on the page
      url = job.xpath('./@href').extract_first()
      # Add those URLs to a (initially empty) list so we can use them in the next for loop
      job_desc_urls_climpart.append(url)
    # Tell it to scrape the job description page for each job
    for job in job_desc_urls_climpart:
      yield scrapy.Request(url=job, callback=self.parse_job_desc)

  # Second parsing method to scrape job titles and locations
  def parse_job_desc(self, response):
    # Get the job titles
    a = response.css(
        'h1.font-company-header').xpath('.//text()').extract_first().strip()
    # Get the locations
    c = 'Oxford or London'
    job_list.append({'Company': 'Climate Impact Partners',
                    'Job Title': a, 'Job URL': response.url, 'Location': c})


# Create the Spider class
class Climate_Policy_Radar(scrapy.Spider):
  name = "climatepolicyradar"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://climatepolicyradar.org/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('a.c-card'):
      # Get the job titles
      a = job.xpath('./div/h3/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://climatepolicyradar.org' + \
          job.xpath('./@href').extract_first()
      # Get the locations
      c = 'London'
      job_list.append({'Company': 'Climate Policy Radar',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class ClimateX(scrapy.Spider):
  name = "climatex"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.climate-x.com/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h2.sppb-addon-title > a'):
      # Get the job titles. Sometimes they include line breaks to make things complicated
      a1 = job.xpath('.//text()').extract()
      if len(a1) == 1:
        a = a1[0]
      else:
        a = " ".join(a1).replace("  ", " ")
      # Get the URLs for those jobs
      b = 'https://www.climate-x.com'+job.xpath('./@href').extract_first()
      # Get the locations
      c = "London"
      #Exclude US jobs
      if "USA" not in a:
        job_list.append({'Company': 'Climate X', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Cogo(scrapy.Spider):
  name = "cogo"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://cogo.bamboohr.com/jobs/embed2.php?version=1.0.0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.BambooHR-ATS-Jobs-Item'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https:'+job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./span/text()').extract_first().strip()
      job_list.append({'Company': 'Cogo', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Common_Seas(scrapy.Spider):
  name = "commonseas"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://commonseas.com/about']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.textowl.text-18 p > strong > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get locations
      c = 'London'
      job_list.append(
          {'Company': 'Common Seas', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Cultivate_London(scrapy.Spider):
  name = "cultivatelondon"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://cultivatelondon.org/job-vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('button.w-tabs-section-header'):
      # Get the job titles
      a = job.xpath('./div[1]/text()').extract_first()
      # All job descriptions are on the same URL
      b = 'https://cultivatelondon.org/job-vacancies/'
      # Get the locations
      c = "London"
      job_list.append({'Company': 'Cultivate London',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Decent_Packaging(scrapy.Spider):
  name = "decentpackaging"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://decentpackaging.co.uk/blogs/%D1%81areers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.careers-blog-list__item-info > div.careers-blog-list__item-container'):
      # Get the job titles
      a = job.xpath('./div[1]/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://decentpackaging.co.uk' + \
          job.xpath('./a/@href').extract_first()
      # Get the locations
      c = 'London'
      # Exclude crap
      if "We're always keen" not in a:
        job_list.append({'Company': 'Decent Packaging',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Delphis(scrapy.Spider):
  name = "delphis"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://delphiseco.com/pages/work-for-us']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.rte.clearfix.text-content > p > strong'):
      # Get the job titles (and trim whitespace)
      a = job.xpath('./text()').extract_first().strip().replace(":", "")
      # All job descriptions are on the same URL
      b = 'https://delphiseco.com/pages/work-for-us'
      # Get the locations
      c = "London"
      # Filter out all the other crap I can't work out how to exclude any other way
      unwanteds = ["Careers", "careers", "Pushing", "info", "Initiative",
                   "Driven", "Confident", "Personable", "Eco-friendly!"]
      if a != "" and not any(x in a for x in unwanteds):
        job_list.append({'Company': 'Delphis', 'Job Title': a,
                        'Job URL': b, 'Location': c})


'''

# Create the Spider class
class DeSmog(scrapy.Spider):
  name = "desmog"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  
  # start_requests method
  def start_requests(self):
    urls = ['https://www.desmog.com/jobs/']
    for url in urls:
      yield scrapy.Request(url = url,
                        callback = self.parse)
    
  #First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.elementor-widget-container > p > a'):
      #Get the job titles
      a = job.xpath('.//text()').extract_first()
      #Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      #Get the locations
      c = 
      #Filter out all the other crap I can't work out how to exclude any other way
      unwanteds = ["Newsletter", "Subscribe", "Donate"]
      if not any(x in a for x in unwanteds):
        job_list.append({'Company':'DeSmog', 'Job Title':a, 'Job URL':b, 'Location':c})

'''

# Create the Spider class


class Dizzie(scrapy.Spider):
  name = "dizzie"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://help.getdizzie.com/en/collections/2937080-jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.g__space > a'):
      # Get the job titles
      a = job.xpath('.//h2//text()').extract_first()
      # All job descriptions are on the same page
      b = 'https://help.getdizzie.com' + job.xpath('./@href').extract_first()
      # Get the locations
      c = 'London'
      # Scrap the crap
      if 'brilliant people' not in a:
        job_list.append({'Company': 'Dizzie', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Dulas(scrapy.Spider):
  name = "dulas"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://dulas.org.uk/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.fusion-text.fusion-text-1 a'):
      # Get the job titles
      a = job.xpath(
          './text()').extract_first().replace("– Application pack", "").strip()
      # All job descriptions need to be downloaded from the same URL
      b = 'https://dulas.org.uk/careers/'
      # Get the locations
      c = "Machynlleth, Powys, Wales"
      job_list.append({'Company': 'Dulas', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Earth_Trust(scrapy.Spider):
  name = "earthtrust"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://earthtrust.org.uk/get-involved/vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.grid-item > a'):
      # Get the job titles
      a = job.xpath('.//h3/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'Near Abingdon, Oxfordshire'
      # Exclude crap
      job_list.append(
          {'Company': 'Earth Trust', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Earthly(scrapy.Spider):
  name = "earthly"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards-api.greenhouse.io/v1/boards/earthly/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['jobs']:
      # Get the job titles
      a = job['title']
      # All job descriptions are on the same URL
      b = job['absolute_url']
      # Get the locations
      c = job['location']['name']
      job_list.append({'Company': 'Earthly', 'Job Title': a,
                      'Job URL': b, 'Location': c})


job_desc_urls_earthwatch = []
# Create the Spider class


class Earthwatch(scrapy.Spider):
  name = "earthwatch"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://earthwatch.org.uk/who-we-are/work-with-us/jobs-and-internships']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape links to individual job pages
  def parse(self, response):
    for job in response.css('a.moduleItemTitle'):
      # Get the URLs for each job listed on the page
      url = 'https://earthwatch.org.uk'+job.xpath('./@href').extract_first()
      # Add those URLs to a (initially empty) list so we can use them in the next for loop
      job_desc_urls_earthwatch.append(url)
    # Tell it to scrape the job description page for each job
    for job in job_desc_urls_earthwatch:
      yield scrapy.Request(url=job, callback=self.parse_job_desc)

  # Second parsing method to scrape job titles and locations
  def parse_job_desc(self, response):
    # Get the job titles
    a = response.css('h2.itemTitle').xpath('./text()').extract_first().strip()
    # Get the locations
    c = response.css('div.itemFullText').xpath('./p[1]/text()').extract_first()
    # Remove Dutch jobs
    if 'Netherlands' not in c:
      job_list.append({'Company': 'Earthwatch', 'Job Title': a,
                      'Job URL': response.url, 'Location': c})


# Create the Spider class
class EcoACTIVE(scrapy.Spider):
  name = "ecoactive"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.ecoactive.org.uk/vacancies']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h2'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # All job descriptions are on the same URL
      b = 'https://www.ecoactive.org.uk/vacancies'
      # Get the locations
      c = "London"
      job_list.append({'Company': 'EcoACTIVE', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Ecologi(scrapy.Spider):
  name = "ecologi"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.ecologi.com/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    # Need to only select ul elements without a class here
    for job in response.css('ul:not([class]) > li.w-full > a'):
      # Get the job titles
      a = job.xpath('./span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = job.xpath('./div/span[3]/text()').extract_first().strip()
      if c == 'Hybrid Remote':
        c = 'Fully Remote'
      # Exclude non-jobs and US jobs
      unwanteds = ["Join Our", "Join our", "US"]
      if not any(x in a for x in unwanteds):
        job_list.append({'Company': 'Ecologi', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Ecosia(scrapy.Spider):
  name = "ecosia"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://jobs.lever.co/ecosia']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('a.posting-title'):
      # Get the job titles
      a = job.xpath('./h5/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = job.xpath('./div/span/text()').extract_first()
      if 'remote' in c:
        job_list.append({'Company': 'Ecosia', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Ecosulis(scrapy.Spider):
  name = "ecosulis"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://ecosulis.bamboohr.com/jobs/embed2.php?version=1.0.0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.BambooHR-ATS-Jobs-Item'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https:'+job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./span/text()').extract_first().strip()
      job_list.append({'Company': 'Ecosulis', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Eden_Rivers_Trust(scrapy.Spider):
  name = "edenriverstrust"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.edenriverstrust.org.uk/jobs/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    # Need to only select ul elements without a class here
    for job in response.css('section.flexible-content-panel.single-column-panel.light-background > div.container > div.row > div.col-xs-12 > div.flexible-content-holder'):
      # Get the job titles
      a = job.xpath('./p[1]//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./p[1]//a/@href').extract_first()
      # Get the locations
      c = "Penrith"
      # Exclude crap
      if "We will always acknowledge" not in a:
        job_list.append({'Company': 'Eden Rivers Trust',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Ember(scrapy.Spider):
  name = "ember"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://ember-climate.org/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.vacancy-single'):
      # Get the job titles
      a = job.xpath('./div[1]/h4//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./div[2]/a/@href').extract_first()
      # Get the locations
      c = job.xpath('.//div[@class="vacancy-location"]/text()').extract_first()
      # Exclude jobs in Asia
      if 'Asia' not in a:
        job_list.append({'Company': 'Ember', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Emitwise(scrapy.Spider):
  name = "emitwise"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://jobs.lever.co/emitwise']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('a.posting-title'):
      # Get the job titles
      a = job.xpath('./h5/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the location
      c = job.xpath('./div/span/text()').extract_first()
      job_list.append({'Company': 'Emitwise', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Energy_Climate_Intelligence_Unit(scrapy.Spider):
  name = "energyclimateintelligenceunit"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://eciu.net/about/vacancies']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.mb-8 > ul > li > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'London'
      job_list.append({'Company': 'Energy & Climate Intelligence Unit',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Environment_Agency(scrapy.Spider):
  name = "environmentagency"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://environmentagencyjobs.tal.net/candidate/jobboard/vacancy/1/adv']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('tr.search_res'):
      # Get the job titles
      a1 = job.xpath('./td/a//text()').extract_first().strip()
      # Get rid of the " - xxxxx" internal job reference and tidy up
      a2 = a1[:-7]
      a = a2.strip()
      # Get the URLs for those jobs
      b = job.xpath('./td/a/@href').extract_first()
      # Get the locations
      c = job.xpath('./td[5]/text()').extract_first().strip()
      if c == 'All' or c == 'Various' or c == 'All, Various' or c == 'Home Working , Various' or c == 'Home Working, Various' or c == 'Home Working , All':
        c = 'England, United Kingdom'
      job_list.append({'Company': 'Environment Agency',
                      'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
    next_page = response.css('div.paging > span.next_links > a').xpath(
        './@href').extract_first()
    if next_page != None:
      yield scrapy.Request(url='https://environmentagencyjobs.tal.net/candidate/jobboard/vacancy/1/adv'+next_page)


# Create the Spider class
class Environmental_Defense_Fund(scrapy.Spider):
  name = "environmentaldefensefund"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.edf.org/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('tr'):
      # Get the job titles
      a = job.xpath('./td[1]/a/text()').extract_first()
      # Get the URLs for those jobs
      b1 = job.xpath('./td[1]/a/@href').extract_first()
      if b1 != None:
        b = 'https://www.edf.org' + b1
      # Get the locations
      c = job.xpath('./td[2]/text()').extract_first()
      if c != None:
        c = c.strip()
      # Exclude crap
      if a != None:
        job_list.append({'Company': 'Environmental Defense Fund',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class EIA(scrapy.Spider):
  name = "eia"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://eia-international.org/about-us/jobs/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    # Job titles and URLs don't have a shared container, so having to do this a different way
    i = 0
    # This is still just looking at job titles and determining the length of the for loop
    for job in response.css('div.wysiwyg > h3'):
      i = i + 1
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      # Need to add the variable i into the xpath string to make this work
      b1 = './p[' + str(i) + ']/a/@href'
      b = response.css('div.wysiwyg').xpath(b1).extract_first()
      # Get the locations
      c = "London"
      job_list.append({'Company': 'Environmental Investigation Agency',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Enviral(scrapy.Spider):
  name = "enviral"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.enviral.co.uk/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.careers-vacancies-section__vacancy-single'):
      # Get the job titles and put them in title case
      a = job.xpath('./h3/text()').extract_first()
      # All job descriptions are on the same URL
      b = 'https://www.enviral.co.uk/careers/'
      # Get the locations
      c = "Bristol"
      job_list.append({'Company': 'Enviral', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Equilibrium_Energy(scrapy.Spider):
  name = "equilibriumenergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards.greenhouse.io/equilibriumenergy']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.opening'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://boards.greenhouse.io' + \
          job.xpath('./a/@href').extract_first()
      # Get the locations
      c = 'Fully Remote'
      job_list.append({'Company': 'Equilibrium Energy',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class EVenergy(scrapy.Spider):
  name = "evenergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://api.teamtailor.com/v1/jobs?&api_key=eknPI3TmDakpDOolH1j8NFp7jmB8WQyai9WK8RQL&api_version=20161108&include=department,role,regions,locations&fields[departments]=name&fields[roles]=name&fields[locations]=name,city&fields[regions]=name&page[size]=20&filter[feed]=public&']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['data']:
      # Get the job titles
      a = job['attributes']['title']
      # Get the URLs for those jobs
      b = job['links']['careersite-job-url']
      # Get the location. This one is messy with a self-referencing API with optional fields
      # Check if the city is filled in
      c0 = job['relationships']['locations']['data']
      # If the city is filled in, store it in c. Otherwise, set c to be an empty string
      if c0 != []:
        print(c0)
        c1 = [location['id'] for location in c0]
        print(c1)
        org_locations = data['included']
        job_locations = []
        for item in org_locations:
          if item['id'] in c1:
            job_locations.append(item['attributes']['city'])
        print(job_locations)
        if 'London' in job_locations:
          c = 'Fully Remote'
          job_list.append(
              {'Company': 'EV.energy', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Fidra(scrapy.Spider):
  name = "fidra"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.fidra.org.uk/about-us/vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h2'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # All job descriptions are on the same page
      b = 'https://www.fidra.org.uk/about-us/vacancies/'
      # Get the locations
      c = 'North Berwick'
      job_list.append({'Company': 'Fidra', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Finance_Earth(scrapy.Spider):
  name = "financeearth"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://finance.earth/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.listing-summary'):
      # Get the job titles
      a = job.xpath('./p[1]/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./ul/li/a/@href').extract_first()
      # Get the locations
      c = "London"
      job_list.append({'Company': 'Finance Earth',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Finisterre(scrapy.Spider):
  name = "finisterre"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://finisterre.com/pages/workshop-opportunities']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.reveal > div > div'):
      # Get the job titles and tidy them up
      a1 = job.xpath('.//text()').extract()
      a = "".join(a1).strip()
      # All job descriptions are on the same URL (unless you want everyone to unexpectedly download a pdf)
      b = 'https://finisterre.com/pages/workshop-opportunities'
      # Get the locations
      c = "St Agnes, Cornwall"
      job_list.append({'Company': 'Finisterre', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class First_Mile(scrapy.Spider):
  name = "firstmile"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://thefirstmile.co.uk/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.vacancy'):
      # Get the job titles
      a = job.xpath('./h5/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./a/@href').extract_first()
      # Get the locations
      c = "London"
      job_list.append({'Company': 'First Mile', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Forest_Of_Marston_Vale(scrapy.Spider):
  name = "marstonvale"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.marstonvale.org/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h2'):
      # Get the job titles and tidy them up
      a1 = job.xpath('.//text()').extract_first()
      # Remove all content inside parentheses (these are salary ranges here)
      a = re.sub(r'\([^)]*\)', '', a1)
      # Get the URLs for those jobs
      b = 'https://www.marstonvale.org/jobs'
      # Get the locations
      c = 'Marston Vale'
      # Exclude crap
      if not any(x in a for x in ['Latest', 'Most read', 'Sign up']):
        job_list.append({'Company': 'Forest of Marston Vale',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Freshwater_Biological_Association(scrapy.Spider):
  name = "freshwaterbiologicalassociation"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.fba.org.uk/working-at-fba']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li > p > a'):
      # Get the job titles and tidy them up
      a = job.xpath('./text()').extract_first()
      # Remove the weird bit from a trustee job title
      if a != None and 'Role description' in a:
        a = a.replace("Role description", "").strip()
      # Remove the '.pdf' part of some other job titles
      if a != None and 'pdf' in a:
        a = a.replace(".pdf", "").strip()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'Lake District'
      job_list.append({'Company': 'Freshwater Biological Association',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Friends_Earth(scrapy.Spider):
  name = "friendsearth"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://jobs.friendsoftheearth.uk/vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.vacancy-details'):
      # Get the job titles
      a = job.xpath('./h3/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://jobs.friendsoftheearth.uk' + \
          job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath(
          './/div[contains(@class,"value_location")]/text()').extract_first()
      job_list.append({'Company': 'Friends of the Earth',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Futerra(scrapy.Spider):
  name = "futerra"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://wearefuterra.com/about']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.item > div.justify-between'):
      # Get the job titles
      a = job.xpath('./div[2]/div/div[1]/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./div[2]/a/@href').extract_first()
      # Get the locations
      c = job.xpath('./div[2]/div/div[2]/text()').extract_first()
      job_list.append({'Company': 'Futerra', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Galapagos_Conservation_Trust(scrapy.Spider):
  name = "galapagosconservationtrust"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://galapagosconservation.org.uk/about-us/careers-and-volunteers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h3'):
      # Get the job titles and tidy them up
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://galapagosconservation.org.uk/about-us/careers-and-volunteers/'
      # Get the locations
      c = "London"
      # Exclude crap
      if a != None and a != "" and not any(x in a for x in ['Job Description', 'Person Specification', 'To Apply', 'Opportunities in Galapagos', 'Central London (Borough)', 'Volunteer Application Form']):
        job_list.append({'Company': 'Galapagos Conservation Trust',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Global_Witness(scrapy.Spider):
  name = "globalwitness"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.globalwitness.org/en/jobs/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('ul.wide-listing > li'):
      # Get the job titles and tidy them up
      a = job.xpath('./div[2]/a/h3/text()').extract_first().replace(
          " - Open to flexible working", "").replace(" (Open to flexible working)", "")
      # Get the URLs for those jobs
      b = 'https://www.globalwitness.org' + \
          job.xpath('./div[2]/a/@href').extract_first()
      # Get the locations and tidy them up
      c = job.xpath(
          './div[1]/div/text()').extract_first().strip().replace("Location: ", "")
      job_list.append({'Company': 'Global Witness',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Granular(scrapy.Spider):
  name = "granular"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://jobs.lever.co/Granular']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('a.posting-title'):
      # Get the job titles
      a = job.xpath('./h5/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = job.xpath('./div/span/text()').extract_first()
      job_list.append({'Company': 'Granular', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Green_Alliance(scrapy.Spider):
  name = "greenalliance"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://green-alliance.org.uk/vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h3'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      if 'Chair' in a:
        a = 'Chair of the Board'
      # All job descriptions need to be downloaded from the same URL
      b = 'https://green-alliance.org.uk/vacancies/'
      # Get the locations
      c = 'London'
      job_list.append({'Company': 'Green Alliance',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Greenpeace(scrapy.Spider):
  name = "greenpeace"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://jobs.greenpeace.org.uk/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.job'):
      # Get the job titles
      a = job.xpath('.//h5/a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://jobs.greenpeace.org.uk/' + \
          job.xpath('.//h5/a/@href').extract_first()
      # Get the locations
      c = job.xpath(
          './/li[@class = "job-location"]/text()').extract_first().strip()
      job_list.append({'Company': 'Greenpeace', 'Job Title': a,
                      'Job URL': b, 'Location': c})


job_desc_urls_groundcontrol = []
# Create the Spider class


class Ground_Control(scrapy.Spider):
  name = "groundcontrol"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.ground-control.co.uk/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape links to individual job pages
  def parse(self, response):
    for job in response.css('li.block-grid-item > a'):
      # Get the URLs for each job listed on the page
      url = job.xpath('./@href').extract_first()
      # Add those URLs to a (initially empty) list so we can use them in the next for loop
      job_desc_urls_groundcontrol.append(url)
    # Tell it to scrape the job description page for each job
    for job in job_desc_urls_groundcontrol:
      yield scrapy.Request(url=job, callback=self.parse_job_desc)

  # Second parsing method to scrape job titles and locations
  def parse_job_desc(self, response):
    # Get the job titles
    a = response.css(
        'h1.font-company-header').xpath('./text()').extract_first()
    # Get the locations. Bit funky here as have to select the element after the element that says 'Locations' and ignore everything else
    for ele in response.css('dt'):
      c1 = ele.xpath('./text()').extract_first()
      if c1 == 'Locations':
        c = ele.xpath('./following-sibling::dd/text()').extract_first().strip()
        # Occasionally this doesn't work and the locations are presented in a different way
        if c == "":
          c = ele.xpath(
              './following-sibling::dd/span/@title').extract_first().strip()
        # The location being 'Head Office' isn't helpful, so we need to replace that
        if c != None:
          c = c.replace("Head Office", "Billericay")
        job_list.append({'Company': 'Ground Control', 'Job Title': a,
                        'Job URL': response.url, 'Location': c})


# Create the Spider class
class Guru_Systems(scrapy.Spider):
  name = "gurusystems"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://gurusystems.com/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.fusion-column-wrapper.fusion-flex-justify-content-flex-start.fusion-content-layout-column'):
      # Get the job titles and put them in title case
      a = job.xpath('./div/h6//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./div/a/@href').extract_first()
      # Get the locations
      c = "London"
      # Remove the non-jobs being scraped that I don't know how to avoid
      if b != None:
        job_list.append({'Company': 'Guru Systems',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Heal_Rewilding(scrapy.Spider):
  name = "healrewilding"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.healrewilding.org.uk/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div[data-testid="mesh-container-content"]'):
      # Get the job titles
      a = job.xpath('.//h3//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./div[7]/a/@href').extract_first()
      # Get the locations
      c1 = job.xpath('./div[6]//text()').extract()
      c = ", ".join(c1)
      if a != None and not any(x in a for x in ['Stay in touch', 'Working with Heal']):
        job_list.append({'Company': 'Heal Rewilding',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Heart_Of_England_Forest(scrapy.Spider):
  name = "heartofenglandforest"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://heartofenglandforest.org/jobs-and-careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('p a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'Warwickshire'
      if not any(x in a for x in ['Get advice and tips', 'we choose to pay']):
        job_list.append({'Company': 'Heart of England Forest',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Heura(scrapy.Spider):
  name = "heura"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://api.teamtailor.com/v1/jobs?&api_key=wYcAmJxo_ufaNijCdYhi_qQUfzEZ0xPxI3HHP7SY&api_version=20161108&include=department,role,regions,locations&fields[departments]=name&fields[roles]=name&fields[locations]=name,city&fields[regions]=name&page[size]=30&filter[feed]=public&filter[locations]=%22London%22&']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['data']:
      # Get the job titles
      a = job['attributes']['title']
      # Get the URLs for those jobs
      b = job['links']['careersite-job-url']
      # Get the location. This one is messy with a self-referencing API with optional fields
      # Check if the city is filled in
      c0 = job['relationships']['locations']['data']
      # If the city is filled in, store it in c. Otherwise, set c to be an empty string
      if c0 != []:
        c1 = job['relationships']['locations']['data'][0]['id']
        c2 = data['included']
        for item in c2:
          if item['id'] == c1:
            c3 = item['attributes']['city']
      else:
        c3 = ""
      # Check if the job is remote (this seems to always be filled in, hopefully it stays that way), then append that status to the location (unless it's not remote)
      remote = job['attributes']['remote-status']
      if remote != "none":
        c = c3 + " - " + remote + " remote"
      else:
        c = c3
      job_list.append({'Company': 'Heura', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Higher_Steaks(scrapy.Spider):
  name = "highersteaks"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://api.teamtailor.com/v1/jobs?&api_key=SN4Omb1K4NRbPOlXqGt6JuIznfx5J4muK71N0oBD&api_version=20161108&include=department,role,regions,locations&fields[departments]=name&fields[roles]=name&fields[locations]=name,city&fields[regions]=name&page[size]=20&filter[feed]=public&']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['data']:
      # Get the job titles
      a = job['attributes']['title']
      # Get the URLs for those jobs
      b = job['links']['careersite-job-url']
      # Get the location. This one is messy with a self-referencing API with optional fields
      # Check if the city is filled in
      c0 = job['relationships']['locations']['data']
      # If the city is filled in, store it in c. Otherwise, set c to be an empty string
      if c0 != []:
        c1 = job['relationships']['locations']['data'][0]['id']
        c2 = data['included']
        for item in c2:
          if item['id'] == c1:
            c3 = item['attributes']['name']
      else:
        c3 = ""
      # Check if the job is remote (this seems to always be filled in, hopefully it stays that way), then append that status to the location (unless it's not remote)
      remote = job['attributes']['remote-status']
      if remote != "none":
        c = c3 + " - " + remote + " remote"
      else:
        c = c3
      # Filter out non-UK jobs
      job_list.append({'Company': 'Higher Steaks',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Highview_Power(scrapy.Spider):
  name = "highviewpower"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://highviewpower.com/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.job_box'):
      # Get the job titles
      a = job.xpath('./div[1]/h3/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./div[3]/a/@href').extract_first()
      # Get the locations
      c = job.xpath('./div[2]/p[2]/text()').extract_first()
      # Exclude crap
      job_list.append({'Company': 'Highview Power',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Hubbub(scrapy.Spider):
  name = "hubbub"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.hubbub.org.uk/job-opportunities']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div > h2'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.hubbub.org.uk/job-opportunities'
      # Get the locations
      c = "London"
      job_list.append({'Company': 'Hubbub', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class IIGCC(scrapy.Spider):
  name = "iigcc"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.iigcc.org/about-us/vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('main.site-main > div > p > strong > a'):
      # Get the job titles & tidy them up
      a = job.xpath('./text()').extract_first().strip()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'London'
      job_list.append({'Company': 'IIGCC', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Inclusive_Energy(scrapy.Spider):
  name = "inclusiveenergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://inclusive.energy/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('article.BlogList-item'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://inclusive.energy' + job.xpath('./a/@href').extract_first()
      # Get the locations (hopefully this is the case for all future jobs too)
      c = 'Edinburgh or London'
      job_list.append({'Company': 'Inclusive Energy',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Innocent(scrapy.Spider):
  name = "innocent"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://innocent.avature.net/externalcareers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.listSingleColumnItem'):
      # Get the job titles
      a = job.xpath('./h3/a/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./h3/a/@href').extract_first()
      # Get the locations
      c = job.xpath('./p/span/text()').extract_first()
      job_list.append({'Company': 'Innocent', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Kaluza(scrapy.Spider):
  name = "kaluza"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.kaluza.com/open-jobs/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('a.MuiBox-root'):
      # Get the job titles and tidy them up
      a = job.xpath('./div[1]/div[1]/p/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://careers.kaluza.com' + job.xpath('./@href').extract_first()
      # Get the locations and tidy them up
      c1 = job.xpath('./div[1]/div[2]/div[1]/div//text()').extract()
      c = ", ".join(c1)
      # Exclude crap
      if a != None:
        job_list.append({'Company': 'Kaluza', 'Job Title': a,
                        'Job URL': b, 'Location': c})


job_desc_urls_keep_britain_tidy = []
# Create the Spider class


class Keep_Britain_Tidy(scrapy.Spider):
  name = "keepbritaintidy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.keepbritaintidy.org/get-involved/work-for-us']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape links to individual job pages
  def parse(self, response):
    for job in response.css('li.related-nav__list__item > a'):
      # Get the URLs for each job listed on the page
      url = 'https://www.keepbritaintidy.org' + \
          job.xpath('./@href').extract_first()
      # Add those URLs to a (initially empty) list so we can use them in the next for loop
      job_desc_urls_keep_britain_tidy.append(url)
    # Tell it to scrape the job description page for each job
    for job in job_desc_urls_keep_britain_tidy:
      yield scrapy.Request(url=job, callback=self.parse_job_desc)

  # Second parsing method to scrape job titles and locations
  def parse_job_desc(self, response):
    # Get the job titles
    a = response.css('h1').xpath('./text()').extract_first()
    # Get the locations. Have to find the <p> element that contains the location, then go back up a step to actually pull the location
    for ele in response.css('div.std-content > p'):
      if ele.xpath('./strong/text()').extract_first() == "Location:" or ele.xpath('./strong/text()').extract_first() == "Location":
        c = ele.xpath('./text()').extract_first().strip()
        job_list.append({'Company': 'Keep Britain Tidy',
                        'Job Title': a, 'Job URL': response.url, 'Location': c})


# Create the Spider class
class KeepCup(scrapy.Spider):
  name = "keepcup"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://uk.keepcup.com/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.column.main div.constrained-block.image-text-columns > div.pagebuilder-column-group'):
      # Get the job titles
      a = job.xpath('.//h4//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('.//a/@href').extract_first()
      # Get locations
      c = job.xpath('.//text()').extract()
      # Clunkily exclude all the crap I'm wading through
      unwanteds = ['Why we love coming to work', 'Global openings',
                   'find a role matching your skills', 'Image LHS']
      if a != None:
        if not any(x in a for x in unwanteds):
          if '3234895233' not in b:
            if 'London' in c[2]:
              job_list.append(
                  {'Company': 'KeepCup', 'Job Title': a, 'Job URL': b, 'Location': c[2]})


# Create the Spider class
class Keep_Scotland_Beautiful(scrapy.Spider):
  name = "keepscotlandbeautiful"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.keepscotlandbeautiful.org/about-us/join-us/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('a.jobLink'):
      # Get the job titles
      a = job.xpath('./div/p[1]/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.keepscotlandbeautiful.org' + \
          job.xpath('./@href').extract_first()
      # Get the locations
      c = job.xpath('./div/p[3]/text()').extract_first().strip()
      # Exclude crap
      job_list.append({'Company': 'Keep Scotland Beautiful',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Knepp_Wildland_Foundation(scrapy.Spider):
  name = "kneppwildlandfoundation"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.kneppwildlandfoundation.org/get-involved']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.list-item-content__text-wrapper'):
      # Get the job titles
      a = job.xpath('./h2/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.kneppwildlandfoundation.org/get-involved'
      # Get the locations
      c = 'Sussex'
      job_list.append({'Company': 'Knepp Wildland Foundation',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Leanpath(scrapy.Spider):
  name = "leanpath"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://leanpath.bamboohr.com/jobs/embed2.php?version=1.0.0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.BambooHR-ATS-Jobs-Item'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https:'+job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./span/text()').extract_first().strip()
      job_list.append({'Company': 'Leanpath', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Lime(scrapy.Spider):
  name = "lime"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://jobs.lever.co/lime']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('a.posting-title'):
      # Get the job titles
      a = job.xpath('./h5/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Check whether it's remote or not
      c1 = job.xpath('./div/span[3]/text()').extract_first()
      # Now get the location, and check it's in the UK
      uk = ['EMEA', 'London', 'UK', 'United Kingdom']
      c2 = job.xpath('./div/span[1]/text()').extract_first()
      if any(x in c2 for x in uk):
        # Tag as Remote or by location if not Remote
        if "Remote" in c1:
          c = "Fully Remote"
        else:
          c = c2
        job_list.append({'Company': 'Lime', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Living_Streets(scrapy.Spider):
  name = "livingstreets"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.livingstreets.org.uk/about-us/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.job-entry'):
      # Get the job titles
      a = job.xpath('./div[1]/p[1]/text()').extract_first().strip()
      # Get the URLs for those jobs
      b = 'https://www.livingstreets.org.uk' + \
          job.xpath('./div[2]/a/@href').extract_first()
      # Get the locations
      c1 = job.xpath('./div[1]/p[2]/span/text()').extract_first()
      if c1 == 'England':
        c = 'London'
      else:
        c = c1
      job_list.append({'Company': 'Living Streets',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Low_Carbon(scrapy.Spider):
  name = "lowcarbon"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://lowcarbon.bamboohr.com/jobs/embed2.php?version=1.0.0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.BambooHR-ATS-Jobs-Item'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https:'+job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./span/text()').extract_first().strip()
      job_list.append({'Company': 'Low Carbon', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Lucy_Yak(scrapy.Spider):
  name = "lucyyak"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://lucyandyak.com/pages/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.rte > p a'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations (generally included in the job title)
      c = a
      # Exclude crap
      if a != None:
        job_list.append(
            {'Company': 'Lucy & Yak', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Lunar_Energy(scrapy.Spider):
  name = "lunarenergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards.greenhouse.io/lunarenergy']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.opening'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://boards.greenhouse.io' + \
          job.xpath('./a/@href').extract_first()
      # Get the locations
      c1 = job.xpath('./span/text()').extract_first()
      if 'UK' in c1:
        c = 'Fully Remote'
        job_list.append({'Company': 'Lunar Energy',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Lune(scrapy.Spider):
  name = "lune"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://lune.crew.work/assets/company.json']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['jobs']:
      # Get the job titles
      a = job['name']
      # Get the URLs for those jobs
      b = 'https://lune.crew.work/jobs/' + job['id']
      # Get the locations
      c = job['location']
      job_list.append({'Company': 'Lune', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Manufacture_2030(scrapy.Spider):
  name = "manufacture2030"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://manufacture2030.com/about-us/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.c-job-listing__item'):
      # Get the job titles
      a = job.xpath('.//h3/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://manufacture2030.com' + \
          job.xpath('.//a/@href').extract_first()
      # Get the locations
      c = "Oxford"
      job_list.append({'Company': 'Manufacture 2030',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Matter(scrapy.Spider):
  name = "matter"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://odtalentsolutionslimited.teamtailor.com/departments/matter']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li > a.focus-visible-company'):
      # Get the job titles
      a = job.xpath('./span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c1 = job.xpath('./div/span[3]/text()').extract_first()
      # That works most of the time, but some jobs don't have the department listed, so there's not always another span before the location span
      if c1 != None:
        c2 = c1
      else:
        c2 = job.xpath('./div/span[1]/text()').extract_first().strip()
      # Weird indentations and spaces sometimes
      c = c2.strip()
      job_list.append({'Company': 'Matter', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Midsummer_Energy(scrapy.Spider):
  name = "midsummerenergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://midsummerwholesale.co.uk/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    # Get the Cambridge jobs first
    for job in response.xpath('//h2[contains(., "Open Positions in Cambridge:")]/following-sibling::div[not(preceding-sibling::h2[contains(., "Open Positions in Glasgow:")])]'):
      # Get the job titles
      a = job.xpath('./div/b/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./span//a/@href').extract_first()
      # These are the Cambridge jobs, so put that in
      c = 'Cambridge'
      # Exclude crap
      if a != None:
        job_list.append({'Company': 'Midsummer Energy',
                        'Job Title': a, 'Job URL': b, 'Location': c})

    # Now the Glasgow jobs
    for job in response.xpath('//h2[contains(., "Open Positions in Glasgow:")]/following-sibling::div'):
      # Get the job titles
      a = job.xpath('./div/b/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./span//a/@href').extract_first()
      # These are the Glasgow jobs, so put that in
      c = 'Glasgow'
      # Exclude crap
      if a != None:
        job_list.append({'Company': 'Midsummer Energy',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Mimica(scrapy.Spider):
  name = "mimica"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.mimicalab.com/jointheteam']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.sqs-block-content > ul > li a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.mimicalab.com' + job.xpath('./@href').extract_first()
      # Get the locations
      c = 'London'
      job_list.append({'Company': 'Mimica', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Mixergy(scrapy.Spider):
  name = "mixergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.mixergy.co.uk/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.items > a'):
      # Get the job titles
      a = job.xpath('./div[2]/h3/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'Oxfordshire'
      job_list.append({'Company': 'Mixergy', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Modo_Energy(scrapy.Spider):
  name = "modoenergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://modoenergy.recruitee.com/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.sc-1543tgf-2'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://modoenergy.recruitee.com' + \
          job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath(
          ".//span[@class='custom-css-style-job-location-city']/text()").extract_first()
      job_list.append(
          {'Company': 'Modo Energy', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Mootral(scrapy.Spider):
  name = "mootral"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.mootral.com/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.w-full > a'):
      # Get the job titles
      a = job.xpath('./span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations and tidy them up
      c = job.xpath('./div/span[3]/text()').extract_first()
      if c == 'UK' or c == 'UK, Mootral Germany':
        c = 'Scotland'
      # Exclude crap
      if a != None:
        job_list.append({'Company': 'Mootral', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Natural_England(scrapy.Spider):
  name = "naturalengland"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.civilservicejobs.service.gov.uk/csr/index.cgi?SID=Y29udGV4dGlkPTMwMjU2NjQ4Jm93bmVydHlwZT1mYWlyJnBhZ2VhY3Rpb249c2VhcmNoY29udGV4dCZvd25lcj01MDcwMDAwJnBhZ2VjbGFzcz1TZWFyY2gmcmVxc2lnPTE2Nzk4NDA5NDMtN2E1NzJhM2ViMDAzYzNlNWUyZjI2ZjgzOTMyN2QwNzNhYTNjN2FkZQ==']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.search-results-job-box'):
      # Get the job titles
      a = job.xpath('./div[2]/a/text()').extract_first()
      # Get rid of the internal reference number included in the job title
      if 'Ref:' in a:
        a = a[:-11].strip()
      # Get the URLs for those jobs
      b = job.xpath('./div[2]/a/@href').extract_first()
      # Get the locations
      c = job.xpath('./div[4]/text()').extract_first().strip()
      if c == 'National':
        c = "London, South East, South West England, North East England, North West England, East Midlands, West Midlands, East of England, Yorkshire"
      job_list.append({'Company': 'Natural England',
                      'Job Title': a, 'Job URL': b, 'Location': c})

    # Get jobs from the next page of results
      next_page_text = response.css(
          'div.search-results-paging-menu').xpath('./ul/li[last()]/a/text()').extract_first()
      if next_page_text != None:
        next_page = response.css(
            'div.search-results-paging-menu').xpath('./ul/li[last()]/a/@href').extract_first()
        yield scrapy.Request(url=next_page, callback=self.parse)


# Create the Spider class
class Naturbeads(scrapy.Spider):
  name = "naturbeads"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.naturbeads.com/work-with-us']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('span[style="font-size:29px;"]'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # All job descriptions are on the same page
      b = 'https://www.naturbeads.com/work-with-us'
      # Get the locations
      # They all seem to be in Bath or Malmesbury (Wiltshire)
      c = 'South West England'
      job_list.append({'Company': 'Naturbeads', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Nature_North(scrapy.Spider):
  name = "naturenorth"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.naturenorth.org.uk/join-the-team/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.accordion-wrapper > h3 > button'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first().strip()
      # Get the URLs for those jobs
      b = 'https://www.naturenorth.org.uk/join-the-team/'
      # Get the locations
      c = 'Northern England'
      job_list.append({'Company': 'Nature North',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class NatureMetrics(scrapy.Spider):
  name = "naturemetrics"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://naturemetrics.breezy.hr/?&location=Guildford%2C%20GB#positions']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.position.transition > a'):
      # Get the job titles
      a = job.xpath('./h2/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://naturemetrics.breezy.hr' + \
          job.xpath('./@href').extract_first()
      # Get the locations
      c = job.xpath('./ul/li[1]/span/text()').extract_first()
      job_list.append({'Company': 'NatureMetrics',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Nautilus_Labs(scrapy.Spider):
  name = "nautiluslabs"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards-api.greenhouse.io/v1/boards/nautiluslabs/jobs/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['jobs']:
      # Get the job titles
      a = job['title']
      # All job descriptions are on the same URL
      b = job['absolute_url']
      # Get the locations
      c = job['location']['name']
      job_list.append({'Company': 'Nautilus Labs',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Normative(scrapy.Spider):
  name = "normative"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.normative.io/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.w-full > a'):
      # Get the job titles & tidy them up
      a = job.xpath('./span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c1 = job.xpath('./div/span/text()').extract()
      c2 = [s.strip() for s in c1]
      c = ", ".join(c2)
      if a != None:
        job_list.append(
            {'Company': 'Normative', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class North_Devon_Biosphere(scrapy.Spider):
  name = "northdevonbiosphere"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.northdevonbiosphere.org.uk/careers.html']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.accordion__title div.paragraph'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.northdevonbiosphere.org.uk/careers.html'
      # Get the locations
      c = 'North Devon'
      # Exclude crap
      if 'Get in touch' not in a:
        job_list.append({'Company': 'North Devon Biosphere',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class North_Wales_Rivers_Trust(scrapy.Spider):
  name = "northwalesriverstrust"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://northwalesriverstrust.org/job-vacancy']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.sqs-block-content > h2'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first().replace(".", "").strip()
      # Get the URLs for those jobs
      b = 'https://northwalesriverstrust.org/job-vacancy'
      # Get the locations
      c = 'North Wales'
      if 'Job Opportunities' not in a:
        job_list.append({'Company': 'North Wales Rivers Trust',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Notpla(scrapy.Spider):
  name = "notpla"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://notpla.jobs.personio.com/search.json']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data:
      # Get the job titles
      a = job['name']
      # Get the URLs for those jobs
      b = 'https://notpla.jobs.personio.com/job/' + str(job['id'])
      # Get locations
      c = job['office']
      job_list.append({'Company': 'Notpla', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Ocean_Bottle(scrapy.Spider):
  name = "oceanbottle"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://oceanbottle.co/pages/ocean-bottle-careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('ul.pf-87_ > li > span > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs (normally they don't include the full URL but sometimes they do)
      b1 = 'https://oceanbottle.co' + job.xpath('./@href').extract_first()
      if b1[:5] == 'https':
        b = job.xpath('./@href').extract_first()
      else:
        b = b1
      # Get the locations
      c = 'London'
      job_list.append({'Company': 'Ocean Bottle',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Ocean_Conservation_Trust(scrapy.Spider):
  name = "oceanconservationtrust"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://oceanconservationtrust.org/work-with-us/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.job-vacancy > h3 > a'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # Get the URLs for those jobs (have to remove first 2 characters of the scraped bit)
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = "Plymouth"
      job_list.append({'Company': 'Ocean Conservation Trust',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Octopus_Energy(scrapy.Spider):
  name = "octopusenergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://jobs.lever.co/octoenergy']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('a.posting-title'):
      # Get the job titles
      a = job.xpath('./h5/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c1 = job.xpath('./div/span[1]/text()').extract_first()
      if c1 == 'United Kingdom, Remote':
        c = 'Unknown'
      elif 'DigiOps' in c1:
        c = 'Fully Remote'
      elif c1 == 'Nationwide, UK':
        c = 'Darlington'
      else:
        c = c1
      # Exclude crap
      if not any(x in a for x in ["Can't find", "Octopus Internships"]):
        job_list.append({'Company': 'Octopus Energy',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Oddbox(scrapy.Spider):
  name = "oddbox"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.oddbox.co.uk/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.block-grid-item > a'):
      # Get the job titles
      a = job.xpath('./div[2]/span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the location. Bit awkward because sometimes location is the 3rd span and sometimes it's the 1st. Easiest to pull both then concatenate
      c1 = job.xpath('./div[2]/div/span[1]/text()').extract_first()
      c2 = job.xpath('./div[2]/div/span[3]/text()').extract_first()
      if c1 != None and c2 != None:
        c = c1.strip() + ", " + c2.strip()
        job_list.append({'Company': 'Oddbox', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Odyssey(scrapy.Spider):
  name = "odyssey"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://odysseyenergysolutions.com/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h5.entry-title > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'Fully Remote'
      job_list.append({'Company': 'Odyssey', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Olio(scrapy.Spider):
  name = "olio"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://olioex.com/join-our-team/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.wpb_wrapper > p > a'):
      # Get the job titles
      a1 = job.xpath('.//text()').extract()
      a = "".join(a1)
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'Fully Remote'
      # Exclude crap
      if not any(x in a for x in ['volunteering', 'Our Values']):
        job_list.append({'Company': 'Olio', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class On_Purpose(scrapy.Spider):
  name = "onpurpose"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://on-purpose.breezy.hr/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.position.transition > a'):
      # Get the job titles
      a = job.xpath('./h2/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://on-purpose.breezy.hr' + job.xpath('./@href').extract_first()
      # Get the locations
      c = job.xpath('./ul/li[1]/span/text()').extract_first()
      job_list.append({'Company': 'On Purpose', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create dictionaries to store job titles and job pages
job_list = []

job_desc_urls_oneclicklca = []
# Create the Spider class


class One_Click_LCA(scrapy.Spider):
  name = "oneclicklca"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.oneclicklca.com/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape links to individual job pages
  def parse(self, response):
    for job in response.css('li.w-full > a'):
      # Get the URLs for each job listed on the page
      url = job.xpath('./@href').extract_first()
      # Add those URLs to a (initially empty) list so we can use them in the next for loop
      job_desc_urls_oneclicklca.append(url)
    # Tell it to scrape the job description page for each job
    for job in job_desc_urls_oneclicklca:
      yield scrapy.Request(url=job, callback=self.parse_job_desc)

  # Second parsing method to scrape job titles and locations
  def parse_job_desc(self, response):
    # Get the job titles and make them title case as they're a mess to categorise otherwise
    a = response.css(
        'h1.font-company-header').xpath('./text()').extract_first().title()
    # Remove all the crap from the job titles
    a = a.replace(" For Sustainability Saas", "").replace(" For A Global Sustainability Scaleup", "").replace(
        " For Life-Cycle Assessment Scaleup", "").replace(", Sustainability Software", "").replace(" For A Sustainability Saas", "").replace("For Saas Carbon Scaleup In Construction", "").replace("For Saas Carbon Scaleup", "")
    # Get the locations. Bit funky here as have to select the element after the element that says 'Locations' and ignore everything else
    for ele in response.css('dt'):
      c1 = ele.xpath('./text()').extract_first()
      if c1 == 'Locations':
        c = ele.xpath('./following-sibling::dd/text()').extract_first().strip()
        # Occasionally this doesn't work and the locations are presented in a different way
        if c == "":
          c = ele.xpath(
              './following-sibling::dd/span/@title').extract_first().strip()
        # Tidy up locations
        if c != None:
          if any(x in c for x in ['Europe', 'United Kingdom']):
            c = 'Fully Remote'
        job_list.append({'Company': 'One Click LCA', 'Job Title': a,
                        'Job URL': response.url, 'Location': c})


# Create the Spider class
class Only_One(scrapy.Spider):
  name = "onlyone"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards-api.greenhouse.io/v1/boards/onlyone/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['jobs']:
      # Get the job titles
      a = job['title']
      # All job descriptions are on the same URL
      b = job['absolute_url']
      # Get the locations
      c = job['location']['name']
      job_list.append({'Company': 'Only One', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Open_Climate_Fix(scrapy.Spider):
  name = "openclimatefix"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://feed.homerun.co/openclimatefix']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  # Have to scrape an XML file for this one
  def parse(self, response):
    # If you don't include the namespace, you don't get any data
    response.selector.register_namespace('d', 'http://www.w3.org/2005/Atom')
    for job in response.xpath('.//d:entry'):
      # Get the job titles
      a = job.xpath('.//d:title/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('.//d:link/@href').extract_first()
      # Get the locations
      c = job.xpath('.//d:location//d:name/text()').extract_first()
      if 'Remote' in c:
        c = 'Fully Remote'
      job_list.append({'Company': 'Open Climate Fix',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Origen(scrapy.Spider):
  name = "origen"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://origencarbonsolutions.teamtailor.com/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li > a'):
      # Get the job titles
      a = job.xpath('./span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations. Check whether it's fully remote first
      c1 = job.xpath('./div/span[3]//text()').extract_first()
      # Exclude jobs without a location listed
      if c1 != None:
        if 'Fully Remote' in c1:
          c = 'Fully Remote'
        # If not remote, get the location, which can appear in a couple of different ways
        else:
          c2 = job.xpath('./div/span[1]/@title').extract_first()
          if c2 != None:
            c = c2
          else:
            c = job.xpath('./div/span[1]/text()').extract_first()
        job_list.append({'Company': 'Origen', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Otovo(scrapy.Spider):
  name = "otovo"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.otovo.com/positions']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('tr'):
      # Get the job titles
      a = job.xpath('./td[1]/a/text()').extract_first()
      # Easiest to exclude crap at this stage
      if a != None:
        # Get the URLs for those jobs
        b = 'https://careers.otovo.com' + \
            job.xpath('./td[1]/a/@href').extract_first()
        # Get the locations and tidy them up
        c1 = job.xpath('./td[3]//text()').extract()
        c = "".join(c1)
        job_list.append({'Company': 'Otovo', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class OVO_Energy(scrapy.Spider):
  name = "ovoenergy"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards-api.greenhouse.io/v1/boards/ovoenergy/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['jobs']:
      # Get the job titles
      a = job['title']
      # All job descriptions are on the same URL
      b = job['absolute_url']
      # Get the locations and tidy up what you can
      c1 = job['location']['name']
      if 'Any of our offices' in c1:
        c = 'London, Bristol, Glasgow'
      elif 'Field Based' in c1:
        c = 'Unknown'
      else:
        c = c1
      job_list.append({'Company': 'OVO Energy', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Patch(scrapy.Spider):
  name = "patch"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.patch.io/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.careers-collection-item > a'):
      # Get the job titles
      a = job.xpath(
          './/div[contains(@class,"job-listing-title")]//text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.patch.io' + job.xpath('./@href').extract_first()
      # Get the locations (need to combine two location divs)
      c1 = job.xpath(
          './/div[contains(@class,"job-listing-location")]/div/text()').extract()
      c = "".join(c1)
      # Looks like all UK jobs can be done fully remotely, but the extracted location will get mapped to 'London', so need to fix that, while also being careful not to stop the foreign jobs being excluded during categorisation
      if c == 'London [Remote]':
        c = 'Fully Remote'
      job_list.append({'Company': 'Patch', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class PECT(scrapy.Spider):
  name = "pect"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.pect.org.uk/about/work-for-us/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.job-listing-item > a'):
      # Get the job titles
      a = job.xpath('./div[1]/h3/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = job.xpath('./div[1]/div/span[2]/text()').extract_first()
      job_list.append({'Company': 'PECT', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Piclo(scrapy.Spider):
  name = "piclo"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards.greenhouse.io/piclo']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.opening'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://boards.greenhouse.io' + \
          job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./span/text()').extract_first()
      job_list.append({'Company': 'Piclo', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Planet_Mark(scrapy.Spider):
  name = "planetmark"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.planetmark.com/about-us/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.accordion_item_trigger > h5'):
      # Get the job titles and tidy up
      a = job.xpath('.//text()').extract_first().title().strip()
      # All the job descriptions are on the same page
      b = 'https://www.planetmark.com/about-us/careers/'
      # Get the locations
      c = 'London'
      job_list.append(
          {'Company': 'Planet Mark', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Planet_Patrol(scrapy.Spider):
  name = "planetpatrol"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://planetpatrol.co/vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.elementor-widget-wrap'):
      # Get the job titles
      a = job.xpath('.//h2//text()').extract_first()
      # Job descriptions are all pop-ups on the same page
      b = 'https://planetpatrol.co/vacancies/'
      # Get the locations
      c = job.xpath('./div/div/div/p[2]//text()').extract_first()
      # Scrap the crap
      if a != None:
        if not any(x in a for x in ['Vacancies', 'Volunteer', 'About Planet Patrol', 'Get the Report', 'Thank you for standing with us']):
          # Tidy up the job title so it doesn't start with 'JOB ROLE'
          a = a.replace("JOB ROLE: ", "").strip()
          job_list.append({'Company': 'Planet Patrol',
                          'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Proforest(scrapy.Spider):
  name = "proforest"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.proforest.net/who-we-are/join-our-team/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.record'):
      # Get the job titles and tidy up
      a = job.xpath('.//h3/a//text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.proforest.net' + \
          job.xpath('.//h3/a/@href').extract_first()
      # Get the locations and tidy up (a bit)
      c1 = job.xpath('.//div[contains(@class,"details")]//text()').extract()
      c = "".join(c1).strip()
      # Exclude non-UK jobs and force the locations into a tidy 'Oxford'
      if any(x in c for x in ['Oxford', 'UK']):
        c = 'Oxford'
        job_list.append(
            {'Company': 'Proforest', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Project_Seagrass(scrapy.Spider):
  name = "projectseagrass"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.projectseagrass.org/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.toggle'):
      # Get the job titles
      a = job.xpath('./h3//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./div//a/@href').extract_first()
      # Get the location
      c = 'Wales'
      job_list.append({'Company': 'Project Seagrass',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Provenance(scrapy.Spider):
  name = "provenance"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.provenance.org/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.flexjobads > div'):
      # Get the job titles
      a = job.xpath('./h4/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.provenance.org' + job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./div/div[1]/text()').extract_first()
      job_list.append({'Company': 'Provenance', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Pukka(scrapy.Spider):
  name = "pukka"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.pukkaherbs.com/uk/en/careers-at-pukka']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.current-vacancies-item-info'):
      # Get the job titles
      a = job.xpath('./h3/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.pukkaherbs.com' + job.xpath('./a/@href').extract_first()
      # Get locations
      c = 'Bristol'
      job_list.append({'Company': 'Pukka', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# This one is usefully funky
# Create the Spider class
class Quantifying_Nature(scrapy.Spider):
  name = "quantifyingnature"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://quantifyingnature.com/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.elementor-widget-wrap.elementor-element-populated'):
      # Get the job titles and tidy them up. This is super messy because sometimes there are 4 divs for each job, and sometimes there are 3. So first we just need to check if there are 3 or 4, then extract accordingly
      y = job.xpath('./div[4]//text()').extract()
      z = "".join(y).strip()
      if z == 'Learn more':
        a = job.xpath('./div[3]//text()').extract_first()
      else:
        a = job.xpath('./div[2]//text()').extract_first()
      # Get the URLs for those jobs
      if z == 'Learn more':
        b1 = job.xpath('./div[4]/div/a/@href').extract_first()
        b = 'https://quantifyingnature.com/careers' + str(b1)
      else:
        b1 = job.xpath('./div[3]/div/a/@href').extract_first()
        b = 'https://quantifyingnature.com/careers' + str(b1)
      # Get the locations
      c = job.xpath('./div[1]//text()').extract_first()
      # Exclude the crap (lots of it) and then tidy up the job titles
      if 'None' not in b:
        a = a.title().strip()
        job_list.append({'Company': 'Quantifying Nature',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Real_Wild_Estates(scrapy.Spider):
  name = "realwildestates"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.realwildestates.com/job-vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.col-inner.text-center.dark'):
      # Get the job titles and put into title case
      a = job.xpath('./div/h3//text()').extract_first().title()
      # Get the URLs for those jobs
      b = job.xpath('./a/@href').extract_first()
      # Get the locations
      c = 'Largely remote with some days in Bristol and Bath'
      job_list.append({'Company': 'Real Wild Estates',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Renewable_Exchange(scrapy.Spider):
  name = "renewableexchange"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://join.com/companies/renewable']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div#publicJobsList + div a'):
      # Get the job titles
      a = job.xpath('.//h3/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = job.xpath(
          './span/div/div/div[2]/div[2]/div[1]/text()').extract_first()
      job_list.append({'Company': 'Renewable Exchange',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Responsible_Steel(scrapy.Spider):
  name = "iucn"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.responsiblesteel.org/about/vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.section__content > p:nth-child(5n+2)'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # All the job descriptions need to be downloaded from the same page
      b = 'https://www.responsiblesteel.org/about/vacancies/'
      # Get the locations and change to Fully Remote where applicable
      c1 = job.xpath('./following-sibling::ul[1]/li[2]/text()').extract_first()
      if c1 != None and 'UK/Europe based' in c1:
        c = 'Fully Remote'
      # Exclude crap
      if not any(x in a for x in ['At ResponsibleSteel', 'Applications will be accepted']):
        job_list.append({'Company': 'Responsible Steel',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Rewilding_Britain(scrapy.Spider):
  name = "rewildingbritain"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.rewildingbritain.org.uk/about-us/current-jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    # Some jobs appear in h5 tags, others in h4 tags, so this is messy
    for job in response.css('div.center__sm.prose > h5'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # Too much of a pain to do anything but link to the careers page for job descriptions
      b = 'https://www.rewildingbritain.org.uk/about-us/current-jobs'
      # Get the locations
      c = 'Fully Remote'
      if a != None:
        if 'Other places to look' not in a:
          job_list.append({'Company': 'Rewilding Britain',
                          'Job Title': a, 'Job URL': b, 'Location': c})
    for job in response.css('div.center__sm.prose > h4'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # Too much of a pain to do anything but link to the careers page for job descriptions
      b = 'https://www.rewildingbritain.org.uk/about-us/current-jobs'
      # Get the locations
      c = 'Fully Remote'
      # Exclude crap
      if a != None:
        if 'Other places to look' not in a:
          job_list.append({'Company': 'Rewilding Britain',
                          'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Ripple(scrapy.Spider):
  name = "ripple"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.rippleenergy.com/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.w-full > a'):
      # Get the job titles and tidy up
      a = job.xpath('./span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations. First check if it's fully remote, then extract location if not
      c1 = job.xpath('./div/span[5]//text()').extract_first()
      if c1 != None:
        if 'Fully Remote' in c1:
          c = 'Fully Remote'
        else:
          c = job.xpath('./div/span[3]/text()').extract_first()
        job_list.append({'Company': 'Ripple', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Saietta(scrapy.Spider):
  name = "saietta"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.saietta.com/vacancies']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.c-card-vacancy > div'):
      # Get the job titles and tidy them up
      a = job.xpath('./h4/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./div/text()').extract_first()
      # A few jobs don't show location, so just put in both possible options
      if c == ', United Kingdom':
        c = 'Oxfordshire, Northamptonshire'
      job_list.append({'Company': 'Saietta', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Scotland_TBP(scrapy.Spider):
  name = "scotlandtbp"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.scotlandbigpicture.com/vacancies']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('article.clear-fix > p > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = "Scotland"
      job_list.append({'Company': 'Scotland: The Big Picture',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Scottish_Seabird_Centre(scrapy.Spider):
  name = "scottishseabirdcentre"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.seabird.org/vacancies']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.card__body'):
      # Get the job titles
      a = job.xpath('./h2/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.seabird.org' + job.xpath('.//a/@href').extract_first()
      # Get the locations
      c = "Scotland"
      job_list.append({'Company': 'Scottish Seabird Centre',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Secret_World_Wildlife_Rescue(scrapy.Spider):
  name = "secretworldwildliferescue"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.secretworld.org/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h5'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b = "https://www.secretworld.org/jobs"
      # Get the locations
      c = "Somerset"
      job_list.append({'Company': 'Secret World Wildlife Rescue',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Seismic(scrapy.Spider):
  name = "seismic"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.seismic-change.com/join-us/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.et_pb_text_inner > h3 > strong > a'):
      # Get the job titles and tidy them up
      a = job.xpath('./text()').extract_first().replace("→", "").strip()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'London'
      job_list.append({'Company': 'Seismic', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Small_Beer(scrapy.Spider):
  name = "smallbeer"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://theoriginalsmallbeer.com/pages/team']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div#s-535379c5-5f7a-4bc5-a765-ff74cff39d97 a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get locations
      c = 'London'
      job_list.append({'Company': 'Small Beer', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Smol(scrapy.Spider):
  name = "smol"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.smolproducts.com/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li > a'):
      # Get the job titles
      a = job.xpath('./span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations. Check whether it's fully remote first
      c1 = job.xpath('./div/span[3]//text()').extract_first()
      if c1 != None:
        if 'Fully Remote' in c1:
          c = 'Fully Remote'
        # If not remote, get the location, which can appear in a couple of different ways
        else:
          c2 = job.xpath('./div/span[1]/@title').extract_first()
          if c2 != None:
            c = c2
          else:
            c = job.xpath('./div/span[1]/text()').extract_first()
      else:
        c = job.xpath('./div/span[1]/text()').extract_first()
      # Exclude crap
      if a != None:
        job_list.append({'Company': 'smol', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Soil_Association(scrapy.Spider):
  name = "soilassocation"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://octoapi.blueoctopus.co.uk/api/GetVacancies?location=&keyword=&page=1&pageSize=100&orderBy=1&companyId=16913&managedbytype=0&locationSearchType=1&keywordsearchtype=1&salaryRangeId=-1&locationId=-1&jobTypeId=-1']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data:
      # Get the job titles
      a = job['VacancyTitle']
      # Get the URLs for those jobs
      b = 'https://jobs.soilassociation.org/vacancies/details?v=' + \
          str(job['Id'])
      # Get the locations
      c = job['AdvertisedLocation']
      job_list.append({'Company': 'Soil Association',
                      'Job Title': a, 'Job URL': b, 'Location': c})



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


# Create the Spider class
class South_Pole(scrapy.Spider):
  name = "southpole"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.southpole.com/jobs?country=United+Kingdom&query=']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.w-full > a'):
      # Get the job titles
      a = job.xpath('./span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations (looks like everything is in London with no fully remote jobs - only works because the URL is already filtering for London jobs only)
      c = 'London'
      job_list.append({'Company': 'South Pole', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Sunswap(scrapy.Spider):
  name = "sunswap"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.sunswap.co.uk/vacancies']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div[data-testid="mesh-container-content"]'):
      # Get the job titles
      a = job.xpath('./div[1]//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./div[4]/a/@href').extract_first()
      # Get the locations
      c = 'Leatherhead'
      if a != None:
        if not any(x in a for x in ['CAREERS', 'All Rights Reserved']):
          job_list.append(
              {'Company': 'Sunswap', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Surfers_Against_Sewage(scrapy.Spider):
  name = "surfersagainstsewage"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.sas.org.uk/job-opportunities/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.accordion-item > button > span.accordion-button-title'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # All job descriptions are on the same page
      b = 'https://www.sas.org.uk/job-opportunities/'
      # Get the locations
      c = 'Cornwall'
      job_list.append({'Company': 'Surfers Against Sewage',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Sustainable_Food_Trust(scrapy.Spider):
  name = "sustainablefoodtrust"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://sustainablefoodtrust.org/get-involved/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.item-grid__text > h3'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./following-sibling::*//a/@href').extract_first()
      # Get the locations
      c = 'Bristol'
      job_list.append({'Company': 'Sustainable Food Trust',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class SustainLife(scrapy.Spider):
  name = "sustainlife"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards.greenhouse.io/sustainlife']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.opening'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://boards.greenhouse.io' + \
          job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./span/text()').extract_first()
      job_list.append({'Company': 'Sustain.Life',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Sustrans(scrapy.Spider):
  name = "sustrans"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = [
        'https://www.sustrans.org.uk/job-vacancies/?location=null&jobvacancyrole=null']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.vacancy'):
      # Get the job titles (need to trim whitespace here)
      a = job.xpath('./p/a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.sustrans.org.uk' + \
          job.xpath('./p/a/@href').extract_first()
      # Get the location
      c = job.xpath('./ul/li[1]/text()').extract_first()
      if c == 'Location: Hybrid':
        c = 'Nearby Any Sustrans Office Hub Across The Uk'
      job_list.append({'Company': 'Sustrans', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Sylvera(scrapy.Spider):
  name = "sylvera"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://jobs.lever.co/sylvera']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('a.posting-title'):
      # Get the job titles
      a = job.xpath('./h5/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the location
      c = job.xpath('./div/span/text()').extract_first()
      if 'England' in c:
        job_list.append({'Company': 'Sylvera', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Tenzo(scrapy.Spider):
    name = "tenzo"
    custom_settings = {'DOWNLOAD_DELAY': 0.6}

    # start_requests method
    def start_requests(self):
      urls = ['https://careers.gotenzo.com/jobs']
      for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)

    # First parsing method to scrape job titles and links to individual job pages
    def parse(self, response):
      for job in response.css('li.block-grid-item > a'):
        # Get the job titles
        a = job.xpath('./div[2]/span/text()').extract_first()
        # Get the URLs for those jobs
        b = job.xpath('./@href').extract_first()
        # Get the locations
        c = job.xpath('./div[2]/div/span[3]/text()').extract_first()
        # Exclude unwanted results
        if 'North Carolina' not in c:
          if 'Join Our Talent Pool' not in a:
            job_list.append(
                {'Company': 'Tenzo', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Tepeo(scrapy.Spider):
  name = "tepeo"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://tepeo.com/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.accordion-item'):
      # Get the job titles
      a = job.xpath('./h2/button/span/text()').extract_first()
      if a != None:
        a = a.strip()
      # Get the URLs for those jobs
      b1 = job.xpath('.//a/@href').extract_first()
      # Exclude 'coming soon' jobs (need to do this here for simplicity)
      if b1 != None:
        b = 'https://tepeo.com' + b1
        # Get the locations
        c = 'Wokingham'
        job_list.append({'Company': 'Tepeo', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Tevva(scrapy.Spider):
  name = "tevva"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.smartrecruiters.com/Tevva']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.opening-job > a'):
      # Get the job titles
      a = job.xpath('./h4/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the location
      c = job.xpath('./ul/li[2]/text()').extract_first()
      job_list.append({'Company': 'Tevva', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class The_Two_Minute_Foundation(scrapy.Spider):
  name = "thetwominutefoundation"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.2minute.org/Job-opportunities']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('ul.navbar-nav > li:nth-child(4) > div > a'):
      # Get the job titles and make them title case
      a = job.xpath('./text()').extract_first()
      # Job descriptions are all on the same page
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'Bude, Cornwall'
      job_list.append({'Company': 'The 2 Minute Foundation',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class The_Barn_Owl_Trust(scrapy.Spider):
  name = "barnowltrust"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.barnowltrust.org.uk/about-the-barn-owl-trust/job-vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('section.entry > h3'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.barnowltrust.org.uk/about-the-barn-owl-trust/job-vacancies/'
      # Get the locations
      c = 'Devon'
      # Exclude crap
      if not any(x in a for x in ['Conservation Team', 'Volunteering']):
        job_list.append({'Company': 'The Barn Owl Trust',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class The_Carbon_Literacy_Project(scrapy.Spider):
  name = "thecarbonliteracyproject"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://carbonliteracy.com/work-with-us/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.accordion'):
      # Get the job titles
      a = job.xpath('./div/text()').extract_first().strip()
      # All job descriptions are on the same page
      b = 'https://carbonliteracy.com/work-with-us/'
      # Get the locations (looks like they offer Manchester or hybrid or remote)
      c = 'Fully Remote'
      # Exclude crap
      if 'no external opportunities' not in a:
        job_list.append({'Company': 'The Carbon Literacy Project',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# This one is usefully funky
# Create the Spider class
class The_Conservation_Volunteers(scrapy.Spider):
  name = "theconservationvolunteers"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www2.tcv.org.uk/cgi-bin/jobs/job_vacancies']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div#content > p.ad'):
      # Get the job titles
      a = job.xpath('./strong[1]/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www2.tcv.org.uk' + job.xpath('./a/@href').extract_first()
      # Get the locations (this one is a bit awkward and needs some serious tidying!)
      c1 = job.xpath('./text()').extract()
      c = c1[2].strip().replace("('", "").replace("',)", "")
      # Get rid of internal-only jobs
      if 'INTERNAL APPLICANTS ONLY' not in job.xpath('.//text()').extract():
        job_list.append({'Company': 'The Conservation Volunteers',
                        'Job Title': a, 'Job URL': b, 'Location': c})


job_desc_urls_felix = []
# Create the Spider class


class The_Felix_Project(scrapy.Spider):
  name = "thefelixproject"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://thefelixproject.org/work-for-us']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape links to individual job pages
  def parse(self, response):
    for job in response.css('li.job'):
      # Get the URLs for each job listed on the page
      url = job.xpath('./a/@href').extract_first()
      # Add those URLs to a (initially empty) list so we can use them in the next for loop
      job_desc_urls_felix.append(url)
    # Tell it to scrape the job description page for each job
    for job in job_desc_urls_felix:
      yield scrapy.Request(url=job, callback=self.parse_job_desc)

  # Second parsing method to scrape job titles and locations
  def parse_job_desc(self, response):
    # Get the job titles
    a = response.css('div.job-title').xpath('./text()').extract_first().strip()
    # Get the locations
    c1 = response.css('div.location').xpath('.//text()').extract()
    c = "".join(c1).strip()
    job_list.append({'Company': 'The Felix Project',
                    'Job Title': a, 'Job URL': response.url, 'Location': c})


# Create the Spider class
class The_National_Forest(scrapy.Spider):
  name = "nationalforest"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.nationalforest.org/about/who-we-are/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.content-block__content'):
      # Get the job titles
      a = job.xpath('./h3/text()').extract_first().strip()
      # Get the URLs for those jobs
      b = 'https://www.nationalforest.org' + \
          job.xpath('./a/@href').extract_first()
      # Get the location
      c = 'Leicestershire'
      job_list.append({'Company': 'The National Forest',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class The_Linnean_Society(scrapy.Spider):
  name = "thelinneansociety"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.linnean.org/the-society/vacancies-and-volunteering']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div > article > a'):
      # Get the job titles
      a = job.xpath('.//h2/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'London'
      # Exclude crap
      job_list.append({'Company': 'The Linnean Society',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class The_Tree_Council(scrapy.Spider):
  name = "thetreecouncil"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://treecouncil.org.uk/who-we-are/jobs/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h3'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b = "https://treecouncil.org.uk/who-we-are/jobs/"
      # Get the locations
      c = "London"
      # Exclude crap
      if not any(x in a for x in ["Follow us", "Contact us", "Tree Council Community"]):
        job_list.append({'Company': 'The Tree Council',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class The_Wildlife_Trusts(scrapy.Spider):
    name = "wildlifetrusts"
    custom_settings = {'DOWNLOAD_DELAY': 0.6}

    # start_requests method
    def start_requests(self):
      urls = ['https://www.wildlifetrusts.org/jobs?selector=.js-view-dom-id-3191fb5733493acdc9a466d5142fe3172d79edde9c3800c307d2a5ed3c7a8b30&contract=All&hours=All&type=All&location_distance=3&online=All&keywords=&location=&location_uuid=&reserve_uuid=&location_autocomplete=&page=0']
      for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)

    # First parsing method to scrape job titles and links to individual job pages
    def parse(self, response):
      for job in response.css('div.node__detail'):
        # Get the job titles
        a = job.xpath('./h2/a//text()').extract_first()
        # Get the URLs for those jobs
        b = job.xpath('./h2/a/@href').extract_first()
        # A few of the job roles don't include the full url so need to deal with those too
        if b[:8] != 'https://':
          b = 'https://www.wildlifetrusts.org' + b
        # Get the locations
        # Most job listings have e.g. 'Suffolk Wildlife Trust' in italics
        c = job.xpath('./div//em/text()').extract_first()
        # For the few that don't, we have to faff about joining together their multiple location fields and cleaning it all up
        if c == None:
          c1 = job.xpath(
              './/div[contains(@class,"field")]//span//text()').extract()
          c2 = "".join(c1)
          c3 = c2.replace("Closing date:", "")
          c = c3.strip()
        job_list.append({'Company': 'The Wildlife Trusts',
                        'Job Title': a, 'Job URL': b, 'Location': c})

      # Get jobs from the next page of results
      next_page = response.css('li.pager__item > a.button').xpath(
          './@href').extract_first()
      if next_page != None:
        yield scrapy.Request(url='https://www.wildlifetrusts.org/jobs'+next_page)


# Create the Spider class
class THIS(scrapy.Spider):
  name = "this"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://this.teamtailor.com/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li > a.focus-visible-company'):
      # Get the job titles
      a = job.xpath('./span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c1 = job.xpath('./div/span[3]/text()').extract_first()
      # That works most of the time, but some jobs don't have the department listed, so there's not always another span before the location span
      if c1 != None:
        c2 = c1
      else:
        c2 = job.xpath('./div/span[1]/text()').extract_first().strip()
      # Weird indentations and spaces sometimes
      c3 = c2.strip()
      # THIS office is in London
      if c3 == "THIS Office" or c3 == "Innovation":
        c = "London"
      else:
        c = c3
      job_list.append({'Company': 'THIS', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class TRAFFIC(scrapy.Spider):
  name = "traffic"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.traffic.org/about-us/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.card-body'):
      # Get the job titles
      a = job.xpath('./h5/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./div/p//a/@href').extract_first()
      # Get the locations
      c = job.xpath('./div/p//text()').extract_first()
      # Exclude crap
      if not any(x in a for x in ['TENDER NOTICE', 'Consultant']):
        job_list.append({'Company': 'TRAFFIC', 'Job Title': a,
                        'Job URL': b, 'Location': c})


'''

# Create the Spider class
class Tred(scrapy.Spider):
    name = "tred"
    custom_settings = {'DOWNLOAD_DELAY': 0.6}

    # start_requests method
    def start_requests(self):
      urls = ['https://tred.earth/climate-change-jobs/']
      for url in urls:
        yield scrapy.Request(url=url, callback=self.parse)

    #First parsing method to scrape job titles and links to individual job pages
    def parse(self, response):
      for job in response.css('article.vacancy-holder > div.vacancy-content-wrap'):
        #Get the job titles
        a = job.xpath('./h3/text()').extract_first()
        #Get the URLs for those jobs
        b = job.xpath('./a/@href').extract_first()
        #Get the locations
        c = job.xpath('.//div[@class="vacancy-location"]/text()').extract_first()
        job_list.append({'Company': 'Tred', 'Job Title': a, 'Job URL': b, 'Location': c})

'''

# Create the Spider class


class Trailstone(scrapy.Spider):
  name = "trailstone"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.trailstonegroup.com/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.job-list > div > a'):
      # Get the job titles
      a = job.xpath('./div/p//text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.trailstonegroup.com' + \
          job.xpath('./@href').extract_first()
      # Get the locations
      c = job.xpath('./div/div/div//text()').extract_first()
      job_list.append({'Company': 'Trailstone', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Tree_Aid(scrapy.Spider):
  name = "treeaid"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.treeaid.org/about/our-team/work-with-tree-aid/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.c-accordion__item'):
      # Get the job titles
      a = job.xpath('./button//text()').extract_first().strip()
      # All job descriptions are on the same page
      b = 'https://www.treeaid.org/about/our-team/work-with-tree-aid/#vacancies'
      # Get the locations (this one needs a bit of tidying!)
      c1 = job.xpath('./div/p[3]//text()').extract()
      c = "".join(c1)
      # Exclude non-UK jobs:
      if not any(x in a for x in ['(e)', '(ve)', 'Facilitateur', 'Burkina Faso', 'Ouagadougou', 'Tamale', 'Ghana']):
        job_list.append({'Company': 'Tree Aid', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Treeapp(scrapy.Spider):
  name = "treeapp"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.thetreeapp.org/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('ul.careers-list > li'):
      # Get the job titles
      a = job.xpath('./div/h6/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./div/p[1]//text()').extract_first()
      job_list.append({'Company': 'Treeapp', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Trees_For_Cities(scrapy.Spider):
  name = "treesforcities"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.treesforcities.org/about-us/vacancies']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.entry-list__entry'):
      # Get the job titles and tidy them up
      a = job.xpath('./div/a//text()').extract()
      a = "".join(a).strip()
      # Get the URLs for those jobs
      b = job.xpath('./div/a/@href').extract_first()
      # No consistent way to get locations
      c = "unknown"
      job_list.append({'Company': 'Trees for Cities',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Trees_For_Life(scrapy.Spider):
  name = "treesforlife"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://treesforlife.org.uk/about-us/work-with-us/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    # Some have the <strong> tag surrounding the link
    for job in response.css('div.col-12.col-lg-10 > p > strong > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'Scotland'
      if a != None:
        job_list.append({'Company': 'Trees for Life',
                        'Job Title': a, 'Job URL': b, 'Location': c})
    # Others have the <strong> tag inside the link
    for job in response.css('div.col-12.col-lg-10 > p > a'):
      # Get the job titles
      a = job.xpath('./strong/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'Scotland'
      if a != None:
        job_list.append({'Company': 'Trees for Life',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class TreeSisters(scrapy.Spider):
  name = "treesisters"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://treesisters.org/vacancies']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.row.no-gutters div.card-body'):
      # Get the job titles and tidy them up
      a = job.xpath('./h2//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('.//a/@href').extract_first()
      # Get the locations
      c = "Fully Remote"
      job_list.append(
          {'Company': 'TreeSisters', 'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Triodos(scrapy.Spider):
  name = "triodos"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.triodos.co.uk/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.atfos-vacancy__list-item > a'):
      # Get the job titles and tidy them up
      a = job.xpath('./div/h3/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = "Bristol"
      job_list.append({'Company': 'Triodos Bank',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Trove_Research(scrapy.Spider):
  name = "troveresearch"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://trove-research.com/careers/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.grve-post-item-inner'):
      # Get the job titles
      a = job.xpath('./div/h3/span[1]/text()').extract_first()
      # All job descriptions have the same URL
      b = job.xpath('./a/@href').extract_first()
      # Get locations
      c = job.xpath('./div/h3/span[2]/text()').extract_first()
      if c != "Bengaluru":
        job_list.append({'Company': 'Trove Research',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class UK100(scrapy.Spider):
  name = "uk100"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.uk100.org/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h3'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # All job descriptions are on the same page
      b = 'https://www.uk100.org/careers'
      # Get the locations
      c = "London"
      job_list.append({'Company': 'UK100', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class UNDO(scrapy.Spider):
  name = "undo"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://undo.bamboohr.com/jobs/embed2.php?version=1.0.0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.BambooHR-ATS-Jobs-Item'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https:'+job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./span/text()').extract_first().strip()
      job_list.append({'Company': 'UNDO', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Upcircle(scrapy.Spider):
  name = "upcircle"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://upcirclebeauty.com/pages/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('button > b > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first().title()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'London'
      job_list.append({'Company': 'Upcircle', 'Job Title': a,
                      'Job URL': b, 'Location': c})


'''

# Create the Spider class
class Uplift(scrapy.Spider):
  name = "uplift"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}
  
  # start_requests method
  def start_requests(self):
    urls = ['https://upliftuk.org/join-our-team/']
    for url in urls:
      yield scrapy.Request(url = url,
                        callback = self.parse)
    
  #First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.is-layout-flow.wp-block-column'):
      #Get the job titles
      a = job.xpath('./h5/text()').extract_first()
      #Get the URLs for those jobs
      b = job.xpath('.//a/@href').extract_first()
      #Get the locations
      c = 'London'
      #Exclude crap
      if a != None:
        job_list.append({'Company':'Uplift', 'Job Title':a, 'Job URL':b, 'Location':c})

'''

# Create the Spider class


class Vaayu(scrapy.Spider):
  name = "vaayu"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards-api.greenhouse.io/v1/boards/vaayutech/jobs/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages (API)
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['jobs']:
      # Get the job titles
      a = job['title']
      # All job descriptions are on the same URL
      b = 'https://www.vaayu.tech/careers'
      # Get the locations
      c = job['location']['name']
      # Remove French jobs
      if 'France' not in a:
        job_list.append({'Company': 'Vaayu', 'Job Title': a,
                        'Job URL': b, 'Location': c})


# Create the Spider class
class Veganuary(scrapy.Spider):
  name = "veganuary"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://veganuary.com/about/jobs/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('a.card__link'):
      # Get the job titles
      a1 = job.xpath('./div[1]//text()').extract()
      a = "".join(a1).strip().title()
      # Get the URLs for those jobs and remove all the messy stuff after the ?
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = "Fully Remote"
      job_list.append({'Company': 'Veganuary', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Volta_Trucks(scrapy.Spider):
  name = "volta"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://volta-trucks.breezy.hr/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.position.transition > a'):
      # Get the job titles
      a = job.xpath('./h2/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://volta-trucks.breezy.hr' + \
          job.xpath('./@href').extract_first()
      # Get the locations
      c = job.xpath('./ul/li[1]/span/text()').extract_first()
      unwanteds = ['Amsterdam', 'Berlin', 'Brussels', 'Cologne', 'Duesseldorf', 'Duisbourg', 'Essen', 'Hamburg', 'Lyon',
                   'Madrid', 'Milan', 'Netherlands', 'Paris', 'Rome', 'Rotterdam', 'Steyr', 'Stockholm', 'The Hague', 'Vienna', 'milan']
      if not any(x in c for x in unwanteds):
        if 'Arrival Employees' not in a:
          job_list.append({'Company': 'Volta Trucks',
                          'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Watershed(scrapy.Spider):
  name = "watershed"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://watershed.com/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('article.open-roles > div > ul > li > a'):
      # Get the job titles and put them in title case
      a = job.xpath('./span/text()').extract_first().title()
      # Get the URLs for those jobs
      b = 'https://watershed.com' + job.xpath('./@href').extract_first()
      # Get the locations
      c = job.xpath('./small/text()').extract_first()
      job_list.append({'Company': 'Watershed', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Waterwise(scrapy.Spider):
  name = "waterwise"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.waterwise.org.uk/vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h3 > a'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'Fully Remote'
      job_list.append({'Company': 'Waterwise', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Wessex_Rivers_Trust(scrapy.Spider):
  name = "wessexriverstrust"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.wessexrt.org.uk/vacancies.html']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('p.display-5'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://www.wessexrt.org.uk/vacancies.html'
      # Get the locations
      c = 'Salisbury'
      job_list.append({'Company': 'Wessex Rivers Trust',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Who_Gives_A_Crap(scrapy.Spider):
  name = "whogivesacrap"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://boards.greenhouse.io/whogivesacrap']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.opening'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https://boards.greenhouse.io' + \
          job.xpath('./a/@href').extract_first()
      # Get the locations
      c1 = job.xpath('./span/text()').extract_first()
      if any(x in c1 for x in ['London', 'England', 'United Kingdom']):
        c = 'Fully Remote'
        job_list.append({'Company': 'Who Gives A Crap',
                        'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Wholegrain_Digital(scrapy.Spider):
  name = "wholegrain"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.wholegraindigital.com/jobs/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.accordion__item > h3 > a'):
      # Get the job titles
      a = job.xpath('.//text()').extract_first().strip()
      # Get the URLs for those jobs
      b = 'https://www.wholegraindigital.com/jobs/' + \
          job.xpath('./@href').extract_first()[1:]
      # Get locations
      c = 'London'
      job_list.append({'Company': 'Wholegrain Digital',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Wild(scrapy.Spider):
  name = "wild"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.wearewild.com/pages/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.StyleSplit__text'):
      # Get the job titles
      a = job.xpath('./h4/text()').extract_first().strip()
      # Get the URLs for those jobs
      b = 'https://www.wearewild.com' + job.xpath('./a/@href').extract_first()
      # Get the locations
      c = 'London'
      job_list.append({'Company': 'Wild', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Wildwood_Trust(scrapy.Spider):
  name = "wildwoodtrust"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://wildwoodtrust.org/job-vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div.container-fluid > p > strong:contains("Job Title:")'):
      # Get the job titles
      a = job.xpath('./following-sibling::text()[1]').extract_first()
      # All job descriptions are on the same page
      b = 'https://wildwoodtrust.org/job-vacancies/'
      # Get the locations. Most are in Kent but some are in Devon
      c = 'Kent'
      if any(x in a for x in ['Devon', 'Ottery', 'Escot']):
        c = 'Devon'
      job_list.append({'Company': 'Wildwood Trust',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class Winnow(scrapy.Spider):
  name = "winnow"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://api.hubapi.com/hubdb/api/v2/tables/3410114/rows?portalId=650776&orderBy=order']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    data = json.loads(response.text)
    for job in data['objects']:
      # Get the job titles (and clean one of them up)
      a = job['values']['1']
      if 'AI sustainability scale up' in a:
        a = a.replace(" for AI sustainability scale up", "")
      # Get the URLs for those jobs
      b = job['values']['5']
      # Get the locations
      c = job['values']['3']
      job_list.append({'Company': 'Winnow', 'Job Title': a,
                      'Job URL': b, 'Location': c})


job_desc_urls_world_energy_council = []
# Create the Spider class


class World_Energy_Council(scrapy.Spider):
  name = "worldenergycouncil"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.worldenergy.org/about-us/careers']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape links to individual job pages
  def parse(self, response):
    for job in response.css('div.card-body h5 + p + a'):
      # Get the URLs for each job listed on the page
      url = job.xpath('./@href').extract_first()
      # Add those URLs to a (initially empty) list so we can use them in the next for loop
      job_desc_urls_world_energy_council.append(url)
    # Tell it to scrape the job description page for each job
    for job in job_desc_urls_world_energy_council:
      yield scrapy.Request(url=job, callback=self.parse_job_desc)

  # Second parsing method to scrape job titles and locations
  def parse_job_desc(self, response):
    # Get the job titles
    a = response.css('h1').xpath('./text()').extract_first()
    # Get the locations
    c = response.css('h2 > span:contains("Location")').xpath(
        './following-sibling::text()[1]').extract()[0]
    job_list.append({'Company': 'World Energy Council',
                    'Job Title': a, 'Job URL': response.url, 'Location': c})


# Create the Spider class
class World_Land_Trust(scrapy.Spider):
  name = "worldlandtrust"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.worldlandtrust.org/who-we-are-2/vacancies/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('h3'):
      # Get the job titles
      a = job.xpath('./text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./following-sibling::p//a/@href').extract_first()
      # Get the locations
      c = 'Suffolk'
      job_list.append({'Company': 'World Land Trust',
                      'Job Title': a, 'Job URL': b, 'Location': c})


# Create the Spider class
class WWF(scrapy.Spider):
  name = "wwf"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://ce0449li.webitrent.com/ce0449li_webrecruitment/wrd/run/ETREC106GF.display_srch_all?WVID=5223411NZL']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('table.sect_header'):
      # Get the job titles
      a = job.xpath('./tr[2]/td/h2/a/text()').extract_first()
      # No idea why but the links to the job descriptions only work if you click from the page with all the jobs on it, so I'm just linking that
      b = 'https://ce0449li.webitrent.com/ce0449li_webrecruitment/wrd/run/ETREC106GF.display_srch_all?WVID=5223411NZL'
      # Get the locations
      c = job.xpath('./tr[5]/td/dl/div[1]/dd/text()').extract_first()
      job_list.append({'Company': 'WWF', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Yum_Bug(scrapy.Spider):
  name = "yumbug"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://www.yumbug.com/jobs']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('div[role=listitem]'):
      # Get the job titles
      a = job.xpath('.//h4//text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('.//a/@href').extract_first()
      # Get the locations
      c = 'London'
      job_list.append({'Company': 'Yum Bug', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Zedify(scrapy.Spider):
  name = "zedify"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://careers.zedify.co.uk/']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.w-full > a'):
      # Get the job titles
      a = job.xpath('./span/text()').extract_first()
      # Get the URLs for those jobs
      b = job.xpath('./@href').extract_first()
      # Get the locations
      c = 'Unknown'
      if 'London' in a:
        c = 'London'
      elif 'Edinburgh' in a:
        c = 'Edinburgh'
      elif 'Manchester' in a:
        c = 'Manchester'
      elif 'Birmingham' in a:
        c = 'Birmingham'
      elif 'Nottingham' in a:
        c = 'Nottingham'
      job_list.append({'Company': 'Zedify', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Create the Spider class
class Zenobe(scrapy.Spider):
  name = "zenobe"
  custom_settings = {'DOWNLOAD_DELAY': 0.6}

  # start_requests method
  def start_requests(self):
    urls = ['https://zenobe.bamboohr.com/jobs/embed2.php?version=1.0.0']
    for url in urls:
      yield scrapy.Request(url=url,
                           callback=self.parse)

  # First parsing method to scrape job titles and links to individual job pages
  def parse(self, response):
    for job in response.css('li.BambooHR-ATS-Jobs-Item'):
      # Get the job titles
      a = job.xpath('./a/text()').extract_first()
      # Get the URLs for those jobs
      b = 'https:'+job.xpath('./a/@href').extract_first()
      # Get the locations
      c = job.xpath('./span/text()').extract_first().strip()
      job_list.append({'Company': 'Zenobe', 'Job Title': a,
                      'Job URL': b, 'Location': c})


# Run the Spider
process = CrawlerProcess()
# LinkedIn orgs
process.crawl(Anibles)
process.crawl(Business_For_Nature)
process.crawl(Clean_Growth_Fund)
process.crawl(Climate_Outreach)
process.crawl(Daily_Dose_Juice)
process.crawl(Deep_Meta)
process.crawl(Denton_Park_Estate)
process.crawl(Echion_Technologies)
process.crawl(Ewhurst_Park)
process.crawl(Giant_Ventures)
process.crawl(Giki)
process.crawl(HCV_Network)
process.crawl(Initiative_Earth)
process.crawl(Just_Stop_Oil)
process.crawl(Kita)
process.crawl(Mana_Biosystems)
process.crawl(Materiom)
process.crawl(Measurable_Energy)
process.crawl(Meatless_Farm)
process.crawl(MyCarbon)
process.crawl(Natcap_Research)
process.crawl(Newcleo)
process.crawl(Noughts_Ones)
process.crawl(On_The_Edge)
process.crawl(Population_Matters)
process.crawl(Safe_Solvents)
process.crawl(Space_Intelligence)
process.crawl(Switch_It_Green)
process.crawl(Tangle)
process.crawl(Tenzing_Natural_Energy)
process.crawl(Too_Good_To_Go)
process.crawl(Treedom)
process.crawl(Trust_For_Sustainable_Living)
process.crawl(Wildlife_And_Countryside_Link)
process.crawl(Wrap)
process.crawl(Zevero)
# Workable ATS orgs
process.crawl(Again)
process.crawl(AimHi_Earth)
process.crawl(Breathe_Battery_Technologies)
process.crawl(Brilliant_Planet)
process.crawl(Carbon_Re)
process.crawl(Climate_Arc)
process.crawl(Climate_Bonds_Initiative)
process.crawl(Dendra)
process.crawl(FareShare)
process.crawl(Global_OTEC)
process.crawl(Hived)
process.crawl(Lick)
process.crawl(Make_My_House_Green)
process.crawl(Onto)
process.crawl(Oxwash)
process.crawl(Pangaia)
process.crawl(Pawprint)
process.crawl(Recycleye)
process.crawl(So_Energy)
process.crawl(Tesseract)
process.crawl(The_Modern_Milkman)
process.crawl(Tokamak_Energy)
process.crawl(Wallbox)
process.crawl(Wildlife_Works)
process.crawl(Zoomo)
process.crawl(Zulu_Forest_Sciences)
# All other orgs
process.crawl(Three_Fifty_Org)
process.crawl(Abel_Cole)
process.crawl(Agile_Charging)
process.crawl(Airly)
process.crawl(Allplants)
process.crawl(Altruistiq)
process.crawl(Amphibian_Reptile_Conservation)
process.crawl(Arrival)
process.crawl(Aura_Power)
process.crawl(Avon_Needs_Trees)
process.crawl(B_Lab_UK)
process.crawl(Ballard_Motive_Solutions)
process.crawl(Bat_Conservation_Trust)
process.crawl(Baukjen)
process.crawl(Beaver_Trust)
process.crawl(BeZero)
process.crawl(Bike_Club)
process.crawl(Biophilica)
process.crawl(Biorecro)
process.crawl(Birdlife)
process.crawl(Blue_Marine_Foundation)
process.crawl(Blue_Ventures)
process.crawl(Bonsucro)
process.crawl(Born_Free_Foundation)
process.crawl(British_Ecological_Society)
process.crawl(Bulb)
process.crawl(Butterfly_Conservation)
process.crawl(Byway)
process.crawl(CABI)
process.crawl(Cairngorms_National_Park)
process.crawl(Carbon_Chain)
process.crawl(CAT)
process.crawl(Cenex)
process.crawl(Centre_Climate_Engagement)
process.crawl(Centre_Sustainable_Energy)
process.crawl(Cervest)
process.crawl(Changeworks)
process.crawl(Chargy)
process.crawl(Circa5000)
process.crawl(City_Of_Trees)
process.crawl(Clean_Air_Fund)
process.crawl(Climate_Change_Committee)
process.crawl(Climate_Connect_Digital)
process.crawl(Climate_Impact_Partners)
process.crawl(Climate_Policy_Radar)
process.crawl(ClimateX)
process.crawl(Cogo)
process.crawl(Common_Seas)
process.crawl(Cultivate_London)
process.crawl(Decent_Packaging)
process.crawl(Delphis)
process.crawl(Dizzie)
process.crawl(Dulas)
process.crawl(Earth_Trust)
process.crawl(Earthly)
process.crawl(Earthwatch)
process.crawl(EcoACTIVE)
process.crawl(Ecologi)
process.crawl(Ecosia)
process.crawl(Ecosulis)
process.crawl(Eden_Rivers_Trust)
process.crawl(Ember)
process.crawl(Emitwise)
process.crawl(Energy_Climate_Intelligence_Unit)
process.crawl(Enviral)
process.crawl(Environment_Agency)
process.crawl(Environmental_Defense_Fund)
process.crawl(EIA)
process.crawl(Equilibrium_Energy)
process.crawl(EVenergy)
process.crawl(Fidra)
process.crawl(Finance_Earth)
process.crawl(Finisterre)
process.crawl(First_Mile)
process.crawl(Forest_Of_Marston_Vale)
process.crawl(Freshwater_Biological_Association)
process.crawl(Friends_Earth)
process.crawl(Futerra)
process.crawl(Galapagos_Conservation_Trust)
process.crawl(Global_Witness)
process.crawl(Granular)
process.crawl(Green_Alliance)
process.crawl(Greenpeace)
process.crawl(Ground_Control)
process.crawl(Guru_Systems)
process.crawl(Heal_Rewilding)
process.crawl(Heart_Of_England_Forest)
process.crawl(Heura)
process.crawl(Higher_Steaks)
process.crawl(Highview_Power)
process.crawl(Hubbub)
process.crawl(IIGCC)
process.crawl(Inclusive_Energy)
process.crawl(Innocent)
process.crawl(Kaluza)
process.crawl(Keep_Britain_Tidy)
process.crawl(KeepCup)
process.crawl(Keep_Scotland_Beautiful)
process.crawl(Knepp_Wildland_Foundation)
process.crawl(Leanpath)
process.crawl(Lime)
process.crawl(Living_Streets)
process.crawl(Low_Carbon)
process.crawl(Lucy_Yak)
process.crawl(Lunar_Energy)
process.crawl(Lune)
process.crawl(Manufacture_2030)
process.crawl(Matter)
process.crawl(Midsummer_Energy)
process.crawl(Mimica)
process.crawl(Mixergy)
process.crawl(Modo_Energy)
process.crawl(Mootral)
process.crawl(Natural_England)
process.crawl(Naturbeads)
process.crawl(Nature_North)
process.crawl(NatureMetrics)
process.crawl(Nautilus_Labs)
process.crawl(Normative)
process.crawl(North_Devon_Biosphere)
process.crawl(North_Wales_Rivers_Trust)
process.crawl(Notpla)
process.crawl(Ocean_Bottle)
process.crawl(Ocean_Conservation_Trust)
process.crawl(Octopus_Energy)
process.crawl(Oddbox)
process.crawl(Odyssey)
process.crawl(Olio)
process.crawl(On_Purpose)
process.crawl(One_Click_LCA)
process.crawl(Only_One)
process.crawl(Open_Climate_Fix)
process.crawl(Origen)
process.crawl(Otovo)
process.crawl(OVO_Energy)
process.crawl(Patch)
process.crawl(PECT)
process.crawl(Piclo)
process.crawl(Planet_Mark)
process.crawl(Planet_Patrol)
process.crawl(Proforest)
process.crawl(Project_Seagrass)
process.crawl(Provenance)
process.crawl(Pukka)
process.crawl(Quantifying_Nature)
process.crawl(Real_Wild_Estates)
process.crawl(Renewable_Exchange)
process.crawl(Responsible_Steel)
process.crawl(Rewilding_Britain)
process.crawl(Ripple)
process.crawl(Saietta)
process.crawl(Scotland_TBP)
process.crawl(Scottish_Seabird_Centre)
process.crawl(Secret_World_Wildlife_Rescue)
process.crawl(Seismic)
process.crawl(Small_Beer)
process.crawl(Smol)
process.crawl(Soil_Association)
process.crawl(Sourceful)
process.crawl(South_Pole)
process.crawl(Sunswap)
process.crawl(Surfers_Against_Sewage)
process.crawl(Sustainable_Food_Trust)
process.crawl(SustainLife)
process.crawl(Sustrans)
process.crawl(Sylvera)
process.crawl(Tenzo)
process.crawl(Tepeo)
process.crawl(Tevva)
process.crawl(The_Two_Minute_Foundation)
process.crawl(The_Barn_Owl_Trust)
process.crawl(The_Carbon_Literacy_Project)
process.crawl(The_Conservation_Volunteers)
process.crawl(The_Felix_Project)
process.crawl(The_Linnean_Society)
process.crawl(The_National_Forest)
process.crawl(The_Tree_Council)
process.crawl(The_Wildlife_Trusts)
process.crawl(THIS)
process.crawl(TRAFFIC)
process.crawl(Trailstone)
process.crawl(Tree_Aid)
process.crawl(Treeapp)
process.crawl(Trees_For_Cities)
process.crawl(Trees_For_Life)
process.crawl(Triodos)
process.crawl(Trove_Research)
process.crawl(UK100)
process.crawl(UNDO)
process.crawl(Upcircle)
process.crawl(Vaayu)
process.crawl(Veganuary)
process.crawl(Volta_Trucks)
process.crawl(Watershed)
process.crawl(Waterwise)
process.crawl(Who_Gives_A_Crap)
process.crawl(Wessex_Rivers_Trust)
process.crawl(Wholegrain_Digital)
process.crawl(Wild)
process.crawl(Wildwood_Trust)
process.crawl(Winnow)
process.crawl(World_Energy_Council)
process.crawl(World_Land_Trust)
process.crawl(WWF)
process.crawl(Yum_Bug)
process.crawl(Zedify)
process.crawl(Zenobe)
process.start()


# Import another package so we can export scraped jobs to a csv file

# Create a list for the column headers
field_names = ['Company', 'Job Title', 'Job URL', 'Location']

# Write to csv file
with open('scraped_jobs.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(job_list)
