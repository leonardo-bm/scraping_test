import scrapy
from dateutil.parser import parse

class EngadgetSpider(scrapy.Spider):
    name = 'engadget'
    start_urls = ['https://www.engadget.com/']

    def parse(self, response):
        find_rss = response.xpath("/html/head/link[1]/@href").extract_first()
        
        engadget_rss = response.urljoin(find_rss)

        if engadget_rss: 
            yield scrapy.Request(engadget_rss)

            response.selector.remove_namespaces()

            items = response.xpath('//rss/channel/item')[:10]
            for item in items:
                Title = item.xpath('.//title/text()').get()

                Pub = item.xpath('.//pubDate/text()').get()
                Published = parse(Pub, fuzzy=True)

                Link = item.xpath('.//link/text()').get()
                yield {'Text': Title,
                        'Published': Published,
                        'Link': Link}



# # ---------- test only ----------

# from scrapy.crawler import CrawlerProcess
# process = CrawlerProcess(settings={
#     "FEEDS": {
#         "engadget_data.json": {"format": "json"}
#     }
# })

# process.crawl(EngadgetSpider)
# process.start()