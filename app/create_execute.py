# -*- coding: utf-8 -*-
"""
Created on 2018/5/31

@author: xing yan
"""
from sqlalchemy import create_engine, Table
from sqlalchemy import MetaData
from sqlalchemy.sql import text
from sqlalchemy.exc import NoSuchTableError
from collections import OrderedDict


class OracleEngine:
    """create oracle engine.
    oracle_tms_dict = {'drivername': 'oracle+cx_oracle', 'host': '192.168.220.119',
                       'database': 'hbqa', 'password': 'howbuy2016', 'port': 1521}
    oracle_tp_dict = {'drivername': 'oracle+cx_oracle', 'host': '192.168.220.126',
                      'password': 'howbuy2016', 'database': 'hbqa', 'port': 1521}
    """

    oracle_url = 'oracle+cx_oracle://{username}:{password}@{dialect}'

    query_all_tab_sql = "SELECT * from {tab_name}"
    query_sql = "SELECT * from {tab_name} where {column_name} like :column_name"
    tab_comments_sql = "SELECT COMMENTS FROM USER_TAB_COMMENTS WHERE TABLE_NAME like :tab_name"

    def __init__(self, username, db_info):
        self.engine = create_engine(self.oracle_url.format(username=username, password=db_info.db_password, dialect=db_info.tms_dsn))
        self.metadata = MetaData(bind=self.engine)

    def tab_metadata(self, tables):
        tabs = []
        for tab in tables:
            try:
                tabs.append(Table(tab, self.metadata, autoload=True))
            except NoSuchTableError:
                continue
        return OrderedDict([(tab.description, tab) for tab in tabs])

    def execute(self, sql, **kwargs):

        with self.engine.begin() as connect:
            return connect.execute(text(sql), **kwargs)

    def with_execute(self, tables, value=None):

        metadata = self.tab_metadata(tables.keys())

        tables_data = []

        with self.engine.begin() as connect:
            for tab in metadata.keys():
                tab_comment = self.get_tab_comment(tab)
                if tables[tab] is None or value is None:
                    result = connect.execute(text(self.query_all_tab_sql.format(tab_name=tab)))
                else:
                    result = connect.execute(text(self.query_sql.format(tab_name=tab, column_name=tables[tab])),
                                             column_name=value if value != '' else '%%')
                col_comments = self.get_col_comments(result, tab=tab)
                tab_map = OrderedDict(tab_name=tab, tab_comment=tab_comment, columns=result.keys(),
                                      col_comments=col_comments, data=result.fetchall())
                tables_data.append(tab_map)
            return tables_data

    def sql_execute(self, sql, **kwargs):
        tables_data = []
        with self.engine.begin() as connect:
            result = connect.execute(text(sql), kwargs)
            """ col_comments = self.get_col_comments(result)"""
            tables_data.append(OrderedDict(columns=result.keys(), data=result.fetchall()))
            return tables_data

    def many_execute(self, tables, **kwargs):

        metadata = self.tab_metadata(tables)

        tables_data = []

        with self.engine.begin() as connect:
            for tab in metadata:
                sql = self.sql_format(tab, op='LIKE')
                result = connect.execute(text(sql), **kwargs)
                tables_data.append(OrderedDict(tab_name=tab, columns=result.keys(), data=result.fetchall()))
            return tables_data

    def comments_execute(self, tables, **kwargs):

        self.tab_metadata(tables.keys())

        tables_data = []

        with self.engine.begin() as connect:
            for tab in tables.keys():
                sql = self.sql_format(tables, tab, op='LIKE')
                result = connect.execute(text(sql), **kwargs)
                tables_data.append(OrderedDict(tab_name=tab, columns=result.keys(), data=result.fetchall()))
            return tables_data

    def get_tab_comment(self, tab):
        result = self.execute(self.tab_comments_sql, tab_name=tab.upper()).fetchone()
        return result[0]

    def get_col_comments(self, result, tab=None):
        return self._query_col_comments(result.keys(), tab=tab)

    @staticmethod
    def sql_format(tables: dict, tab, op='=', key='AND'):

        sql = "SELECT * FROM {tab_name} {field}"

        if tables.get(tab) is None:
            return sql.format(table_name=tab, where_field='')

        col = tables.get(tab)
        col_part_sql = ' 1=1 '

        if isinstance(col, str):
            col_part_sql = " {col} {op} :{value} ".format(col=col, op=op, value=col.lower())
        if isinstance(col, list):
            col_part = []
            for col in tables.get(tab):
                col_part.append(" {col} {op} :{value} ".format(col=col, op=op, value=col.lower()))
            col_part_sql = key.join(col_part)

        field_sql = 'WHERE {part_sql}'.format(part_sql=col_part_sql)

        return sql.format(tab_name=tab, field=field_sql)

    def _query_col_comments(self, cols, tab=None):

        all_col_comments_sql = "SELECT COMMENTS FROM USER_COL_COMMENTS WHERE COLUMN_NAME = :col_name and COMMENTS is not NULL "

        user_col_comments_sql = "SELECT COMMENTS FROM USER_COL_COMMENTS WHERE TABLE_NAME = :tab_name " \
                                "AND COLUMN_NAME = :col_name "

        with self.engine.begin() as connect:
            col_comments = []
            for col in cols:
                if tab is None:

                    result = connect.execute(text(all_col_comments_sql), col_name=col.upper())
                else:
                    result = connect.execute(text(user_col_comments_sql), tab_name=tab.upper(), col_name=col.upper())
                col_comment = result.fetchone()[0]
                if col_comment is not None:
                    col_comment = col_comment[:35]
                else:
                    col_comment = 'null'
                col_comments.append(col_comment)
            return col_comments

    def update_business_batch_flow(self, trade_dt, sys_code):
        batch_sql = "UPDATE business_batch_flow f SET f.batch_stat='2' WHERE f.trade_dt =:trade_dt AND f.sys_code =:sys_code"

        with self.engine.begin() as connect:
            connect.execute(text(batch_sql), trade_dt=trade_dt, sys_code=sys_code)


if __name__ == '__main__':
    """
        tables = {
            'USER_TAB_COMMENTS': ['TABLE_NAME', 'COMMENTS'],
            'USER_COL_COMMENTS': ['TABLE_NAME', 'COLUMN_NAME', 'COMMENTS']
        }
        table_info = {'table':'USER_TAB_COMMENTS', 'column':['TABLE_NAME', 'COMMENTS'], 'key':'or'}
    SELECT * FROM USER_TAB_COMMENTS T WHERE T.TABLE_NAME LIKE '' OR T.COMMENTS LIKE '';
    SELECT * FROM USER_COL_COMMENTS C WHERE C.TABLE_NAME LIKE '' OR C.COLUMN_NAME OR C.COMMENTS LIKE '';
    """
    table_info = {'table_name': 'USER_TAB_COMMENTS', 'columns': ['TABLE_NAME', 'COMMENTS'], 'key': 'or'}


