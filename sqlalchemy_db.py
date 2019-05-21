# -*- coding: utf-8 -*-
"""
Created on 2018/6/11

@author: xing yan
"""
import os
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.sql import select
basedir = os.path.abspath(os.path.dirname(__file__))
engine = create_engine('sqlite:///' + os.path.join(basedir, 'test.sqlite'), echo=True)

metadata = MetaData()
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String),
              Column('fullname', String)
              )

addresses = Table('addresses', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('user_id', None, ForeignKey('users.id')),
                  Column('email_address', String, nullable=False)
                  )

metadata.create_all(engine)

ins = users.insert()
conn = engine.connect()
conn.execute(ins, name='wang wei', fullname='wang jia wei')
conn.execute(addresses.insert(), [
    {'user_id': 1, 'email_address': 'jack@admin.com'},
    {'user_id': 1, 'email_address': 'jack@test.com'},
    {'user_id': 2, 'email_address': 'jack@163.com'},
    {'user_id': 4, 'email_address': 'zhang@163.com'}
])

s = select([users])
print(str(s))
result = conn.execute(s)
print(result)

for row in result:
    print(row[users.c.name], row[users.c.fullname])

