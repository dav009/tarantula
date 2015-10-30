import tarantula.resolver as resolver
from tarantula.scraper import ScraperTask
from tarantula.errors import NotResolved
import pytest


class TestUtils:
    def test_make_request(self):
        task = ScraperTask("http://www.google.com", "output_folder", method="get", params={}, headers={} )
        html_text = resolver.make_request(task)
        assert("google" in html_text)

    def test_failing_request(self, monkeypatch):
        task = ScraperTask("http://www.blablanonexistangasdadasd.com", "output_folder", method="get", params={}, headers={} )
        with pytest.raises(Exception):
            resolver.make_request(task)
