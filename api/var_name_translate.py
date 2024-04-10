# -*- coding:utf-8 -*-
# @Time     : 2023/5/23 16:05
# @Author   : ALIEN(XuLang)
# @Project  : my_app

import json
import requests


class NamedType:
    LITTLE_HUMP = 1
    GREAT_HUMP = 2
    UNDERLINE = 3
    CONSTANT = 4


def get_var_name(word, named_type=NamedType.UNDERLINE, translation_mode="1"):
    url = "https://fanyi.phpstudyhelper.com/TranslateWord"

    data = {
        "word": word,
        "named_type": str(named_type),
        "translation_mode": translation_mode
    }

    resp = requests.post(url, data=data)
    res_dict = json.loads(resp.text)
    return res_dict["data"]["word"]


if __name__ == "__main__":
    print(get_var_name("获取单词字典"))
