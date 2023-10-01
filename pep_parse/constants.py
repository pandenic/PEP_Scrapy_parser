"""Contains constants for PEP parser."""
import time
from pathlib import Path

CURRENT_TIME_FORMAT = time.strftime("%Y-%m-%d_%H-%M-%S")
PEP_SUMMARY_FILENAME = f"status_summary_{CURRENT_TIME_FORMAT}.csv"
PEP_LIST_FILENAME = "pep_%(time)s.csv"

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = "results"
