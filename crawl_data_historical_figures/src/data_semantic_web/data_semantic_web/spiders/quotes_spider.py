import scrapy
from scrapy.settings import Settings
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule, CrawlSpider
from urllib import parse

import re


class QuotesItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    tag = scrapy.Field()


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    params = []
    # def __init__(self):
    #     f = open("./nhanvat/nhanvatlist.txt", "r")
    #     for item in f:
    #         self.params.append(item.replace(
    #             " ", "_").replace("\n", "").strip())
    #     f.close()

    def start_requests(self):

        f = open("./nhanvat/nhanvatlist.txt", "r")
        for item in f:
            self.params.append(item.replace(
                " ", "_").replace("\n", "").strip())
        f.close()

        # print(self.params)

        url = 'https://vi.wikipedia.org/wiki/'
        for param in self.params:
            u = url + parse.quote(param.encode('utf-8'))
            yield scrapy.Request(u, self.parse, cb_kwargs={"filename": param})

    def parse(self, response, filename):
        if response.status == 200:
            information = response.xpath(
                "//div[@class='mw-parser-output']/p//text()").getall()
            stringText = ""
            for text in information:
                text.replace("\n", "")
                stringText += re.sub('(\[\d+\])', " ", text).strip() + " "
                # stringText.strip()
                stringText = re.sub('(\s+){2}', " ", stringText)
            stringText.strip()
            wirteFile(filename, stringText)


def wirteFile(filename, text):
    fs = open("./data/"+filename+".txt", "a")
    fs.write(text)
    fs.close()


def get_settings():
    settings = Settings()
    return settings


if __name__ == '__main__':
    settings = get_settings()
    runner = CrawlerRunner(settings)
    d = runner.crawl(QuotesSpider)
    d.addBoth(lambda _: reactor.stop())
    reactor.run()
