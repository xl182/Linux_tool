# -*- coding:utf-8 -*-
# @Time     : 2023/8/14 21:55
# @Author   : ALIEN(XuLang)
# @Project  : my_app

import os

stored_path = ""


def store_path():
    global stored_path
    stored_path = os.path.abspath(".")
    print(f"stored {stored_path}")


def restore_path():
    global stored_path
    os.chdir(stored_path)
    print(f"restore to {stored_path}")


if __name__ == "__main__":
    store_path()
    restore_path()
