import scrapy

class SynonymScraperItem(scrapy.Item):
 	# Define the fields of the items 
 	# To be called by the spiders
 	# link = scrapy.Field()

 	url = scrapy.Field()
 	title = scrapy.Field()
 	description = scrapy.Field()
 	keywords = scrapy.Field()

	# pass