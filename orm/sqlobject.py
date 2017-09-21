# encoding: UTF-8

from sqlobject import *

DSNs = {'sqlite': 'sqlite:///:memory:'}


class Users(SQLObject):
    login = StringCol(length)