# -*- coding: utf-8 -*-
"""
Created on 2018/5/25

@author: xing yan
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Length, Optional
from ..models import EnvironMapping


class EnvironMapForm(FlaskForm):
    tp_ip = StringField('后台IP', validators=[InputRequired()])
    tms_ip = StringField('中台IP', validators=[InputRequired()])
    user_prefix = StringField('DB用户前缀', validators=[InputRequired()])
    submit = SubmitField('提交')


class QueryFlaskForm(FlaskForm):

    def __init__(self, *args, **kwargs):
        super(QueryFlaskForm, self).__init__(*args, **kwargs)
        self.test_env.choices = [(env.tms_ip, env.tms_ip) for env in
                                 EnvironMapping.query.order_by(EnvironMapping.id).all()]


class FundCodeForm(QueryFlaskForm):
    fund_code = StringField('FundCode', validators=[InputRequired()])
    test_env = SelectField('选择环境')
    submit = SubmitField('查询')


class DealOrderForm(QueryFlaskForm):
    deal_no = StringField('DealNo', validators=[InputRequired()])
    test_env = SelectField('选择环境')
    submit = SubmitField('查询')


class CustInfoForm(QueryFlaskForm):
    cust_no = StringField('CustNo')
    test_env = SelectField('测试环境')
    submit = SubmitField('查询')


class QueryBatchFlowForm(QueryFlaskForm):
    trade_dt = StringField('TRADE DT')
    sys_code = StringField('SYS CODE')
    test_env = SelectField('选择环境')
    submit = SubmitField('查询')


class QueryCustBookForm(QueryFlaskForm):
    cust_no = StringField('CustNo')
    fund_code = StringField('FundCode')
    test_env = SelectField('选择环境')
    submit = SubmitField('查询')


class SQLAreaEditForm(QueryFlaskForm):
    sql_area = TextAreaField("Sql语句", validators=[InputRequired(), Length(max=5000)], render_kw={"rows": 8})
    schema = SelectField('Schema', choices=[('ORDERS1', 'ORDERS1'), ('BATCH', 'BATCH'), ('PRO', 'PRO'),
                                            ('ZHZX', 'ZHZX'), ('ORD', 'ORD'), ('ESIGN', 'ESIGN')])
    test_env = SelectField('选择环境')
    submit = SubmitField('执行')


class QueryDatabaseDictForm(QueryFlaskForm):
    table_name = StringField("表名称")
    comments = StringField("表注释")
    schema = SelectField('Schema', choices=[('ORDERS1', 'ORDERS1'), ('BATCH', 'BATCH'), ('PRO', 'PRO'),
                                            ('ZHZX', 'ZHZX'), ('ORD', 'ORD'), ('ESIGN', 'ESIGN')])
    test_env = SelectField('选择环境')
    submit = SubmitField('执行')


class RandomGenerateCustomForm(FlaskForm):
    cust_id = StringField("身份证ID", validators=[Optional(), Length(15, 18, message="身份证ID最大限制15到18位字符串.")])
    random_id_btn = SubmitField("随机生成")

    cust_name = StringField("客户姓名", validators=[Optional(), Length(1, 10, message="客户姓名最大限制10位.")])
    random_name_btn = SubmitField("随机生成")

    phone_number = StringField("手机号码", validators=[Optional(), Length(1, 13, message="手机号码最大限制13位")])
    random_number_btn = SubmitField("随机生成")

    bank_number = StringField("银行卡号", validators=[Optional(), Length(1, 20, message="银行卡卡号最大限制20位.")])
    bank_end_number = StringField("尾号", validators=[Optional(), Length(1, 4, message="银行卡尾号最多输入4位.")], default='111')
    random_bank_number_btn = SubmitField("随机生成")

    count = IntegerField("生成数量", validators=[InputRequired()], default=1)

    all_generate_btn = SubmitField("全部随机生成")
    submit = SubmitField("提交")
