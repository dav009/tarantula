
from scraper import ScraperTask
from scraper import scrape_tasks, scrape
from parser import parser
from parsers.html import HtmlParser


class SampleHTMLParser(HtmlParser):

	def extract(self, parsed_data):
		return str(parsed_data)


parser(input_folder="/Users/dav009/source/tarantula/data/", output_folder="/Users/dav009/source/tarantula/parsed/", parser=SampleHTMLParser())

#tasks = []
#for i in range(0,10000):
#    tasks.append(ScraperTask(url="http://google.com",
#                             output_folder="/Users/dav009/source/tarantula/data/"))
#scrape_tasks(tasks)

#params = {
#     "objeto" : ["10000000", "11000000", "12000000", "15000000", "13000000", "14000000", "27000000", "20000000", "21000000", 
#                   "22000000", "26000000", "23000000", "24000000", "25000000", "40000000", "32000000", "31000000", "30000000"
#                   "39000000", "41000000", "50000000", "52000000", "43000000", "42000000", "44000000", "46000000", "45000000"
#                   "47000000", "49000000", "60000000", "48000000", "51000000", "56000000", "54000000", "55000000", "53000000",
#                   "94000000", "81000000", "82000000", "86000000", "84000000", "77000000", "91000000", "93000000", "83000000",
#                   "70000000", "92000000", "72000000", "80000000", "76000000", "71000000", "73000000", "85000000", "78000000",
#                   "90000000", "95000000"],
#
#     "paginaObjetivo": ["1"],
#     "cuantias": ["1", "2", "3", "4", "5"]
#}
#url = "https://www.contratos.gov.co/consultas/resultadosConsulta.do?&ctl00$ContentPlaceHolder1$hidIDProducto=-1&ctl00$ContentPlaceHolder1$hidRedir=&departamento=&ctl00$ContentPlaceHolder1$hidNombreDemandante=-1&ctl00$ContentPlaceHolder1$hidNombreProducto=-1&fechaInicial=&ctl00$ContentPlaceHolder1$hidIdEmpresaC=0&ctl00$ContentPlaceHolder1$hidIdOrgV=-1&ctl00$ContentPlaceHolder1$hidIDProductoNoIngresado=-1&ctl00$ContentPlaceHolder1$hidRangoMaximoFecha=&fechaFinal=&desdeFomulario=true&ctl00$ContentPlaceHolder1$hidIdOrgC=-1&ctl00$ContentPlaceHolder1$hidIDRubro=-1&tipoProceso=&registrosXPagina=10&numeroProceso=&municipio=0&estado=0&ctl00$ContentPlaceHolder1$hidNombreProveedor=-1&ctl00$ContentPlaceHolder1$hidIdEmpresaVenta=-1"
#
#
#scrape(url, output_folder="/Users/dav009/source/tarantula/data/", params_and_values=params)
