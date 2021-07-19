import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re

class HitoSpider(CrawlSpider):
    name = "hito"
    def start_requests(self):
        url = 'https://vi.wikipedia.org/wiki/Vi%E1%BB%87t_Nam'
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        if response.status == 200:
            #ten quoc gia 
            tenQuocGia = response.xpath("//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[1]/th/div/span//text()").getall()
            stringText = ""
            for text in tenQuocGia:
                text.replace("\n", "")
                stringText += re.sub('(\[\d+\])', " ", text)
                stringText = re.sub('(\s+){2}', " ", stringText)

            #tieu ngu
            for i in range(6):
                path="//*[@id='mw-content-text']/div[1]/table[1]/tbody/tr[4]/td/div//text()"
                tieuNgu = response.xpath(path).getall()
                stringText=""
                for text in tieuNgu:
                    text.replace("\n", "")
                    stringText += re.sub('(\[\d+\])', " ", text)
                    stringText = re.sub('(\s+){2}', " ", stringText)
                    print

