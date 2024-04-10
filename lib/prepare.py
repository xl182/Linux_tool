import os
import time

from m_config.path import *

os.chdir(os.path.dirname(__file__))


def tran_ui():
    os.chdir(ui_dir)

    ui_files = []
    for _ in os.listdir(ui_dir):
        if ".ui" not in _:
            continue
        if float(time.time()) - os.path.getmtime(_) > 60 * 10:
            continue
        ui_files.append(_)

    for ui_file in ui_files:
        ui_py_file = f"ui_{ui_file.replace('.ui', '.py')}"
        command = f'{str(uic_path)} {ui_file} -o {ui_py_file}'
        os.system(command)
        print(command)


def tran_qrc():
    os.chdir(qrc_dir)
    if not os.path.exists("../src/resource.qrc"):
        return

    if float(time.time()) - os.path.getmtime("../src/resource.qrc") < 60 * 10:
        command = f"{rcc_path}  ../src/resource.qrc -o ../src/resource_rc.py"
        os.system(command)
        print(command)

    os.chdir(ui_dir)
    for py_file in os.listdir(ui_dir):
        if ".py" not in py_file:
            continue
        if float(time.time()) - os.path.getmtime(py_file) > 60 * 10:
            continue
        print(f"replaced {py_file}")
        with open(py_file, "r+", encoding="utf-8") as f:
            text = f.read()
            text = text.replace("import resource_rc", "import src.resource_rc")
        with open(py_file, "w", encoding="utf-8") as f:
            f.write(text)


def prepare():
    tran_ui()
    tran_qrc()


if __name__ == "__main__":
    tran_ui()
    tran_qrc()
