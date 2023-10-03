"""Define the models for spider middleware."""
from typing import Iterable, Union

from scrapy import Item, Request, Spider, signals
from scrapy.crawler import Crawler
from scrapy.http import Response


class PepParseSpiderMiddleware:
    """Contains middlewares' description for PepParseSpider."""

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> 'PepParseSpiderMiddleware':
        """Create spiders."""
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response: Response, spider: Spider) -> None:
        """
        Contains actions for each response.

        Each response that goes through
        the spider middleware and into the spider.
        """
        return None

    def process_spider_output(
        self,
        response: Response,
        result: Union[Iterable, Item],
        spider: Spider,
    ) -> Union[Iterable, Item]:
        """Proceed response the results from the Spider."""
        for i in result:
            yield i

    def process_spider_exception(
        self, response: Response, exception: Exception, spider: Spider,
    ) -> None:
        """
        Define exception handling.

        For a spider or process_spider_input() method.
        """
        pass

    def process_start_requests(
        self, start_requests: Iterable[Request], spider: Spider,
    ) -> Iterable[Request]:
        """
        Proceed response the results from the Spider.

        Without an associated response.
        """
        for r in start_requests:
            yield r

    def spider_opened(self, spider: Spider) -> None:
        """Define action when spider is opened."""
        spider.logger.info("Spider opened: %s" % spider.name)


class PepParseDownloaderMiddleware:
    """Contains downloader middleware actions."""

    @classmethod
    def from_crawler(cls, crawler: Crawler) -> 'PepParseDownloaderMiddleware':
        """Create your spiders."""
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request: Request, spider: Spider) -> None:
        """
        Perform actions for requests.

        Requests That goes through the downloader.
        """
        return None

    def process_response(
        self, request: Request, response: Response, spider: Spider,
    ) -> Response:
        """
        Perform actions when response returned.

        Response returned from the downloader.
        """
        return response

    def process_exception(
        self, request: Request, exception: Exception, spider: Spider,
    ) -> None:
        """
        Define exception handling.

        For a spider or process_spider_input() method.
        """
        pass

    def spider_opened(self, spider: Spider) -> None:
        """Define action when spider is opened."""
        spider.logger.info("Spider opened: %s" % spider.name)
