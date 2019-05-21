# -*- coding: utf-8 -*-
"""
Created on 2018/6/11

@author: xing yan
"""
import os
from sqlalchemy import create_engine, Table, Integer, Column, MetaData, column, DateTime
from sqlalchemy.sql import select, and_, or_, not_, text


engine = create_engine('oracle+cx_oracle://SIT_XM122_PRO:howbuy2015@192.168.220.119:1521/hbqa', echo=True)

metadata = MetaData(bind=engine)

conn = engine.connect()

HIGH_PRODUCT_BASIC_INFO = Table('HIGH_PRODUCT_BASIC_INFO', metadata, autoload=True)
FUND_BASIC_INFO = Table('FUND_BASIC_INFO', metadata, autoload=True)
TA_INFO = Table('TA_INFO', metadata, autoload=True)

a = '产品名称'

s = select([HIGH_PRODUCT_BASIC_INFO]).where(HIGH_PRODUCT_BASIC_INFO.c.fund_code=='PE0088')
s1 = select([FUND_BASIC_INFO])
s2 = select([TA_INFO])

result = conn.execute(s)
result1 = conn.execute(s1)
result2 = conn.execute(s2)
# print(result.fetchall())

s3 = text('select * from HIGH_PRODUCT_BASIC_INFO where fund_code =:fund_code')

result3 = conn.execute(s3, fund_code='PE0088')

for row in result3:
    print(row)
print("=======================")

# for row in result1:
#     print(row)
# print("=======================")
# for row in result2:
#     print(row)