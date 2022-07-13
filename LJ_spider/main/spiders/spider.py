import scrapy

from test2.items import LJ_Item

class Myspider(scrapy.spiders.Spider):
    name = "lianjia"
    allowed_domains = ["bj.lianjia.com/ershoufang/"]

    place= input('请输入你要查询的区域:')
    for j in range(1,3):
        start_urls = [f"https://bj.lianjia.com/ershoufang/pg{j}rs{place}/"]

        def parse(self, response):
            item = LJ_Item()
            for i in range(1, 31):
                item['name'] = response.xpath(f'//*[@id="content"]/div[1]/ul/li[{i}]/div[1]/div[1]/a/text()').extract()
                item['discribe'] = response.xpath(f'//*[@id="content"]/div[1]/ul/li[{i}]/div[1]/div[3]/div/text()').extract()
                item['price'] = response.xpath(f'//*[@id="content"]/div[1]/ul/li[{i}]/div[1]/div[6]/div[1]/span/text()').extract()
                item['uprice'] = response.xpath(f'//*[@id="content"]/div[1]/ul/li[{i}]/div[1]/div[6]/div[2]/span/text()').extract()
                if item['name'] and item['discribe'] and item['price'] and item['uprice']:
                    print(item['name']+item['discribe']+item['price']+item['uprice'])
                    yield(item)




