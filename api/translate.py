import hashlib
import json
import random

import bs4
import requests





def baidu_translate(text, from_lang="en", to_lang="zh"):
    appid = "20230304001585529"
    key = "glcYcvilga2eFjLz6pmC"

    def get_md5(question, _salt):
        _data = appid + question + _salt + key
        return hashlib.md5(_data.encode(encoding="UTF-8"))

    salt = str(random.randint(1, 65536))
    md5 = get_md5(text, salt)
    data = {
        "q": text.encode(),
        "from": from_lang,
        "to": to_lang,
        "appid": appid,
        "salt": salt,
        "sign": md5.hexdigest()
    }
    response = requests.post("https://fanyi-api.baidu.com/api/trans/vip/translate", data=data)
    if response.status_code != 200:
        return None
    result = json.loads(response.text)

    try:
        result = result["trans_result"][0]["dst"]
    except KeyError:
        result = None
    return result


def get_word_dictionary(word):
    def get_content(from_obj, selector_str):
        rst = from_obj.select(selector_str)
        if len(rst) == 0:
            return None
        elif len(rst) == 1:
            return rst[0].get_text().replace("\xa0", "  ").strip()
        else:
            return '\n'.join([e.get_text() for e in rst])

    req_link = f"https://cn.bing.com/dict/search?q={word}"
    res_txt = requests.get(req_link).text
    soup = bs4.BeautifulSoup(res_txt, 'html.parser')
    word_info_selector_dict = {
        # '英语': 'div#headword',
        '中文翻译': 'div.qdef > ul > li',
        '复数': 'div.hd_div1',
        '英式发音': 'div.hd_pr',
        '美式发音': 'div.hd_prUS',
    }
    word_info_dict = {}
    related_divs = soup.select('div.lf_area > div')
    for k, v in word_info_selector_dict.items():
        word_info_dict[k] = get_content(related_divs[0], v)
    return word_info_dict


if __name__ == "__main__":
    print(baidu_translate("hello"))
