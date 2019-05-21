# -*- coding: utf-8 -*-
"""
Created on 2018/5/25

@author: xing yan
"""
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SubmitField, SelectField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Length, Optional ,ValidationError
from ..models import EnvironMapping ,User


class EnvironMapForm(FlaskForm):
    user_prefix = StringField('数据库实例', validators=[InputRequired()])
    tms_url = StringField("数据库URL", default="192.168.220.119:1521/hbqa")
    db_password = StringField("数据库密码", default="howbuy2015")
    submit = SubmitField('提交')

class EnvRoleRction(FlaskForm):
    user_prefix = StringField('邮箱', validators=[InputRequired()])
    tms_url = StringField("用户名", validators=[InputRequired()])
    db_password = StringField("权限", validators=[InputRequired()])
    submit = SubmitField('提交')

class QueryFlaskForm(FlaskForm):

    def __init__(self, *args, **kwargs):
        super(QueryFlaskForm, self).__init__(*args, **kwargs)
        self.test_env.choices = [(env.tms_ip, env.tms_ip) for env in
                                 EnvironMapping.query.order_by(EnvironMapping.id).all()]

class QueryUserPrefix(FlaskForm):

    def __init__(self, *args, **kwargs):
        super(QueryUserPrefix, self).__init__(*args, **kwargs)
        self.userPrefix.choices = [(env.user_prefix,env.user_prefix) for env in
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
    schema = SelectField('Schema', choices=[('TRADE', 'TRADE'),('ORDERS1', 'ORDERS1')])
    test_env = SelectField('选择环境')
    submit = SubmitField('执行')

class QuerySql(QueryUserPrefix):
    sql_area = TextAreaField("Sql语句", validators=[InputRequired(), Length(max=5000)], render_kw={"rows": 8})
    Desc = TextAreaField("语句描述", validators=[Length(max=5000)], render_kw={"rows": 1})
    #schema = SelectField('Schema', choices=[('TRADE', 'TRADE'),('ORDERS1', 'ORDERS1')])
    userPrefix = SelectField('选择实例')
    save = SubmitField("SQL保存")
    submit = SubmitField('执行')

class QueryDatabaseDictForm(QueryFlaskForm):
    table_name = StringField("表名称")
    comments = StringField("表注释")
    schema = SelectField('Schema', choices=[('ORDERS1', 'ORDERS1'), ('BATCH', 'BATCH'), ('PRO', 'PRO'),
                                            ('ZHZX', 'ZHZX'), ('ORD', 'ORD'), ('ESIGN', 'ESIGN')])
    test_env = SelectField('选择环境')
    submit = SubmitField('执行')


class BusinessBatchFlowForm(FlaskForm):
    trade_dt = StringField("TA日期", validators=[InputRequired(), Length(8, 8, message="只能输入8位字符，如20181009")])
    sys_code = SelectField('选择业务类型', choices=[('92', '群济批处理'), ('91', '公募批处理'), ('93', '高端公募批处理'), ('94', 'TP私募批处理')])
    test_env = SelectField('选择环境', choices=[('192.168.221.220', '192.168.221.220')])
    submit = SubmitField('置完成')


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


class QuickAddAccountForm(QueryFlaskForm):
    cust_id = StringField("身份证ID", validators=[Optional(), Length(15, 18, message="身份证ID最大限制15到18位字符串.")])
    random_id_btn = SubmitField("随机生成")

    cust_name = StringField("客户姓名", validators=[Optional(), Length(1, 10, message="客户姓名最大限制10位.")])
    random_name_btn = SubmitField("随机生成")

    phone_number = StringField("手机号码", validators=[Optional(), Length(1, 13, message="手机号码最大限制13位")])
    random_number_btn = SubmitField("随机生成")

    bank_number = StringField("银行卡号", validators=[Optional(), Length(1, 20, message="银行卡卡号最大限制20位.")])
    bank_end_number = StringField("尾号", validators=[Optional(), Length(1, 4, message="银行卡尾号最多输入4位.")], default='111')
    random_bank_number_btn = SubmitField("随机生成")

    # count = IntegerField("生成数量", validators=[InputRequired()], default=1)

    test_env = SelectField('选择环境')

    all_generate_btn = SubmitField("全部随机生成")

    submit = SubmitField("快速开户")