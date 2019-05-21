# -*- coding: utf-8 -*-
"""
Created on 2018/9/10

@author: xing yan
"""

from flask import render_template, request, g
from flask.views import View

from . import boot
from .forms import DealOrderForm
from .. import db
from ..models import PageView, EnvironMapping
from ..create_execute import OracleEngine


@boot.before_request
def query_page_view():
    page_view = PageView.query.filter_by(view=request.endpoint).first()
    if page_view is None:
        page_view = PageView(view=request.endpoint)
        db.session.add(page_view)
    if request.method == 'POST':
        page_view.pv += 1
        db.session.add(page_view)
    g.page_view = page_view


@boot.context_processor
def inject_template_extras():
    return dict(page_view=g.page_view)


@boot.teardown_request
def teardown_req(exc=None):
    pass


class BaseView(View):

    methods = ['GET', 'POST']

    def set_query_table(self):
        raise NotImplementedError()

    def page_view_count(self):
        page_view = PageView.query.filter_by(view=self.__class__.__name__).first()
        if page_view is None:
            page_view = PageView(view=self.__class__.__name__)
            db.session.add(page_view)
        return page_view

    def dispatch_request(self):
        pass


class HelloView(BaseView):

    def dispatch_request(self):

        tables = {
            'deal_order': 'deal_no',
            'high_deal_order_dtl': 'deal_no',
            'deal_order_extend': 'deal_no',
            'payment_order': 'deal_no',
            'simu_fund_check_order': 'deal_no'
        }

        form = DealOrderForm()
        tabs_data = []
        page_view = self.page_view_count()

        if form.validate_on_submit():
            db_info = EnvironMapping.query.filter_by(tms_ip=form.test_env.data).first()
            engine = OracleEngine(username=db_info.user_prefix + '_ORDERS1', password=db_info.db_password)
            tabs_data = engine.with_execute(tables, form.deal_no.data)
            page_view.pv += 1
            db.session.add(page_view)
        return render_template('boot/query.html', form=form, tabs_data=tabs_data)


boot.add_url_rule('/hello', view_func=HelloView.as_view("hello_view"))


@boot.route('/querydealorder', methods=('GET', 'POST'))
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
        engine = OracleEngine(username=db_info.user_prefix + '_ORDERS1', password=db_info.db_password)
        tabs_data = engine.with_execute(tables, form.deal_no.data)
    return render_template('core/querydealorder.html', form=form, tabs_data=tabs_data)