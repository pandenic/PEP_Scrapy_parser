"""Contains spider description."""
from typing import Any, Generator

import scrapy
from scrapy import Request
from scrapy.http import Response

from pep_parse.constants import PARSING_DOMAIN
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Contains PepSpider description."""

    name = "pep"
    allowed_domains = [PARSING_DOMAIN]
    start_urls = [f"https://{PARSING_DOMAIN}/"]

    def parse(self, response: Response) -> Generator[Request, Any, None]:
        """Perform parsing through url in start_urls."""
        pep_list = response.css("section[id=numerical-index] tbody tr")
        for pep in pep_list:
            pep_data = {
                "number": str(pep.css("a::text").getall()[0]),
                "name": str(pep.css("a::text").getall()[1]),
            }
            yield response.follow(
                pep.css("a::attr(href)").get(),
                callback=self.parse_pep,
                cb_kwargs=pep_data,
            )

    def parse_pep(
        self,
        response: Response,
        number: str,
        name: str,
    ) -> Generator[PepParseItem, Any, None]:
        """Perform parsing through followed url."""
        data = {
            "number": number,
            "name": name,
            "status": response.css("abbr::text").get(),
        }
        yield PepParseItem(data)
