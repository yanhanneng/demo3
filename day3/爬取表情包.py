# -*- coding:utf-8 -*-

import re,time

import requests,threading
from lxml import etree

gLock = threading.Lock()

class BiaoqingSpider(object):
    def __init__(self):
        self.base_url = "https://www.doutula.com/photo/list/?page=%d"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def send_requests(self,url):
        response = requests.get(url,headers=self.headers)
        return response

    def parse_response(self, response):   #笑话页面URL提取
        html = response.content.decode()
        html_down = etree.HTML(html)
        url_list = html_down.xpath("//div[@class='page-content text-center']/div/a/@href")
        return url_list

    def src_respinse(self,response):  #图片页面url列表
        html = response.content.decode()
        html_down = etree.HTML(html)
        tupian_src_list = html_down.xpath("//div['swiper-slide']//td/img/@src ")
        return tupian_src_list

    def save_image(self, response, file_name):  #保存
        print("[INFO] : Save image <{}>".format(response.url))
        with open("./Images6/"+file_name,'wb') as f:
            f.write(response.content)

    def main(self):
        while True:
            try:
                nNum = int(input(u"请输入需要下载表情包的页数: "))
                if nNum > 0:
                    break
            except ValueError:
                print(u"请输入数字。")
                continue
        for i in range(nNum):
            bases_url = self.base_url %(i+1)
            try:
                response = self.send_requests(url=bases_url)
                url_list = self.parse_response(response)
                for xh_url in url_list:
                    response = self.send_requests(url=xh_url)
                    time.sleep(0.01)
                    tupian_src_list = self.src_respinse(response)
                    for tupian_src in tupian_src_list:
                        response = requests.get(url=tupian_src)
                        self.save_image(response, tupian_src[-10:])
            except Exception as e:
                print("[ERROR]：请求处理失败，{}"%format(e))
        print("谢谢使用")

if __name__ == '__main__':
    spider = BiaoqingSpider()
    spider.main()

