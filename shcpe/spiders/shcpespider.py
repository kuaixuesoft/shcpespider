import scrapy
from ..items import ShcpeItem

class ShcpeSpider(scrapy.Spider):
    name = "shcpe"
    allowed_domains = ["shcpe.com.cn"]
    start_urls = [
        "http://www.shcpe.com.cn/list_15.html",
    ]

    def parse(self, response):
        result = response.xpath("//span[@class='spanR']/text()").extract()

        shcpeitem = ShcpeItem()

        shcpeitem["Number_of_participants_in_ECDS_system"] = result[0]
        shcpeitem["The_number_of_online_members_of_trading_system"] = result[1]

        shcpeitem["Acceptance_sheets_today"] = result[2]
        shcpeitem["Acceptance_amounting_today"] = result[3]
        shcpeitem["Discounting_sheets_today"] = result[4]
        shcpeitem["Discounting_amounting_today"] = result[5]
        shcpeitem["Number_of_transactions_today"] = result[6]
        shcpeitem["Transaction_amounting_today"] = result[7]

        shcpeitem["Acceptance_sheets_year"] = result[8]
        shcpeitem["Acceptance_amounting_year"] = result[9]
        shcpeitem["Discounting_sheets_year"] = result[10]
        shcpeitem["Discounting_amounting_year"] = result[11]
        shcpeitem["Number_of_transactions_year"] = result[12]
        shcpeitem["Transaction_amounting_year"] = result[13]

        #print(shcpeitem["Transaction_amounting_year"])

        yield shcpeitem

