import codecs
import os
from multiprocessing import Pool, Value
from os import listdir

from tarantula.utils import get_input_output_pairs, assure_folder_exists, remove_file

import logging

logger = logging.getLogger("tarantula")

class Parser:

    def open_file(self, path):
        return codecs.open(path, 'r', 'utf-8')

    def parse(self, path):
        pass

    def extract(self, parsed_data):
        pass


class XlsParser(Parser):
    def parse(self, path):
        pass


class ParseTask:
    def __init__(self, path_to_file, path_to_output_file, parser):
        self.path = path_to_file
        self.parser = parser
        self.output_file = path_to_output_file

    def execute(self):
        try:
            extracted_data = self.extract()
            output = codecs.open(self.output_file, 'w', 'utf-8')
            output.write(extracted_data)
            output.close()
        except Exception as e:
            remove_file(self.output_file)
            logger.error("Error while parsing %s -- %s"%(self.path, e))


    def extract(self):
        parsed_object = self.parser.parse(self.path)
        return self.parser.extract(parsed_object)


def parser_worker(parser_task):
    parser_task.execute()


def parse(input_folder, output_folder, parser, workers=5):
    assure_folder_exists(output_folder)
    pool = Pool(workers)
    input_output_pairs = get_input_output_pairs(input_folder, output_folder)
    tasks = list([ParseTask(input_file_name, output_file_name, parser) for input_file_name, output_file_name in input_output_pairs])
    
    info_line = "Parsing  %s tasks with %s workers"%(len(tasks), workers)
    logger.info(info_line)
    
    pool.map(parser_worker, tasks)
