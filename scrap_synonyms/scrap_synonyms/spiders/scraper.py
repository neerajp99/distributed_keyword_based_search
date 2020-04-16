import scrapy 
from ..items import SynonymScraperItem 
import json 
from pathlib import Path

class SynonymScraper(scrapy.Spider):
	name = "synonym_scraper"
	# start_urls = ["https://moz.com/top500"] 

	# Open fetched json file 
	path = Path('/Users/neeraj/Desktop/distributed_keyword_based_search/scrap_synonyms/scrap_synonyms/links.json')

	with open(path) as f:
		data = json.loads(f.read())
		# print(data[0]['link'])
	data[0]['link'] = data[0]['link'][58:]

	start_urls = data[0]['link']

	# Method to handle the response downloaded for each of the request made
	def parse(self, response):
		# Scrapy item container instance
		items = SynonymScraperItem()

		# HREF_SELECTOR = 'a ::attr(href)'
		# links = response.css(HREF_SELECTOR).extract()

		# Scraping meta content
		title = response.css("title::text").extract_first() if response.css("title::text").extract_first() else ""
		if response.xpath("//meta[@name='keywords']/@content"):
			keywords = response.xpath("//meta[@name='keywords']/@content").extract_first()
		else:
			keywords = ""
		description = response.xpath("//meta[@name='description']/@content").extract_first() if response.xpath("//meta[@name='description']/@content").extract_first() else ""
		url = response.request.url

		# Adding to the scrapy container item
		# items['link'] = links
		# yield items

		# add to the scrapy container item
		items['url'] = url 
		items['keywords'] = keywords 
		items['description'] = description 
		items['title'] = title 

		yield {
			# items
			"url": url,
			"title": title,
			"keywords": keywords,
			"description": description,

		}
