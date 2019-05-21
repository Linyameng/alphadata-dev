# -*- coding: utf-8 -*-
"""
Created on 2018/5/25

@author: xing yan
"""
from flask import render_template, redirect, flash, request, url_for
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from ..models import User
from .forms import LoginForm, RegistrationForm, ChangePasswordForm, PasswordResetForm, ProvideEmailForm, ChangeEmailForm
from .. import db


@auth.before_app_request
def before_request():
    if current_user.is_authenticated:
        current_user.ping()
        if not current_user.confirmed \
                and request.endpoint[:5] != 'auth.' \
                and request.endpoint != 'static':
            return redirect(url_for('auth.unconfirmed'))


@auth.route('/login', methods=('GET', 'POST'))
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('无效用户名或是密码.')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('你已退出登录.')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=('GET', 'POST'))
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        flash('一个包含令牌的链接地址已生成，请点击确认链接激活用户.')
        return render_template('auth/gets_token.html', endpoint='.confirm', token=token, user=user)
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        flash('你的账号已激活,谢谢！')
    else:
        flash('该确认链接地址无效或已过期.')
    return redirect(url_for('main.index'))


@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    flash('一个包含token令牌新的链接地址已生成.')
    return render_template('auth/gets_token.html', endpoint='.confirm', token=token, user=current_user)


@auth.route('/change-password', methods=('GET', 'POST'))
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.new_password.data
            db.session.add(current_user)
            flash('您的密码已改成功，请使用新密码重新登录.')
            return redirect(url_for('.logout'))
        else:
            flash('原密码不正确.')
    return render_template('auth/change_password.html', form=form)


@auth.route('/reset', methods=('GET', 'POST'))
def reset_password_request():
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = ProvideEmailForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = user.generate_reset_token()
            flash('一个包含新token令牌链接地址已生成,请点击该地址重设密码.')
            return render_template('auth/gets_token.html', endpoint='.reset_password', token=token, user=user)
    return render_template('auth/provide_email.html', form=form)


@auth.route('/reset/<token>', methods=('GET', 'POST'))
def reset_password(token):
    if not current_user.is_anonymous:
        return redirect(url_for('main.index'))
    form = PasswordResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            flash('用户不存在.')
            return redirect(url_for('main.index'))
        if user.reset_password(token, form.new_password.data):
            flash('你的密码已更新.')
            return redirect(url_for('.login'))
        else:
            flash('无效的链接或是令牌已过期.')
            return redirect(url_for('main.index'))
    return render_template('auth/reset_password.html', form=form)


@auth.route('/change-email', methods=('GET', 'POST'))
@login_required
def change_email_request():
    form = ChangeEmailForm()
    form.old_email.data = current_user.email
    if form.validate_on_submit():
        if current_user.verify_password(form.password.data):
            token = current_user.generate_change_email_token(form.email.data)
            flash('一个包含新token令牌链接地址已生成,请点击该地址修改邮箱地址.')
            return render_template('auth/gets_token.html', endpoint='.change_email', token=token, user=current_user)
        else:
            flash('无效邮箱或是密码.')
    return render_template('auth/change_password.html', form=form)


@auth.route('/change-email/<token>')
@login_required
def change_email(token):
    if current_user.change_email(token):
        flash('邮箱地址已更新,请使用新的邮箱地址登录.')
        return redirect(url_for('.login'))
    else:
        flash('更新邮箱链接无效或是已过期.')
        return redirect(url_for('main.index'))