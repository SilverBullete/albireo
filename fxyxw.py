import re
from .abstract import AbstractRule
import datetime

# 法学院新闻
class GjxyxwRule(AbstractRule):
    name = 'fxyxw'

    def title(self):
        return self.selector.xpath("//div[@id='news1']/div[@class='news1title']/text()").extract()[0]

    def content(self):
        content = ""
        for p in self.selector.xpath("//div[@class='news1content']"):
            content = content + p.extract().strip()
            # content = re.sub(r'<p.*?>', "", content)
            # content = re.sub(r'</p>', "", content)
            # content = re.sub(r'<br>', "\r\n", content)
            # content = re.sub(r'<.*?>', "", content)
            # content = re.sub(r'<img.*?>', "", content)
        return content

    def description(self):
        return ''

    def published_at(self):
        t = self.selector.xpath("//div[@class='news1info']/text()").extract()[0].split(u"：")[
            2].split()[0]
        return datetime.datetime.strptime(str(t), '%Y-%m-%d').timestamp()

    def author(self):
        return self.selector.xpath("//div[@class='news1info']/text()").extract()[0].split(u"：")[
            1].split()[0]

    def category(self):
        return 'fxy'

    def url_list(self, sel):
        urls = self.selector.xpath("//*[@id='bboxnews2']/dl/dt/a/@href").extract()

        for url in urls:
            yield 'http://www.law.zjut.edu.cn/' + url