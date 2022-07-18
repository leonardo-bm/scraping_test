import scrapy
from dateutil.parser import parse

class TheVergeSpider(scrapy.Spider):
    
    name = 'theverge'
    start_urls = ['https://www.theverge.com/']

    def parse(self, response):
        find_rss = response.xpath("/html/head/link[26]/@href").extract_first()
   
        theverge_rss = response.urljoin(find_rss)

        if theverge_rss:
            yield scrapy.Request(theverge_rss)

            response.selector.remove_namespaces()

            entries = response.xpath('//feed/entry')[:10]
            for entry in entries:
                Title = entry.xpath('.//title/text()').get()

                Pub = entry.xpath('.//published/text()').get()
                Published = parse(Pub, fuzzy=True)

                Link = entry.xpath('.//link/@href').get()
                yield {'Text': Title,
                        'Published': Published,
                        'Link': Link}



# ---------- test only ----------

# from scrapy.crawler import CrawlerProcess
# process = CrawlerProcess(settings={
#     "FEEDS": {
#         "theverge_data.json": {"format": "json"},
#     },
# })

# process.crawl(TheVergeSpider)
# process.start()