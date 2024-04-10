import time

import requests

app_id = "1091502237210902528"
app_key = "ad2a660bcb19453eaea6a0a2f7e834a4"

headers = {'content-type': "application/json"}
url = "http://openai.100tal.com/aiimage/common-formula-reg"


time_stamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())

data = {
    "img_base64": None
}
