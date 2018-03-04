import re
from .abstract import AbstractRule
import datetime

# 理学院公告
class LxyxwRule(AbstractRule):
    name = 'lxyxw'

    def title(self):
        return self.selector.xpath("//div[@class='cg-content']/h2/text()").extract()[0]

    def content(self):
        content = ""
        for p in self.selector.xpath("//div[@class='art-content article-content']"):
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
        t = self.selector.xpath("//div[@class='cg-content']/p/text()").extract()[0].split(u"：")[
            3].rsplit()[0]
        return datetime.datetime.strptime(str(t), '%Y年%m月%d日').timestamp()

    def author(self):
        return self.selector.xpath("//div[@class='cg-content']/p/text()").extract()[0].split(u"：")[
            2].rsplit()[0]

    def category(self):
        return 'lxy'

    def url_list(self, sel):
        urls = self.selector.xpath("//ul[@class='cg-news-list']/li/a/@href").extract()

        for url in urls:
            yield 'http://www.lxy.zjut.edu.cn/' + url