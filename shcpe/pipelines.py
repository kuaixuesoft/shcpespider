# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from datetime import datetime

class ShcpePipeline(object):

    def __init__(self):
        # connection database
        self.connect = pymysql.connect('localhost','root','root','shcpe',use_unicode=True,charset='utf8')
        # get cursor
        self.cursor = self.connect.cursor()
        print("connecting mysql success!")
 
    def process_item(self, item, spider):
        print("start writing datas")
        print(item)
        try:
            # insert data
            sqlstr = '''
            insert into statistic(
                check_time,
                number_of_participants_in_ecds_system,
                the_number_of_online_members_of_trading_system,
                acceptance_sheets_today,
                acceptance_amounting_today,
                discounting_sheets_today,
                discounting_amounting_today,
                number_of_transactions_today,
                transaction_amounting_today,
                acceptance_sheets_year,
                acceptance_amounting_year,
                discounting_sheets_year,
                discounting_amounting_year,
                number_of_transactions_year,
                transaction_amounting_year
            ) VALUES("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")
            '''.format(
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                item['Number_of_participants_in_ECDS_system'],
                item['The_number_of_online_members_of_trading_system'],
                item['Acceptance_sheets_today'],
                item['Acceptance_amounting_today'],
                item['Discounting_sheets_today'],
                item['Discounting_amounting_today'],
                item['Number_of_transactions_today'],
                item['Transaction_amounting_today'],
                item['Acceptance_sheets_year'],
                item['Acceptance_amounting_year'],
                item['Discounting_sheets_year'],
                item['Discounting_amounting_year'],
                item['Number_of_transactions_year'],
                item['Transaction_amounting_year']
            )
            self.cursor.execute(sqlstr)
            self.connect.commit()
            self.connect.close()
        except Exception as error:
            # print error
            print(error)
            return item

