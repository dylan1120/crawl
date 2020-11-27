import scrapy
from bs4 import BeautifulSoup


class FirstCrawler(scrapy.Spider):
    name = 'first'
    start_urls = ['https://koubei.16888.com/117870/']      
    
    # 網頁解析函式
    def parse(self, response):
        for car in response.xpath('/html/body/div/div/div/div[@class="mouth_box"]/dl'):   # 遍歷xpath
            advantage = car.xpath('dd/div[2]/p[1]/span[@class="show_dp f_r"]/text()').extract_first()
            disadvantage = car.xpath('dd/div[2]/p[2]/span[2]/text()').extract_first()
            sums = car.xpath('dd/div[2]/p[3]/span[2]/text()').extract_first()
            support_num = car.xpath('dd/div/div[@class="like f_r"]/a/text()').extract_first()
           
            print('優點：',advantage)
            print('缺點：',disadvantage)
            print('綜述：',sums)
            print('支援人數:',support_num)