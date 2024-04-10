# -*- coding:utf-8 -*-
# @Time     : 2023/8/14 22:10
# @Author   : ALIEN(XuLang)
# @Project  : my_app
import os
import sys

from lib.prepare import prepare
os.chdir(os.path.dirname(__file__))
sys.path.append("../../")
prepare()
