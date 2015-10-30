from pyexcel_xls import get_data

from tarantula.parser import Parser

class XlsParser(Parser):
    def parse(self, path):
        return get_data(path)