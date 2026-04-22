import io
import subprocess
from PIL import Image


def start_adb_service(ADB_PATH='C:\Program Files\BlueStacks_nxt_cn\HD-Adb.exe'):
    cmd = [ADB_PATH, 'get-state']
    result = subprocess.run(cmd, shell=True, capture_output=True, check=True)


def stop_adb_service(ADB_PATH='C:\Program Files\BlueStacks_nxt_cn\HD-Adb.exe'):
    cmd = [ADB_PATH, 'kill-server']
    result = subprocess.run(cmd, shell=True, capture_output=True, check=True)


def get_screenshot(ADB_PATH='C:\Program Files\BlueStacks_nxt_cn\HD-Adb.exe'):
    start_adb_service()
    cmd = [ADB_PATH, 'exec-out', 'screencap', '-p']
    result = subprocess.run(cmd, shell=True, capture_output=True, check=True)

    image_data = io.BytesIO(result.stdout)
    img = Image.open(image_data)
    
    stop_adb_service()

    return img