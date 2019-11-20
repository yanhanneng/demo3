# https://www.sbiquge.com/0_466/  小说url
# //div[@class="listmain"]/dl/dd/a/@href  所有章节的url提取
# //div[@class="listmain"]/dl/dd/a/text()  章节名字
# //div[@id="content"]/text() 小说提取



# //div[@class="clearfix dirconone"]/li/a/@href  url获取
# //div[@class="clearfix dirconone"]/li/a/@title  章节名

import re

import requests
from lxml import etree
from bs4 import BeautifulSoup


class ZhetianSpider(object):
    def __init__(self):
        self.base_url = "https://www.sbiquge.com/0_466/"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.content_pattern = re.compile("\s|<.*?>|&.*?;")

    def send_request(self, url):
        """ 发送url请求，并返回响应"""
        # print("[INFO]: send request [{}] <{}>".format("GET", url))
        response = requests.get(url, headers=self.headers)
        return response

    def parse_detail(self, response):
        """ 提取 并 返回所有连接章节页的连接 """
        html = response.content
        html_dom = etree.HTML(html)
        url_list = html_dom.xpath("//div[@class='listmain']/dl/dd/a/@href")
        return url_list

    def txt_content(self, response):
        """ 提取 并 返回所有章节的文本的内容 """
        html = response.content
        html_dom = etree.HTML(html)
        wenben_list = html_dom.xpath("//div[@id='content']/text()")
        for wenben in wenben_list:
            return wenben

    def save_data(self, wenben_list ):
        """ 保存所有图片数据 """
        # print("[INFO] : Save image <{}>".format(file_name))
        with open("zhetian.txt" , "wb") as f:
            pass


    def main(self):
        """ 调度中心，控制各个方法的执行并传递参数"""

        ## 第一级for： 处理所有列表页的请求

        # try:
        response = self.send_request(url=self.base_url)
        detail_url_list = self.parse_detail(response)
        for detail_url in detail_url_list:
            zhangjie_url = "https://www.sbiquge.com"+detail_url
            response = self.send_request(zhangjie_url)

            wenben = self.txt_content(response)
            wenben = self.content_pattern.sub("", wenben)
            print(wenben)



        # except Exception as e:
        #     print("[ERROR]: Bad Request {}".format(e) )

        print("[INFO]:谢谢使用")


if __name__ == '__main__':
    spider = ZhetianSpider()
    spider.main()
