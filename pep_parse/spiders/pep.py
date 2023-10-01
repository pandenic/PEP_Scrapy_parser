"""Contains spider description."""
import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    """Contains PepSpider description."""

    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
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

    def parse_pep(self, response, number, name):
        """Perform parsing through followed url."""
        data = {
            "number": number,
            "name": name,
            "status": response.css("abbr::text").get(),
        }
        yield PepParseItem(data)
