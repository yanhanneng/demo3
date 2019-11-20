import requests

class TiebaSpider(object):
	def __init__(self):
		self.base_url = "http://tieba.baidu.com/f?"
		self.headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}

		self.tieba_name = input("请输入需要采集的贴吧名:")
		self.start_page = int(input("请输入需要采集的起始页:")) 
		self.end_page = int(input("请输入需要采集的结束页："))

	def send_requests(self,params):
		"""发送请求"""
		print("[INFL]:正在发送请求")
		response = requests.get(url=self.base_url,headers=self.headers,params=params)
		return response

	def save_data(self,response,fime_name):
		"""接收响应，保存数据"""
		html = response.content
		with open(fime_name,"wb")as f:
			f.write(html)

	def main(self):
		for page in range(self.start_page,self.end_page+1):
			pn = (page -1) * 50

			params = {"kw":self.tieba_name,"pn " : pn }

			try:
				response = self.send_requests(params)
				fime_name = self.tieba_name + str(page) + ".html"
				self.save_data(response,fime_name)

			except Exception as e:
				print("[ERROR]：请求处理失败，{}".formate(e))

		print("[INFO]:谢谢使用")

if __name__ == '__main__':
	spider=TiebaSpider()
	spider.main()

