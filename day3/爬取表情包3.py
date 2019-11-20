# -*- coding:utf-8 -*-

import re,time

import requests,threading
from lxml import etree

gLock = threading.Lock()

class BiaoqingSpider(object):
    def __init__(self):
        self.base_url = "https://fabiaoqing.com/biaoqing/lists/page/%d.html"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def send_requests(self,url):
        response = requests.get(url,headers=self.headers)
        return response

    def parse_response(self, response):   #笑话页面URL提取
        html = response.content.decode()
        html_down = etree.HTML(html)
        url_list = html_down.xpath("//div[@class='tagbqppdiv']/a/img/@data-original")
        return url_list

    def save_image(self, response, file_name):  #保存
        print("[INFO] : Save image <{}>".format(response.url))
        with open("./Images7/"+file_name,'wb') as f:
            f.write(response.content)

    def main(self):
        # a1 = time.time()
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
                print(url_list)
                for xh_url in url_list:
                    response = self.send_requests(url=xh_url)
                    time.sleep(0.2)
                    self.save_image(response, xh_url[-10:])

            except Exception as e:
                print("[ERROR]：请求处理失败，{}"%format(e))
        print("谢谢使用")

if __name__ == '__main__':
    spider = BiaoqingSpider()

    spider.main()


