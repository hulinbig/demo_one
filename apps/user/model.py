#!-*- coding:utf-8 -*-
__author__ = 'ALX LIN'

class User:
    def __init__(self, username, password, phone=None):
        self.username = username
        self.password = password
        self.phone = phone

    def __str__(self):
        return self.username