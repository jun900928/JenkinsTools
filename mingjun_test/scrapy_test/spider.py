# -*- coding:utf-8 -*-

import urllib
import urllib2
import re


class Spider:
	def __init__(self):
		self.URL="http://www.artist.cn/snakewu1994/StyleBasis_Four/en_album_607236.shtml"

	def getPage(self,offset):
		url=self.URL+""+str(offset)
		print url
		request=urllib2.Request(url)
		response=urllib2.urlopen(request)
		with open("html","w") as f:
			f.write(response.read())
		return response.read()


	def getContents(self,offset):
		page=self.getPage(offset)
		pattern=re.compile('<div class="u-cover u-cover-1"><img class.*?><a title="(.*?)" href="(.*?)" .*?></a>.*?<span class="nb">(.*?)</span>')
		items = re.findall(pattern,page)
		for item in items:
			print item[0],item[1],item[2]


spider=Spider()
spider.getContents("")
