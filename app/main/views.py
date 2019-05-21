# -*- coding: utf-8 -*-
"""
Created on 2018/5/24

@author: xing yan
"""
from datetime import datetime
from flask import render_template, abort, flash, redirect, url_for ,session, send_from_directory
from flask_login import current_user, login_required
import os
from . import main
from .. import db
from ..models import Permission, User, EnvironMapping, PageView ,actioncolumn
from ..decorators import permission_required, admin_required
from ..create_execute import OracleEngine
from collections import OrderedDict

@main.route('/favicon.ico')
def favicon():
    return send_from_directory( 'static','favicon.ico', mimetype='image/vnd.microsoft.icon')


@main.route('/', methods=('GET', 'POST'))
@login_required
def index():
    username = current_user.username
    role = User.query.filter_by(username=username).first()
    if role:
        bb = role.role_id
    else:
        bb = 1
    print(bb)
    return render_template('index.html', current_time=datetime.utcnow(), bb = bb)


@main.route('/admin')
@login_required
@admin_required
def for_admin_only():
    return 'For administrator'


@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderate_only():
    return 'for comment moderators!'


@main.route('/user/<username>', methods=('GET',))
@login_required
def user_info(username):
    username = current_user.username
    role = User.query.filter_by(username=username).first()
    if role:
        bb = role.role_id
    else:
        bb = 1
    print(bb)
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user ,bb=bb)
