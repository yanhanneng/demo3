
import re
import requests
from lxml import etree

def xshuospider():
    url = "http://www.quanshuwang.com/book/44/44683/15379612.html"
    response = requests.get(url=url)
    html = response.content.decode("gbk")
    html_down = etree.HTML(html)
    txt = html_down.xpath("//div[@class='mainContenr']//text()")
    print(txt)

    # reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    # reg = re.compile(reg)
    # urls = re.findall(reg, html)


    print(html)

if __name__ == '__main__':
    xshuospider()