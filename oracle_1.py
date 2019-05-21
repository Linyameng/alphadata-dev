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

Base = automap_base()
engine = create_engine('oracle+cx_oracle://SIT_XM122_PRO:howbuy2015@192.168.220.119:1521/hbqa', echo=True)

# metadata = MetaData(bind=engine)
#
# conn = engine.connect()
#
# HIGH_PRODUCT_BASIC_INFO = Table('HIGH_PRODUCT_BASIC_INFO', metadata, autoload=True)
# FUND_BASIC_INFO = Table('FUND_BASIC_INFO', metadata, autoload=True)
# TA_INFO = Table('TA_INFO', metadata, autoload=True)
Base.prepare(engine, reflect=True)

# table = Base.metadata.tables

conn = engine.connect()

fund_limit = Base.classes.fund_limit
ta_info = Base.classes.ta_info


with conn.begin() as trans:
    result = conn.execute(select[ta_info])
    for row in result:
        print(row)


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


