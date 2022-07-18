import scrapy
from dateutil.parser import parse

class GizmodoSpider(scrapy.Spider):
    name = 'gizmodo'
    start_urls = ['https://es.gizmodo.com/']

    def parse(self, response):
        find_rss = response.xpath("/html/head/link[32]/@href").extract_first()
        
        gizmodo_rss = response.urljoin(find_rss)

        if gizmodo_rss: 
            yield scrapy.Request(gizmodo_rss)

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



# ---------- test only ----------

# from scrapy.crawler import CrawlerProcess
# process = CrawlerProcess(settings={
#     "FEEDS": {
#         "gizmodo_data.json": {"format": "json"},
#     },
# })

# process.crawl(GizmodoSpider)
# process.start()