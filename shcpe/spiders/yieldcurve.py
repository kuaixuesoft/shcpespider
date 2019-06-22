import scrapy
from ..items import YieldCurveItem

import time
import pandas as pd

class YieldCurveSpider(scrapy.Spider):
    name = "YieldCurve"
    allowed_domains = ["shcpe.com.cn"]
    # start_urls = [
    #     "http://www.shcpe.com.cn/index_132_lcid_1_date_2019-06-18.html",
    # ]
    start_urls = []
    for d in pd.date_range('6/1/2018','12/31/2018',normalize=True):
        start_urls.append("http://www.shcpe.com.cn/index_132_lcid_1_date_{}.html".format(str(d).split(' ')[0]))
    print(start_urls)

    def parse(self, response):

        result = response.xpath("//td/text()").extract()
        result2 = response.xpath("//input[@name='rateDate']/@value").extract()
        Data_time = result2[0].strip()
        print('--------------')
        print(result)

        yieldcurveItem = YieldCurveItem()
        yieldcurveItem["Data_time"] = Data_time
        '''['1D',
         '2.5485',
         '2.5487',
         '7D',
         '2.5524',
         '2.5537',
         '1M',
         '3.1115',
         '3.1198',
         '3M',
         '3.1426',
         '3.1681',
         '6M',
         '3.1500',
         '3.2015',
         '9M',
         '3.2274',
         '3.3093',
         '1Y',
         '3.2118',
         '3.3199']'''
        yieldcurveItem["Interest_Rate_1D"] = result[1]
        yieldcurveItem["Rate_of_eturn_1D"] = result[2]

        yieldcurveItem["Interest_Rate_7D"] = result[4]
        yieldcurveItem["Rate_of_eturn_7D"] = result[5]

        yieldcurveItem["Interest_Rate_1M"] = result[7]
        yieldcurveItem["Rate_of_eturn_1M"] = result[8]

        yieldcurveItem["Interest_Rate_3M"] = result[10]
        yieldcurveItem["Rate_of_eturn_3M"] = result[11]

        yieldcurveItem["Interest_Rate_6M"] = result[13]
        yieldcurveItem["Rate_of_eturn_6M"] = result[14]

        yieldcurveItem["Interest_Rate_9M"] = result[16]
        yieldcurveItem["Rate_of_eturn_9M"] = result[17]

        yieldcurveItem["Interest_Rate_1Y"] = result[19]
        yieldcurveItem["Rate_of_eturn_1Y"] = result[20]

        #print(shcpeitem["Transaction_amounting_year"])

        print(yieldcurveItem)

        yield yieldcurveItem

