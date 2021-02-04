import scrapy
from scrapy.http import Request,Response
from ..items import TutorialItem
from urllib.parse import urljoin


class DemoWallSpider(scrapy.Spider):
    name = 'demo_wall'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['https://wallhaven.cc/toplist?page=1']

    def img_data_parse(self, response):
        img_data = response.content
        item = TutorialItem()
        item['img_url'] = img_data
        yield item

    def img_parse(self, response):
        img_url = response.css("#wallpaper::attr(src)").get()
        item = TutorialItem()
        item['img_url'] = img_url
        yield item

        # yield scrapy.Request(url=img_url, callback=self.img_data_parse)



    def parse(self, response):
        # detail now page
        lis = response.css('section > ul > li')
        for li in lis:
            img_page = li.css('figure > a::attr(href)').get()
            yield scrapy.Request(url=img_page, callback=self.img_parse)

        # flip over
        now_url = response.request.url
        page = int(now_url.split("=")[-1])
        if page < 10:
            page += 1
            page_url = '?page=%d' % page
            next_page = urljoin(self.start_urls[0].split('?')[0], page_url)
            yield scrapy.Request(url=next_page, callback=self.parse)
