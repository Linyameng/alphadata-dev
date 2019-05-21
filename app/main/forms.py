# -*- coding: utf-8 -*-
"""
Created on 2018/5/25

@author: xing yan
"""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired


class UserForm(FlaskForm):
    name = StringField('姓名：', validators=[InputRequired()])
    submit = SubmitField('提交')


