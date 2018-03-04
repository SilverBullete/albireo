import re
from .abstract import AbstractRule
import datetime

# 经贸学院公告通知
class JmxyggRule(AbstractRule):
    name = 'jmxygg'

    def title(self):
        return self.selector.xpath("//div[@class='news1title']/text()").extract()[0]

    def content(self):
        content = ""
        for p in self.selector.xpath("//div[@class='news1content']").xpath(".//p"):
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
            2].rsplit()[0]
        return datetime.datetime.strptime(str(t), '%Y-%m-%d').timestamp()

    def author(self):
        return self.selector.xpath("//div[@class='news1info']/text()").extract()[0].split(u"：")[
            1].rsplit()[0]

    def category(self):
        return 'jmxy'

    def url_list(self, sel):
        urls = self.selector.xpath("//*[@id='bboxnews2']/dl/dt/a/@href").extract()

        for url in urls:
            yield 'http://www.cba.zjut.edu.cn/' + url