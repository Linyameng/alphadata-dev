# -*- coding: utf-8 -*-
"""
Created on 2018/5/24

@author: xing yan
"""
from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_required

from . import core
from .. import db
from ..models import EnvironMapping, PageView ,SaveSql
from .forms import (FundCodeForm, DealOrderForm, EnvironMapForm, CustInfoForm, SQLAreaEditForm, QueryCustBookForm,
                    QueryDatabaseDictForm, RandomGenerateCustomForm, BusinessBatchFlowForm, QuickAddAccountForm,QuerySql)

from ..create_execute import OracleEngine
from . import exts
from .utils import Fabricate
from .client import BaseHttpClient
import datetime,sys
from collections import OrderedDict


@core.before_request
def query_page_view():
    page_view = PageView.query.filter_by(view=request.endpoint).first()
    if page_view is None:
        page_view = PageView(view=request.endpoint)
        db.session.add(page_view)
    if request.method == 'POST':
        page_view.pv += 1
        db.session.add(page_view)
    g.page_view = page_view


@core.context_processor
def inject_template_extras():
    return dict(page_view=g.page_view)


@core.route('/envs', methods=('GET', 'POST'))
def test_env():
    """
    维护测环境信息
    :return:
    """
    form = EnvironMapForm()
    envs = EnvironMapping.query.all()
    if form.validate_on_submit():
        userprefix = form.user_prefix.data
        SQLStatements = EnvironMapping.query.filter_by(user_prefix=userprefix).first()
        if SQLStatements is None:
            env_info = EnvironMapping(
                                      user_prefix=form.user_prefix.data,
                                      tms_dsn=form.tms_url.data,
                                      db_password=form.db_password.data)
            db.session.add(env_info)
            flash("添加成功. {ip}".format(ip=env_info))
            return redirect(url_for('.test_env'))
        else:
            flash("数据库实例重复")
            return redirect(url_for('.test_env'))
    return render_template('core/edit_environ.html', form=form, tab_data=envs)


@core.route('/queryfundcode', methods=('GET', 'POST'))
def query_fund_code():
    """
    根据产品代码查询产品中心相关表
    :return:
    """
    tables = {
        'fund_basic_info': 'fund_code',
        'high_product_basic_info': 'fund_code',
        'fund_limit': 'fund_code',
        'fund_fee_rate': 'fund_code',
        'fund_discount': 'fund_code',
        'acti_rate_discount_cfg': 'fund_code',
        'acti_rate_discount_org_cfg': 'fund_code',
        'product_appointment_info': 'product_id',
        'fund_nav_status': 'fund_code',
        'high_product_control_info': 'fund_code',
        'high_product_age_limit': 'fund_code',
        'high_product_agreement_conf': 'fund_code',
        'high_product_payredeem_channel': 'fund_code',
        'high_product_extend_info': 'fund_code',
        'high_product_lock_info': 'fund_code',
        'high_product_lock_white_list': 'fund_code',
        'high_product_trade_limit_dtl': 'fund_code',
        'fund_tx_open_cfg': 'product_id'
    }

    form = FundCodeForm()
    tabs_data = []

    if form.validate_on_submit():
        db_info = EnvironMapping.query.filter_by(tms_ip=form.test_env.data).first()
        engine = OracleEngine(username='PRO', db_info=db_info)
        tabs_data = engine.with_execute(tables, form.fund_code.data)

    return render_template('core/queryfundcode.html', form=form, tabs_data=tabs_data)


@core.route('/querydealorder', methods=('GET', 'POST'))
def query_deal_order():
    """
    根据订单号，查询订单相关表
    :return:
    """

    tables = {
        'deal_order': 'deal_no',
        'high_deal_order_dtl': 'deal_no',
        'deal_order_extend': 'deal_no',
        'payment_order': 'deal_no',
        'simu_fund_check_order': 'deal_no'
    }

    form = DealOrderForm()

    tabs_data = []
    if form.validate_on_submit():
        db_info = EnvironMapping.query.filter_by(tms_ip=form.test_env.data).first()
        engine = OracleEngine(username='ORDERS1', db_info=db_info)
        tabs_data = engine.with_execute(tables, form.deal_no.data)

    return render_template('core/querydealorder.html', form=form, tabs_data=tabs_data)


