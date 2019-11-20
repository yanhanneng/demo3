# -*- coding:utf-8 -*-

import xlwt
import requests
from lxml import etree
import time

all_info_list = []

def get_info(url):
    # url = "https://www.qidian.com/all?page=5"
    response = requests.get(url=url).content.decode("utf8")
    html_down = etree.HTML(response)
    infos = html_down.xpath("//ul[@class='all-img-list cf']/li")
    # print(infos)
    for info in infos:
        # 标题
        title = info.xpath('div[2]/h4/a/text()')[0]
        # 作者
        author = info.xpath('div[2]/p[1]/a[1]/text()')[0]
        # 风格1
        style1 = info.xpath('div[2]/p[1]/a[2]/text()')[0]
        # 风格2
        style2 = info.xpath('div[2]/p[1]/a[3]/text()')[0]
        # 风格
        style = style1 + style2
        # 完结程度
        complete = info.xpath('div[2]/p[1]/span/text()')[0]
        # 小说介绍
        introduce = info.xpath('div[2]/p[2]/text()')[0].strip()

        info_list = [title, author, style, complete, introduce]
        # 把数据存入列表
        all_info_list.append(info_list)
        print(all_info_list)
    time.sleep(0.1)


if __name__ == '__main__':
    urls = ['http://a.qidian.com/?page={}'.format(str(i)) for i in range(1, 6)]
    for url in urls:
        get_info(url)
        time.sleep(1)
    header = ["title","author","style","complete","introduce"]
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet("Sheel")
    for h in range(len(header)):
        sheet.write(0,h,header[h])

    i = 1
    for list in all_info_list:
        j = 0
        for data in list:
            sheet.write(i,j,data)
            print(data)
            j += 1
        i += 1
    book.save("xiaoshuo.xls")
























