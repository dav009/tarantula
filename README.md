# Tarantula

Muchos sitios tienen datos interesantes pero no tienen APIs, ni ofrecen dumps de los datos.

Tarantula es un scraper+parser para descargar los datos de esos sitios y convertirlos en datasets


## Requisitos: 
- Python3.4

## Instalacion
- `sudo pip install git+git://github.com/dav009/tarantula.git`


## Ejemplo

https://monitoreoinvias.com ofrece informacion sobre el estado de las vias.

Si quisieramos descargar todas las paginas que contienen informacion sobre las vias tendriamos que descargar los enlaces a los perfiles de las vias de las paginas de busqueda. 

Para obtener una pagina de busqueda necesitamos enviar
un request get `https://monitoreoinvias.com/publico-departamento.php` con el parametro `id` que corresponde al departamento.
i.e: `https://monitoreoinvias.com/publico-departamento.php?id=05`.

Luego de descargar todas las paginas, tenemos que parsear el html para buscar los enlaces a los perfiles de vias.

Tarantula ofrece ambas utilidades.

El siguiente codigo crea un scraper que descargara el contenido de las paginas de busqueda,pasando cada uno de los valores que puede tomar el parametro `id`.

```python
from tarantula.scraper import scrape

scrape_busqueda_data_folder = "busqueda_monitoria_vias_raw"
params = {
     "id" : ["05","15","17","18","19","27","25","95","41","52","54","63","66","68","73","76"]
}
url = "https://monitoreoinvias.com/publico-departamento.php"
scrape(url, output_folder=scrape_busqueda_data_folder, params_and_values=params, workers=10)
```


`scrape` almacenara todos los resultados en `output_folder` que luego pueden ser parseados por `tarantula.parse`

```python
from tarantula.parser import parse
extracted_busqueda_data_folder =  "busqueda_monitoria_vias_extracted"

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

parse(input_folder=scrape_busqueda_data_folder, output_folder=extracted_busqueda_data_folder, parser=MonitoreoViasParserSearchResults(), workers=10)
```

`parse` recibe:
 - `input_folder`: un folder de entrada donde previamente `scrape` ha descargado los datos. 
 - `output_folder`: un folder de salida donde guardara los resultados.
 - `parser`: un parseador el cual se encargara de parsear cada archivo del folder de entrada y extraera los datos que se guardaran en el folder de salida.

 Cada archivo dentro del folder pasa por `MonitoreoViasParserSearchResults` que en este caso es un parseador de html.
El parseador solo implementa la funcion `extract` donde recibe el html parseado, y retorna un archivo json con los `ids` encontrados dentro de los `<a>` tags de una pagina previamente descargada.
`parse` enviara cada archivo al parseador y guardara los resultados en el `output_folder`


## Notas

`scrape` puede recibir un diccionario complejo con parametros, en ese caso todos los parametros son combinados y enviados como request. 

Ejemplo:

```python
....
params = {
     "param1" : ["1", "2"],
     "param2": ["a", "b", "c"],
     "param3": ["x", "y", "z"]
}
scrape(url, output_folder, params_and_values=params, workers=10)
```

scrapeara `url` con parametros: `1, a, x`, `1, a, y` .... `2, b, y`.... `2, c, z`
