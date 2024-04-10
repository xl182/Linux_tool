import base64
import json
from io import BytesIO

import cv2
import numpy as np
import requests
from PIL import Image

API_KEY = "Kmi48UaKrgh7BT6gLubviEyO"
SECRET_KEY = "LftZIW2R0ynIaxCHoKexS7tNOPs2IBWC"


def get_payload(image):
    base64_str = ''
    if isinstance(image, Image.Image):
        img_buffer = BytesIO()
        image.save(img_buffer, format='JPEG')
        bytes_data = img_buffer.getvalue()
        base64_str = base64.b64encode(bytes_data).decode("utf-8")
    if isinstance(image, np.ndarray):
        bytes_data = cv2.imencode(".jpg", image)[1].tobytes()
        base64_str = base64.b64encode(bytes_data).decode("utf-8")
    if isinstance(image, str):
        with open(image, "rb") as f:
            base64_str = base64.b64encode(f.read()).decode("utf8")

    result = ""
    for _ in base64_str:
        if _.isdigit() or _.isalpha():
            result += _
        else:
            _ = str(hex(ord(_))).replace("0x", "%")
            result += _
    return result


def baidu_recognize(image):
    print(type(image))
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic?access_token=" + get_access_token()
    payload = 'image=' + get_payload(image)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    result_dict = json.loads(response.text)
    words = ''
    for item in result_dict["words_result"]:
        words += item["words"] + '\n'
    return words


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    img = "OCR/ocr_test.jpg"
    # img = cv2.imread("test.jpg")
    # img = Image.open("test.jpg")
    print(baidu_recognize(img))
