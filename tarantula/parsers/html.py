from lxml import html
from lxml.cssselect import CSSSelector


from parser import Parser

class HtmlParser(Parser):
    def parse(self, path):
        f = self.open_file(path)
        html_content = "\n".join([line for line in f])
        print(html_content)
        return html.fromstring(html_content)