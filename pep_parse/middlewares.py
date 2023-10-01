"""Define the models for spider middleware."""
from scrapy import signals


class PepParseSpiderMiddleware:
    """Contains middlewares' description for PepParseSpider."""

    @classmethod
    def from_crawler(cls, crawler):
        """Create spiders."""
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        """
        Contains actions for each response.

        Each response that goes through
        the spider middleware and into the spider.
        """
        return None

    def process_spider_output(self, response, result, spider):
        """Proceed response the results from the Spider."""
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        """
        Define exception handling.

        For a spider or process_spider_input() method.
        """
        pass

    def process_start_requests(self, start_requests, spider):
        """
        Proceed response the results from the Spider.

        Without an associated response.
        """
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        """Define action when spider is opened."""
        spider.logger.info("Spider opened: %s" % spider.name)


class PepParseDownloaderMiddleware:
    """Contains downloader middleware actions."""

    @classmethod
    def from_crawler(cls, crawler):
        """Create your spiders."""
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        """
        Perform actions for requests.

        Requests That goes through the downloader.
        """
        return None

    def process_response(self, request, response, spider):
        """
        Perform actions when response returned.

        Response returned from the downloader.
        """
        return response

    def process_exception(self, request, exception, spider):
        """
        Define exception handling.

        For a spider or process_spider_input() method.
        """
        pass

    def spider_opened(self, spider):
        """Define action when spider is opened."""
        spider.logger.info("Spider opened: %s" % spider.name)
