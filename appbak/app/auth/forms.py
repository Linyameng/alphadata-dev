# -*- coding: utf-8 -*-
"""
Created on 2018/5/25

@author: xing yan
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, InputRequired, EqualTo, Regexp
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[InputRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[InputRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    email = StringField('邮箱', validators=[InputRequired(), Email(), Length(1, 64)])
    username = StringField('用户名', validators=[InputRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                     'Usernames must have only letters,'
                                                                                     'numbers, dots or underscores')])
    password = PasswordField('新密码', validators=[InputRequired(), EqualTo('confirm', 'Password must match.')])
    confirm = PasswordField('重复输入密码')
    submit = SubmitField('注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已注册.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('旧密码', validators=[InputRequired()])
    new_password = PasswordField('新密码', validators=[InputRequired(), EqualTo('confirm', '二次输入的密码不一致.')])
    confirm = PasswordField('重复输入新密码')
    submit = SubmitField('确认修改')


class PasswordResetForm(FlaskForm):
    email = StringField('邮箱', validators=[InputRequired(), Email(), Length(1, 64)])
    new_password = PasswordField('新密码', validators=[InputRequired(), EqualTo('confirm', '二次输入的密码不一致.')])
    confirm = PasswordField('重复输入新密码')
    submit = SubmitField('确认修改')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('邮箱不存在.')


class ProvideEmailForm(FlaskForm):
    email = StringField('邮箱', validators=[InputRequired(), Email(), Length(1, 64)])
    submit = SubmitField('提交')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('邮箱不存在.')


class ChangeEmailForm(FlaskForm):
    old_email = StringField('邮箱', validators=[InputRequired(), Email(), Length(1, 64)])
    email = StringField('新邮箱', validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField('密码', validators=[InputRequired()])
    submit = SubmitField('更新邮箱地址')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已注册.')
