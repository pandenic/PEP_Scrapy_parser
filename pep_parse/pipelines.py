"""Contains pipeline descriptions."""
import os.path

from pep_parse.constants import BASE_DIR, PEP_SUMMARY_FILENAME, RESULTS_DIR


class PepParsePipeline:
    """Describe a pipline for PepParse."""

    def open_spider(self, spider):
        """Perform action when spider is being started."""
        self.pep_summary = {}

    def process_item(self, item, spider):
        """Perform action when item is being processed."""
        if self.pep_summary.get(item["status"]):
            self.pep_summary[item["status"]] += 1
        else:
            self.pep_summary[item["status"]] = 1
        return item

    def close_spider(self, spider):
        """Perform action when spider is being closed."""
        total = sum(self.pep_summary.values())

        pep_summary_filepath = os.path.join(
            BASE_DIR, RESULTS_DIR, PEP_SUMMARY_FILENAME,
        )

        with open(pep_summary_filepath, mode="w", encoding="utf-8") as file:
            file.write("Статус,Количество\n")
            file.writelines(
                [
                    f"{status},{quantity}\n"
                    for status, quantity in self.pep_summary.items()
                ],
            )
            file.write(f"Total,{total}\n")
