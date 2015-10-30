import requests
from tarantula.errors import NotResolved

requests_methods = {
    "post": requests.post,
    "get": requests.get
}


def make_request(scraper_task):
    try:
        request = requests_methods[scraper_task.method]
        result = request(scraper_task.url, params=scraper_task.params, headers=scraper_task.headers)
        if result.status_code != 200:
            raise(NotResolved)
        else:
            return result.text
    except KeyError:
        raise ValueError("Wrong requests method")
    except Exception as e:
        raise e
