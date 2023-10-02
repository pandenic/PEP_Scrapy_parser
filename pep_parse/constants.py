"""Contains constants for PEP parser."""
import os.path
import time
from pathlib import Path

PARSING_DOMAIN = "peps.python.org"

OUTPUT_FILE_FORMAT = "csv"
CURRENT_TIME_FORMAT = time.strftime("%Y-%m-%d_%H-%M-%S")
PEP_SUMMARY_FILENAME = (
    f"status_summary_{CURRENT_TIME_FORMAT}.{OUTPUT_FILE_FORMAT}"
)
PEP_LIST_FILENAME = f"pep_%(time)s.{OUTPUT_FILE_FORMAT}"

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = "results"
PEP_SUMMARY_RESULT_PATH = os.path.join(RESULTS_DIR, PEP_SUMMARY_FILENAME)
