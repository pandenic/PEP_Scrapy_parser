"""Contains settings for PEP Scrapy project."""
import os.path
from pathlib import Path

from pep_parse.constants import BASE_DIR, PEP_LIST_FILENAME, RESULTS_DIR

Path.joinpath(BASE_DIR, RESULTS_DIR).mkdir(exist_ok=True)


BOT_NAME = "pep_parse"
NEWSPIDER_MODULE = f"{BOT_NAME}.spiders"
SPIDER_MODULES = [NEWSPIDER_MODULE]

ROBOTSTXT_OBEY = True

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    os.path.join(RESULTS_DIR, PEP_LIST_FILENAME): {
        "format": "csv",
        "fields": ["number", "name", "status"],
        "overwrite": True,
    },
}

ITEM_PIPELINES = {
    "pep_parse.pipelines.PepParsePipeline": 300,
}
