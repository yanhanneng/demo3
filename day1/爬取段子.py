# url= https://www.neihan8.com/article//index_2.html   网页URL
# //div[@class="text-column-item box box-790"]/h3/a/@href  每个段子URL
# //div[@class="text-column-item box box-790"]/h3/a/text()   段子的标题
# //div[@class="detail"]/p/text()   文本获取

import re,time

import requests,threading
from lxml import etree

class NeihanSpider(threading.Thread):
    def __init__(self,num):
        self.base_url = "https://www.neihan8.com/article//index_%d.html"
        self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        self.content_pattern = re.compile("\s|<.*?>|&.*?;")

        super(NeihanSpider, self).__init__()
        # 定义属性保存 num 值
        self.num = num

    def send_requests(self,url):
        print("[INFO]: send request [{}] <{}>".format("GET", url))
        response = requests.get(url,headers=self.headers)
        return response

    def parse_response(self, response):   #URL提取
        html = response.content.decode()
        html_down = etree.HTML(html)
        url_list = html_down.xpath("//div[@class='text-column-item box box-790']/h3/a/@href")
        return url_list

    def text_respinse(self,response):  #文本提取
        html = response.content.decode()
        html_down = etree.HTML(html)
        content_list = html_down.xpath("//div[@class='detail']/p/text() ")
        return content_list

    def run(self):
        for i in range(5):

    # self.name 是继承⾃ ⽗类Thread 的， ⽤于保存线程的名称
            time.sleep(0.5)

    def save_data(self, content_list):
        with open("duanzi.txt", "a") as f:
            # f.write("第{}页:\n".format(self.page))
            for content in content_list:
                # 清洗数据
                new_content = self.content_pattern.sub("", content)
                f.write(new_content)
                f.write("\n\n")

    def main(self):
        while True:
            try:
                nNum = int(input(u"请输入需要下载的页数: "))
                if nNum > 0:
                    break
            except ValueError:
                print(u"请输入数字。")
                continue
        for i in range(nNum):
            bases_url = self.base_url %(i+1)
            try:
                response = self.send_requests(bases_url)
                url_list = self.parse_response(response)
                for xh_url in url_list:
                    xho_url = "https://www.neihan8.com"+xh_url
                    response = self.send_requests(url=xho_url)
                    time.sleep(0.01)
                    content_list = self.text_respinse(response)
                    self.save_data(content_list)

            except Exception as e:
                print("[ERROR]：请求处理失败，{}"%format(e))

        print("[INFO]:谢谢使用")


if __name__ == '__main__':
    mythread = NeihanSpider(10)
    # spider = NeihanSpider()
    mythread.start()
    mythread.main()
