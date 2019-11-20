# 列表页： url = "http://tieba.baidu.com/f?"
#     params = {"kw" : xxx, "pn" : (page - 1) * 50}

#     提取详情页xpath("//a[@class='j_th_tit']/@href")

# 详情页： 提取图片的连接xpath("//img[@class='BDE_Image']/@src")
# 图片名提取：//div[@id="picture"]/p/img/@alt

# 图片： 直接 按 wb 保存即可。


import requests
from lxml import etree
import time,random,threading


class TiebaSpider(object):
    def __init__(self):
        self.base_url = "https://www.mzitu.com/page/3/"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

    def send_request(self, url):
        """ 发送url请求，并返回响应"""
        response = requests.get(url, headers=self.headers)
        return response

    def parse_detail(self, response):
        """ 提取 并 返回所有图片页的连接 """
        html = response.content
        html_dom = etree.HTML(html)
        url_list = html_dom.xpath("//div[@class='pic']/a/@href")
        return url_list

    def parse_image(self, response):
        """ 提取 并 返回所有连接图片的连接 """
        html = response.content
        html_dom = etree.HTML(html)
        url_list = html_dom.xpath("//div[@id='picture']/p/img/@src")
        # alt_list = html_dom.xpath("//div[@id='picture']/p/img/@alt")
        return url_list

    def save_image(self, response, file_name):
        """ 保存所有图片数据 """
        # print("[INFO] : Save image <{}>".format(file_name))
        with open("Images7/" + file_name+".jpg", "wb") as f:
            f.write(response.content)

    def main(self):
        """ 调度中心，控制各个方法的执行并传递参数"""
        try:
            response = self.send_request(url=self.base_url)

            detail_url_list = self.parse_detail(response)
                ## 第二级for ： 处理所有详情页的请求
            for detail_url in detail_url_list:
                response = self.send_request(detail_url)
                image_url_list = self.parse_image(response)

                # #     ## 第三级for： 处理所有图片的请求
                file_name =str(random.randint(1,1000))
                for image_url in image_url_list:
                    response = self.send_request(image_url)

                    time.sleep(0.1)
                         # 保存图片数据
                    # self.save_image(response, file_name)
                    print(response.content)

        except Exception as e:
             print("[ERROR]: Bad Request {}".format(e) )


if __name__ == '__main__':
    spider = TiebaSpider()
    # t1 = threading.Thread(main())
    spider.main()

