import scrapy 

class SynonymScraper(scrapy.Spider):
	name = "synonym_scraper"
	start_urls = ["https://www.thesaurus.com/browse/list/2"] 

	# Method to handle the response downloaded for each of the request made
	def parse(self, response):
		title = response.css('div.css-10cokgy h3::text').extract_first()
		yield {"titletext" : title}
