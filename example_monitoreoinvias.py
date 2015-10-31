import json
import logging
import itertools

from lxml.cssselect import CSSSelector

from tarantula.scraper import ScraperTask, scrape_tasks, scrape
from tarantula.parser import parse
from tarantula.parsers.html import HtmlParser
from tarantula.utils import join_json

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')

logger = logging.getLogger("tarantula")


class MonitoreoViasParserSearchResults(HtmlParser):
  '''
  Extrae los ids de los enlaces a los perfiles de las vias en construccion
  '''
  def extract(self, parsed_data):
    anchors = CSSSelector("a")(parsed_data)
    urls = [anchor.get('href')for anchor in anchors]
    urls = list(filter(lambda x: "publico-via.php?id=" in x, urls))
    ids = list(set([url.split("id=")[1] for url in urls]))
    return json.dumps(ids)


scrape_busqueda_data_folder = "busqueda_monitoria_vias_raw"
extracted_busqueda_data_folder =  "busqueda_monitoria_vias_extracted"

def busqueda_de_vias():
  params = {
       "id" : ["05","15","17","18","19","27","25","95","41","52","54","63","66","68","73","76"]
  }
  url = "https://monitoreoinvias.com/publico-departamento.php"
  scrape(url, output_folder=scrape_busqueda_data_folder, params_and_values=params, workers=10)
  parse(input_folder=scrape_busqueda_data_folder, output_folder=extracted_busqueda_data_folder, parser=MonitoreoViasParserSearchResults(), workers=10)


busqueda_de_vias()
set_of_identifiers = set(list(itertools.chain(*join_json(extracted_busqueda_data_folder))))
