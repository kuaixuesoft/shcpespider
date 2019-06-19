# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ShcpeItem(scrapy.Item):


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
