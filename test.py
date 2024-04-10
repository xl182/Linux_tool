import time

import pywifi
from pywifi import const


def break_wifi(self):
    # 页面ip池满，断开wifi，重连！
    wifi = pywifi.PyWiFi()  # 声明wifi类对象
    iface = wifi.interfaces()[0]  # 读取第一个wifi
    # 获取无线网卡信息
    wifi_name = iface.scan_results()[0].ssid  # 获取WiFi的名字
    iface.disconnect()  # 断开第一个wifi
    time.sleep(5)
    # wifi名字1
    if "wifi名字1" == wifi_name:
        name_ssid = "wifi名字1"
        name_key = 'wifi密码'
    # wifi名字2
    elif "wifi名字2" == wifi_name:
        name_ssid = "wifi名字2"
        name_key = "wifi密码"
    # 判断wifi是否断开，没有断开在断开一次
    if iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
        wifi = pywifi.PyWiFi()  # 声明wifi类对象
        iface = wifi.interfaces()[0]  # 读取第一个wifi
        iface.disconnect()  # 断开第一个wifi

    # 切换wifi
    profile = pywifi.Profile()
    profile.ssid = name_ssid  # 切换wifi名字
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP  # 获取wifi在第几个
    profile.key = name_key  # 切换wifi的密码
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
