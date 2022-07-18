import scrapy
from dateutil.parser import parse

class PhoronixSpider(scrapy.Spider):
    name = 'phoronix'
    start_urls = ['https://www.phoronix.com/']

    def parse(self, response):
        find_rss = response.xpath("/html/body/div[2]/div/div/div/a[1]/@href").extract_first()
        
        phoronix_rss = response.urljoin(find_rss)

        if phoronix_rss: 
            yield scrapy.Request(phoronix_rss)

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
#         "phoronix_data.json": {"format": "json"},
#     },
# })

# process.crawl(PhoronixSpider)
# process.start()