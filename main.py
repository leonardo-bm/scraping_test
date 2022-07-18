#!/usr/bin/env python3

from scraping.spiders.engadget import EngadgetSpider
from scraping.spiders.gizmodo import GizmodoSpider
from scraping.spiders.phoronix import PhoronixSpider
from scraping.spiders.theverge import TheVergeSpider

from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

settings = get_project_settings()
settings.set('FEED_URI', 'main_result.json')
settings.set('FEED_FORMAT', 'json')

configure_logging()

runner = CrawlerRunner(settings)

runner.crawl(EngadgetSpider)
runner.crawl(GizmodoSpider)
runner.crawl(PhoronixSpider)
runner.crawl(TheVergeSpider)

d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()
