# -*- coding:utf-8 -*-

# url = https://www.2952.cc/b/10/10344/


import requests
import threading,re
from lxml import etree

def xiaoshuo():
    url = "https://www.2952.cc/b/61/61901/"
    html = requests.get(url=url).content.decode("GBK")
    html_down = etree.HTML(html)
    url_list = html_down.xpath("//div[@class='dirtitone']//li/a/@href")
    for zj_url in url_list:
        zj_url = url + zj_url[12:]
        html = requests.get(url=zj_url).content.decode("gbk")
        html_down = etree.HTML(html)
        txt_list = html_down.xpath("//div[@id='content']/text()")   #小说内容
        mc_list = html_down.xpath("//div[@class='bookname']/h1/text()")  #章节名称
        for content in txt_list:
            print("[INFO] : Save image <{}>".format(zj_url))
            with open("zhetian3.txt", "a",encoding='utf-8') as f:
                # f.write(mc)
                f.write(content)
                # f.write("\n\n")
if __name__ == '__main__':
    t1 = threading.Thread(target=xiaoshuo)

    t1.start()

    # xiaoshuo()


