# -*- coding: utf-8 -*-
import scrapy

class WallpaperItem(scrapy.Item):
	title = scrapy.Field()
	image_urls = scrapy.Field()
