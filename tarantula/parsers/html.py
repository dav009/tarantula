from lxml import html
from lxml.cssselect import CSSSelector


from tarantula.parser import Parser

class HtmlParser(Parser):

    def parse(self, path):
        f = self.open_file(path)
        html_content = "\n".join([line for line in f])
        return html.fromstring(html_content)