@core.route('/querycustinfo', methods=('GET', 'POST'))
def query_cust_info():
    """
    查询测试环境客户信息
    :return:
    """
    form = CustInfoForm()
    tabs_data = []
    if form.validate_on_submit():
        db_info = EnvironMapping.query.filter_by(tms_ip=form.test_env.data).first()
        engine = OracleEngine('ZHZX', db_info=db_info)
        cust_no = form.cust_no.data
        tabs_data = engine.sql_execute(exts.query_cust_info_sql, cust_no=cust_no if cust_no != '' else '%%')
    return render_template('core/querycustinfo.html', form=form, tabs_data=tabs_data)


@core.route('/querynotifyorder', methods=('GET', 'POST'))
def query_notify_deal_order():
    """
    查询未通知的订单
    :return:
    """
    form = FundCodeForm()
    tabs_data = []
    if form.validate_on_submit():
        db_info = EnvironMapping.query.filter_by(tms_ip=form.test_env.data).first()
        engine = OracleEngine('ORDERS1', db_info=db_info)
        tabs_data = engine.sql_execute(exts.query_notify_deal_order_sql, fund_code=form.fund_code.data)
    return render_template('core/querynotifyorder.html', form=form, tabs_data=tabs_data)


@core.route('/querycustbook', methods=('GET', 'POST'))
def query_cust_book():
    """
    查询客户持仓信息
    :return:
    """

    tables = {
        'cust_books': 'tx_acct_no',
        'sub_cust_books': 'tx_acct_no',
        'cust_books_dtl': 'tx_acct_no',
    }

    form = QueryCustBookForm()

    tabs_data = []
    if form.validate_on_submit():
        db_info = EnvironMapping.query.filter_by(tms_ip=form.test_env.data).first()
        engine = OracleEngine(username='ORDERS1', db_info=db_info)
        tabs_data = engine.with_execute(tables, form.cust_no.data)

    return render_template('core/querycustbook.html', form=form, tabs_data=tabs_data)


@core.route('/sqlline', methods=('GET', 'POST'))
@login_required
def sql_area_execute():
    """
    在线执行sql
    :return:
    """
    
    form = QuerySql()
    tabs_data = OrderedDict()
    username = current_user.username
    hint = ''
    if form.validate_on_submit():
        if form.save.data:
            sql_area = form.sql_area.data
            SQLStatements = SaveSql.query.filter_by(SQL_statements=sql_area).first()
            if SQLStatements is None:
                save_sql = SaveSql(SQL_statements=form.sql_area.data,
                                   instance=form.userPrefix.data,
                                   Desc =form.Desc.data,
                                   creator=username,
                                   CREATE_DATE=datetime.datetime.now())
                db.session.add(save_sql)
                flash("添加成功. {ip}".format(ip=save_sql))
            else:
                flash("SQL语句重复")
                return redirect(url_for('.sql_area_execute'))
        if form.submit.data:
            db_info = EnvironMapping.query.filter_by(user_prefix=form.userPrefix.data).first()
            engine = OracleEngine(username=form.userPrefix.data, db_info=db_info)
            try:
                if "update" in form.sql_area.data or "delete" in form.sql_area.data:
                    flash("暂不支持修改和删除")
                    return redirect(url_for('.sql_area_execute'))
                else:
                    if "where" in form.sql_area.data:
                        tabs_data = engine.sql_execute(form.sql_area.data)
                    else:
                        tabs_data = engine.sql_execute(form.sql_area.data+" where rownum <= 10")
                        hint ='a'
            except Exception as e:
                flash("执行sql错误: {msg}".format(msg=e))
                return redirect(url_for('.sql_area_execute'))
    return render_template('core/sqlarea.html', form=form, tabs_data=tabs_data, hint =hint)

@core.route('/quickSql', methods=('GET', 'POST'))
@login_required
def quick_sql():
    """
    SQL保持查询记录
    :return:
    """
    tabs_data = SaveSql.query.all()
    print(tabs_data)
    return render_template('core/sqlquery.html', tabs_data=tabs_data)


@core.route('/datadict', methods=('GET', 'POST'))
def query_data_dict():
    """
    查询数据库字典
    :return:
    """

    tables = OrderedDict({'user_tab_comments': ['table_name', 'comments']})

    form = QueryDatabaseDictForm()
    tabs_data = []
    if form.validate_on_submit():
        db_info = EnvironMapping.query.filter_by(tms_ip=form.test_env.data).first()
        engine = OracleEngine(username=form.schema.data, db_info=db_info)

        table_name, comments = form.table_name.data, form.comments.data

        if not comments:
            comments = '%%'

        if table_name:
            tables.update({'user_col_comments': ['table_name', 'comments']})
        else:
            table_name = '%%'

        tabs_data = engine.comments_execute(tables, **dict(table_name=table_name, comments=comments))

    return render_template('core/datadict.html', form=form, tabs_data=tabs_data)


