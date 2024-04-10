import os
import re
import subprocess


def get_cmd_output(cmd):
    res = ""
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    for line in iter(p.stdout.readline, b''):
        res += line.decode('utf-8').strip()
    return res


def get_temp():
    cmd = ["sudo", "cat", "/sys/class/thermal/thermal_zone0/temp"]
    temp = int(get_cmd_output(cmd)) / 1000
    return temp


def get_ip():
    cmd = ["sudo", "ifconfig"]
    output = get_cmd_output(cmd)

    pat = re.compile(r"192.168.\d{1,3}.\d{1,3}")
    res = pat.findall(output)
    return res


if __name__ == "__main__":
    print(get_ip())
    print(get_temp())
