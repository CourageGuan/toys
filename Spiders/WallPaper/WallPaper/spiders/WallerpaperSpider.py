import scrapy
from WallPaper.items import WallpaperItem
from scrapy.crawler import CrawlerProcess

class WallpaperSpider(scrapy.Spider):

	name ='Wallpaper' #爬虫名

	allowed_domains = ["simpledesktops.com","static.simpledesktops.com"]
	start_urls = ["http://simpledesktops.com/browse/desktops/2011/jul/14/cassette/"]

	def parse(self, response):

		host = u"http://simpledesktops.com"
		item = WallpaperItem()

		#item['title'] = response.xpath('//div[@class="desktop"]//img//@title').extract()
		download = response.xpath('//div[@class="desktop"]//h2//@href').extract()
		if len(download) > 0:
			download[0] = host + download[0]

		item['image_urls'] = download

		yield item

		next_url = host + response.xpath('//a[@class="forward"]//@href').extract_first()

		if next_url:
			yield  scrapy.Request(next_url,callback=self.parse)
