# -*- coding: utf-8 -*-
"""
Created on 2018/5/31

@author: xing yan
"""
from sqlalchemy import create_engine, Table
from sqlalchemy import MetaData
from sqlalchemy.sql import text, select, and_, or_, not_
from sqlalchemy.exc import NoSuchTableError
from collections import OrderedDict


table_name = 'cm_blacklist_direct'

engine = create_engine('oracle+cx_oracle://JKCS_XM109_BATCH:howbuy2015@192.168.220.119:1521/hbqa', echo=True)
metadata = MetaData(bind=engine)
# tp_acct_deal_rec = Table('tp_acct_deal_rec', metadata, autoload=True)
# ac_tx_hbone = Table('ac_tx_hbone', metadata, autoload=True)
#
# s = select([tp_acct_deal_rec, ac_tx_hbone]).where(and_(tp_acct_deal_rec.c.hbone_no == ac_tx_hbone.c.hbone_no, tp_acct_deal_rec.c.tx_code == '520019'))
# result = engine.execute(s)

business_batch_flow = Table('business_batch_flow', metadata, autoload=True)

batch_sql = "UPDATE business_batch_flow f SET f.batch_stat='2' WHERE f.trade_dt =:trade_dt AND f.sys_code =:sys_code"

result = engine.execute(text(batch_sql), trade_dt='20180927', sys_code='92')

print(result)

result.close()
