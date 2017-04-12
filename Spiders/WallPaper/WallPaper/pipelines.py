# -*- coding: utf-8 -*-
import urllib,os
from WallPaper import settings

class WallpaperPipeline(object):

	def process_item(self, item, spider):

		store_path = '%s/%s'%(settings.IMAGES_STORE,spider.name)
		if not os.path.exists(store_path):
			os.makedirs(store_path)

		for image_url in item['image_urls']:

			url_name = image_url.split('=')
			file_name = url_name[-1] + '.png'
			file_path = '%s/%s'%(store_path,file_name)

			if os.path.exists(file_path):
				continue

			with open(file_path,'wb') as file_writer:
				conn = urllib.urlopen(image_url)
				file_writer.write(conn.read())
				file_writer.close()

		return item
