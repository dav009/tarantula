import logging
import codecs
from multiprocessing import Pool, Value
import os

import resolver
from utils import combine_parameters

logger = logging.getLogger("tarantula")

counter = Value('i', 1)


def scraper_worker(scraper_task, f):
    try:
        result = resolver.make_request(scraper_task)
        processed_result = f(result)
        output = codecs.open(scraper_task.filename(), 'w', 'utf-8')
        output.write(processed_result)
        output.close()
        logger.info("Finished task %s" % (scraper_task.filename()))
    except Exception as e:
        infoline = "Scraper task  %s failed with: %s"%(scraper_task.filename(), e)
        logger.error(infoline)
        print(infoline)
    counter.value += 1
    if (counter.value % 1000) == 0:
        print("done %s...\r" % (counter.value))


class ScraperTask:

    def __init__(self, url, output_folder, method="get", params={}, headers={}):
        self.params = params
        self.method = method
        self.url = url
        self.folder = output_folder
        self.headers = headers

    def name(self):
        if len(self.params.keys()) > 0:
            params_name = "_".join([key + "_" + value for key, value in zip(self.params.keys(), self.params.values()) ])
            name = params_name
        else:
            name = self.url.replace("/", "_")
        return name

    def filename(self):
        return os.path.join(self.folder, self.name()) 


class Scraper:
    def base_scrape(self, list_of_tasks, f, workers=5):
        pool = Pool(workers)
        info_line = "Scraping  %s tasks with %s workers"%(len(list_of_tasks), workers)
        logger.info(info_line)
        print(info_line)
        tasks = list([(scraper_task, f) for scraper_task in list_of_tasks])
        pool.starmap(scraper_worker, tasks)


def do_nothing(r):
    return r


def get_tasks(url, output_folder, params_and_values={}, method="get", headers={}):
    list_of_combined_params = combine_parameters(params_and_values)
    return list([ScraperTask(url=url, params=param_config, headers=headers, method=method, output_folder=output_folder) for param_config in list_of_combined_params])


def scrape(url, output_folder, params_and_values={}, method="get", headers={}, workers=5, f=do_nothing):
    tasks = get_tasks(url=url, output_folder=output_folder, params_and_values=params_and_values, method=method, headers=headers)
    scrape_tasks(tasks, workers=workers, f=f)


def scrape_tasks(list_of_tasks, workers=5, f=do_nothing):
    Scraper().base_scrape(list_of_tasks, f=f, workers=workers)
