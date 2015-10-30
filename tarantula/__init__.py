import logging

from scraper import scrape_tasks
from scraper import scrape

format_ = "%(asctime)s %(levelname)-8s %(name)-18s: %(message)s"
logging.basicConfig(format=format_)
fileHandler = logging.FileHandler("logger.txt")

logger = logging.getLogger("tarantula")
logger.setLevel(logging.INFO)
logger.addHandler(fileHandler)