@core.route('/queryhbone', methods=('GET', 'POST'))
def query_custno_or_hbone():
    form = CustInfoForm

    tabs_data = []
    if form.validate_on_submit():
        db_info = EnvironMapping.query.filter_by(tms_ip=form.test_env.data).first()
        engine = OracleEngine(username='ZHZX', db_info=db_info)

        tables = [
            {'table': 'AC_TX_HBONE', 'columns': ['tx_acct_no']}
        ]

        tabs_data = engine.sql_execute(exts.query_cust_info_sql)


@core.route('/forge-cust', methods=('GET', 'POST'))
def forge_cust_info():
    """
    在线生成客户信息，包含身份证、姓名、手机号、银行卡号等信息
    :return:
    """
    form = RandomGenerateCustomForm()
    rand_data = []

    if form.validate_on_submit():
        fabr = Fabricate()
        if form.random_id_btn.data:
            form.cust_id.data = fabr.cust_id()

        if form.random_name_btn.data:
            form.cust_name.data = fabr.cust_name()

        if form.random_number_btn.data:
            form.phone_number.data = fabr.phone_number()

        if form.random_bank_number_btn.data:
            form.bank_number.data = fabr.bank_number(end_number=form.bank_end_number.data)

        if form.all_generate_btn.data:
            cust_id, cust_name, phone_number, bank_number = (fabr.cust_id(), fabr.cust_name(), fabr.phone_number(),
                                                             fabr.bank_number(end_number=form.bank_end_number.data))
            form.cust_id.data = cust_id
            form.cust_name.data = cust_name
            form.phone_number.data = phone_number
            form.bank_number.data = bank_number
            rand_data.append((cust_id, cust_name, phone_number, bank_number))

        if form.submit.data:
            count = 1
            try:
                count = form.count.data
            except ValueError:
                pass
            cust_id = form.cust_id.data
            cust_name = form.cust_name.data
            phone_number = form.phone_number.data
            bank_number = form.bank_number.data
            rand_data.append((cust_id, cust_name, phone_number, bank_number))
            if count > 1:
                rand_data = fabr.get_more_generate(count, end_number=form.bank_end_number.data)

    return render_template('core/forge_cust_info.html', form=form, rand_data=rand_data)


@core.route('/update-batch-flow', methods=('GET', 'POST'))
def update_batch_flow():
    """
    手动置批处理节点为完成状态
    """
    form = BusinessBatchFlowForm()

    if form.validate_on_submit():
        db_info = EnvironMapping.query.filter_by(tms_ip=form.test_env.data).first()
        engine = OracleEngine('BATCH', db_info=db_info)
        engine.update_business_batch_flow(form.trade_dt.data, form.sys_code.data)
        flash("批处理节点置成功.")
    return render_template('core/update-batch-flow.html', form=form)


@core.route('/quick-add-account', methods=('GET', 'POST'))
def quick_add_account():
    """
    一键开户
    """

    form = QuickAddAccountForm()
    rand_data = []
    if form.validate_on_submit():
        fabr = Fabricate()
        if form.random_id_btn.data:
            form.cust_id.data = fabr.cust_id()

        if form.random_name_btn.data:
            form.cust_name.data = fabr.cust_name()

        if form.random_number_btn.data:
            form.phone_number.data = fabr.phone_number()

        if form.random_bank_number_btn.data:
            form.bank_number.data = fabr.bank_number(end_number=form.bank_end_number.data)

        if form.all_generate_btn.data:
            cust_id, cust_name, phone_number, bank_number = (fabr.cust_id(), fabr.cust_name(), fabr.phone_number(),
                                                             fabr.bank_number(end_number=form.bank_end_number.data))
            form.cust_id.data = cust_id
            form.cust_name.data = cust_name
            form.phone_number.data = phone_number
            form.bank_number.data = bank_number

        if form.submit.data:
            cust_id = form.cust_id.data
            cust_name = form.cust_name.data
            phone_number = form.phone_number.data
            bank_number = form.bank_number.data
            http_client = BaseHttpClient(form.test_env.data)
            result = http_client(cust_id, cust_name, phone_number, bank_number)
            rand_data.append((cust_id, cust_name, phone_number, bank_number, result))

    return render_template('core/quick_add_account.html', form=form, rand_data=rand_data)
