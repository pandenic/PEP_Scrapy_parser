"""Contains pipeline descriptions."""
import os.path
from typing import Dict

from scrapy import Item, Spider

from pep_parse.constants import BASE_DIR, PEP_SUMMARY_RESULT_PATH
from pep_parse.settings import FEED_EXPORT_ENCODING


class PepParsePipeline:
    """Describe a pipline for PepParse."""

    def open_spider(self, spider: Spider) -> None:
        """Perform action when spider is being started."""
        self.pep_summary: Dict[str, int] = {}

    def process_item(self, item: Item, spider: Spider) -> Item:
        """Perform action when item is being processed."""
        if self.pep_summary.get(item["status"]):
            self.pep_summary[item["status"]] += 1
        else:
            self.pep_summary[item["status"]] = 1
        return item

    def close_spider(self, spider: Spider) -> None:
        """Perform action when spider is being closed."""
        total = sum(self.pep_summary.values())

        pep_summary_filepath = os.path.join(
            BASE_DIR,  # BASE_DIR tests/test_main.py::test_run_scrapy
            PEP_SUMMARY_RESULT_PATH,
        )

        with open(pep_summary_filepath, mode="w", encoding=FEED_EXPORT_ENCODING) as file:
            file.write("Статус,Количество\n")
            file.writelines(
                [
                    f"{status},{quantity}\n"
                    for status, quantity in self.pep_summary.items()
                ],
            )
            file.write(f"Total,{total}\n")
