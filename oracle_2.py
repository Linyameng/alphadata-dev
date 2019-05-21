# -*- coding: utf-8 -*-
"""
Created on 2018/6/11

@author: xing yan
"""
import os
from sqlalchemy import create_engine, Table, Integer, Column, MetaData, column, DateTime
from sqlalchemy.sql import select, and_, or_, not_, text
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from collections import OrderedDict

engine = create_engine('oracle+cx_oracle://SIT_XM122_PRO:howbuy2015@192.168.220.119:1521/hbqa', echo=True)

metadata = MetaData(bind=engine)

conn = engine.connect()

FUND_BASIC_INFO = Table('FUND_BASIC_INFO', metadata, autoload=True)
TA_INFO = Table('TA_INFO', metadata, autoload=True)

HIGH_PRODUCT_BASIC_INFO = Table('HIGH_PRODUCT_BASIC_INFO', metadata, autoload=True)
HIGH_PRODUCT_RISK_BOOK_STATE = Table('HIGH_PRODUCT_RISK_BOOK_STATE', metadata, autoload=True)
HIGH_PRODUCT_AGE_LIMIT = Table('HIGH_PRODUCT_AGE_LIMIT', metadata, autoload=True)
HIGH_PRODUCT_AGREEMENT_CONF = Table('HIGH_PRODUCT_AGREEMENT_CONF', metadata, autoload=True)
HIGH_PRODUCT_CONTROL_INFO = Table('HIGH_PRODUCT_CONTROL_INFO', metadata, autoload=True)
HIGH_PRODUCT_EXTEND_INFO = Table('HIGH_PRODUCT_EXTEND_INFO', metadata, autoload=True)
HIGH_PRODUCT_LOCK_INFO = Table('HIGH_PRODUCT_LOCK_INFO', metadata, autoload=True)
HIGH_PRODUCT_LOCK_WHITE_LIST = Table('HIGH_PRODUCT_LOCK_WHITE_LIST', metadata, autoload=True)
HIGH_PRODUCT_MANAGER_EMAIL = Table('HIGH_PRODUCT_MANAGER_EMAIL', metadata, autoload=True)
HIGH_PRODUCT_PAYREDEEM_CHANNEL = Table('HIGH_PRODUCT_PAYREDEEM_CHANNEL', metadata, autoload=True)

tables = (HIGH_PRODUCT_BASIC_INFO, HIGH_PRODUCT_RISK_BOOK_STATE, HIGH_PRODUCT_AGE_LIMIT,
          HIGH_PRODUCT_AGREEMENT_CONF, HIGH_PRODUCT_CONTROL_INFO, HIGH_PRODUCT_EXTEND_INFO,
          HIGH_PRODUCT_LOCK_INFO, HIGH_PRODUCT_LOCK_WHITE_LIST, HIGH_PRODUCT_MANAGER_EMAIL,
          HIGH_PRODUCT_PAYREDEEM_CHANNEL)

data_dic = OrderedDict([(tab.description, tab) for tab in tables])

with engine.begin() as connection:

    c = text('SELECT COMMENTS FROM USER_TAB_COMMENTS WHERE TABLE_NAME=:table_name')
    s = text('select * from {name} where fund_code=:fund_code')
    for t in data_dic.keys():
        tab_comment = connection.execute(c, table_name=t).fetchone()
        result = connection.execute(select([data_dic[t]]).where(data_dic[t].c.fund_code=='S27679'))
        data_dic[t] = {'tab_comment': tab_comment[0], 'tab_columns': result.keys(), 'data': result.fetchall()}

    print(data_dic)


# s = select([fund_limit])
# s1 = select([ta_info])
# r = conn.execute(s)
# r1 = conn.execute(s1)
#
# print(fund_limit)
# for row in r:
#     print(row)
# print("============================")
# for row1 in r1:
#     print(row1)


