#!/usr/bin/env python
# coding: utf-8

from SimpleAppServer import expose, test
from httphandler import Response
from simpletemplate import SimpleTemplate

from validators import NotEmpty, RegexValidator
from widgets import Text, Submit, Form

editforms=(Text('username', u'ユーザ名',
            validators=(NotEmpty(), RegexValidator(r'[A-Za-z\d]')),),
           Text('password', u'パスワード',
            validators=(NotEmpty(), RegexValidator(r'[A-Za-z\d]')),),
           Submit('submit', u'ログイン'))
loginform=Form(editforms, {'action':'/login', 'method':'POST'})

base_body="""<html><body>%s</body></html>"""
