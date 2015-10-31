import json
import logging

from lxml.cssselect import CSSSelector

from tarantula.scraper import ScraperTask, scrape_tasks, scrape
from tarantula.parser import parse
from tarantula.parsers.html import HtmlParser

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M')

logger = logging.getLogger("tarantula")


class SampleHTMLParser(HtmlParser):
  '''
  Sample html parser 
  coutns anchors & paragraphs
  '''
  def extract(self, parsed_data):
    number_of_anchors = len(CSSSelector("a")(parsed_data))
    number_of_paragraphs =  len(CSSSelector("p")(parsed_data))
    data = { "anchors": number_of_anchors, "paragraphs": number_of_paragraphs}
    return json.dumps(data)

def get_registraduria_with_params():
  '''
  combines all the params in the given dict `param`
  scrapes all the urls with those params in the given output_folder (scrape_data_folder)

  then the files in  scrape_data_folder are parsed via SampleHTMLParser which counts the anchors & paragraphs
  in each file, and outputs the results to another folder.
  '''
  scrape_data_folder = "registraduria_raw_data"
  extracted_data_folder =  "registraduria_extracted_data"

  params = {
       "objeto" : ["10000000", "11000000", "12000000", "15000000", "13000000", "14000000", "27000000", "20000000", "21000000"],
       "paginaObjetivo": ["1"],
       "cuantias": ["1", "2", "3"]
  }
  url = "https://www.contratos.gov.co/consultas/resultadosConsulta.do?&ctl00$ContentPlaceHolder1$hidIDProducto=-1&ctl00$ContentPlaceHolder1$hidRedir=&departamento=&ctl00$ContentPlaceHolder1$hidNombreDemandante=-1&ctl00$ContentPlaceHolder1$hidNombreProducto=-1&fechaInicial=&ctl00$ContentPlaceHolder1$hidIdEmpresaC=0&ctl00$ContentPlaceHolder1$hidIdOrgV=-1&ctl00$ContentPlaceHolder1$hidIDProductoNoIngresado=-1&ctl00$ContentPlaceHolder1$hidRangoMaximoFecha=&fechaFinal=&desdeFomulario=true&ctl00$ContentPlaceHolder1$hidIdOrgC=-1&ctl00$ContentPlaceHolder1$hidIDRubro=-1&tipoProceso=&registrosXPagina=10&numeroProceso=&municipio=0&estado=0&ctl00$ContentPlaceHolder1$hidNombreProveedor=-1&ctl00$ContentPlaceHolder1$hidIdEmpresaVenta=-1"


  print("scraping registraduria...")
  scrape(url, output_folder=scrape_data_folder, params_and_values=params, workers=10)
  print("parsing registraduria..")
  parse(input_folder=scrape_data_folder, output_folder=extracted_data_folder, parser=SampleHTMLParser(), workers=8)


def just_scrape_tasks_in_list():
  '''
  Creates 5 tasks to scrape google.com
  to the given output folder
  '''
  print("scraping google 5 times..")
  tasks = []
  for i in range(0, 5):
      tasks.append(ScraperTask(url="http://google.com",
                               output_folder="raw_data_tasks_in_list"))
  scrape_tasks(tasks)

get_registraduria_with_params()
just_scrape_tasks_in_list()
