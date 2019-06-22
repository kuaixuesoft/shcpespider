import scrapy
from ..items import ShcpeItem
import time
from datetime import datetime

class ShcpeSpider(scrapy.Spider):
    name = "shcpe"
    allowed_domains = ["shcpe.com.cn"]
    start_urls = [
        "http://www.shcpe.com.cn/list_15.html",
    ]

    def parse(self, response):

        Data_time = response.xpath("/html/body/section/div/div/section/div[1]/div[2]/dl[1]/dt/div/text()").extract()
        Data_time = Data_time[0].strip()
        print(Data_time) #2019年06月18日
        Data_time = datetime.strptime(Data_time, "%Y年%m月%d日")

        result = response.xpath("//span[@class='spanR']/text()").extract()

        shcpeitem = ShcpeItem()
        shcpeitem["Data_time"] = Data_time
        shcpeitem["Number_of_participants_in_ECDS_system"] = result[0]
        shcpeitem["The_number_of_online_members_of_trading_system"] = result[1]

        shcpeitem["Acceptance_sheets_today"] = float(result[2])
        shcpeitem["Acceptance_amounting_today"] = float(result[3])
        shcpeitem["Discounting_sheets_today"] = float(result[4])
        shcpeitem["Discounting_amounting_today"] = float(result[5])
        shcpeitem["Number_of_transactions_today"] = float(result[6])
        shcpeitem["Transaction_amounting_today"] = float(result[7])

        shcpeitem["Acceptance_sheets_year"] = float(result[8])
        shcpeitem["Acceptance_amounting_year"] = float(result[9])
        shcpeitem["Discounting_sheets_year"] = float(result[10])
        shcpeitem["Discounting_amounting_year"] = float(result[11])
        shcpeitem["Number_of_transactions_year"] = float(result[12])
        shcpeitem["Transaction_amounting_year"] = float(result[13])

        #print(shcpeitem["Transaction_amounting_year"])

        yield shcpeitem

