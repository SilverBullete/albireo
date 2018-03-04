import re
from .abstract import AbstractRule
import datetime

# 国际学院新闻速递
class GjxyxwRule(AbstractRule):
    name = 'gjxyxw'

    def title(self):
        return self.selector.xpath("//div[@class='new_head']/h3/text()").extract()[0]

    def content(self):
        content = ""
        for p in self.selector.xpath("//div[@class='new_body']").xpath(".//p"):
            content = content + p.extract().strip()
            # content = re.sub(r'<p.*?>', "", content)
            # content = re.sub(r'</p>', "", content)
            # content = re.sub(r'<br>', "\r", content)
            # content = re.sub(r'<.*?>', "", content)
            # content = re.sub(r'<img.*?>', "", content)
        return content

    def description(self):
        return ''

    def published_at(self):
        t = re.sub(r'<.*?>', "", self.selector.xpath("//div[@class='new_info']/span").extract()[1]).split(u"：")[
            1]
        return datetime.datetime.strptime(str(t), '%Y-%m-%d').timestamp()

    def author(self):
        return re.sub(r'<.*?>', "", self.selector.xpath("//div[@class='new_info']/span").extract()[0]).split(u"：")[
            1]

    def category(self):
        return 'gjxy'

    def url_list(self, sel):
        urls = self.selector.xpath("//div[@id='news']/a/@href").extract()

        for url in urls:
            yield 'http://www.gjxy.zjut.edu.cn' + url