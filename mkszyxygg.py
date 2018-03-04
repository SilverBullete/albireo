import re
from .abstract import AbstractRule
import datetime

# 马克思主义学院公告
class MkszyxyggRule(AbstractRule):
    name = 'mkszyxygg'

    def title(self):
        return self.selector.xpath("//div[@id='news1']/div[@class='news1title']/text()").extract()[0]

    def content(self):
        content = ""
        for p in self.selector.xpath("//div[@class='news1content']"):
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
        t = self.selector.xpath("//div[@class='news1info']/text()").extract()[0].split(u"：")[
            3].split()[0]
        return datetime.datetime.strptime(str(t), '%Y-%m-%d').timestamp()

    def author(self):
        return self.selector.xpath("//div[@class='news1info']/text()").extract()[0].split(u"：")[
            1].rsplit(u"来源")[0].split()[0]

    def category(self):
        return 'mkszyxy'

    def url_list(self, sel):
        urls = self.selector.xpath("//*[@id='arrowlist2']/li/a/@href").extract()

        for url in urls:
            yield 'http://www.mkszyxy.zjut.edu.cn/' + url