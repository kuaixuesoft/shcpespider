# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ShcpeItem(scrapy.Item):

    Data_time = scrapy.Field()

    Number_of_participants_in_ECDS_system = scrapy.Field()
    The_number_of_online_members_of_trading_system = scrapy.Field()

    Acceptance_sheets_today = scrapy.Field()
    Acceptance_amounting_today = scrapy.Field()
    Discounting_sheets_today = scrapy.Field()
    Discounting_amounting_today = scrapy.Field()
    Number_of_transactions_today = scrapy.Field()
    Transaction_amounting_today = scrapy.Field()

    Acceptance_sheets_year = scrapy.Field()
    Acceptance_amounting_year = scrapy.Field()
    Discounting_sheets_year = scrapy.Field()
    Discounting_amounting_year = scrapy.Field()
    Number_of_transactions_year = scrapy.Field()
    Transaction_amounting_year = scrapy.Field()



class YieldCurveItem(scrapy.Item):

    Data_time = scrapy.Field()

    Interest_Rate_1D = scrapy.Field()
    Rate_of_eturn_1D = scrapy.Field()

    Interest_Rate_7D = scrapy.Field()
    Rate_of_eturn_7D = scrapy.Field()

    Interest_Rate_1M = scrapy.Field()
    Rate_of_eturn_1M = scrapy.Field()

    Interest_Rate_3M = scrapy.Field()
    Rate_of_eturn_3M = scrapy.Field()

    Interest_Rate_6M = scrapy.Field()
    Rate_of_eturn_6M = scrapy.Field()

    Interest_Rate_9M = scrapy.Field()
    Rate_of_eturn_9M = scrapy.Field()

    Interest_Rate_1Y = scrapy.Field()
    Rate_of_eturn_1Y = scrapy.Field()