from airtest.core.api import *
from src.core.ocr_module import get_text_and_loc
from src.core.adb_module import get_screenshot
from src.core.speed_adjust_module import set_speed

def enter_tiaozhan():
    # 点击战斗
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((608, 2452))
    
    # 点击日常挑战
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((426, 354))


def yuansuwangzuo():
    # 点击元素王座
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((326, 600))
    
    # 点击一键扫荡
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((1082, 360))
    
    time.sleep(2)
    
    # 点击确定
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((708, 1648))
    
    # 点击返回
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((1341, 335))


def heishita():
    # 点击黑石塔
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((367, 887))
    
    # 点击扫荡
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((155, 2504))
    
    # 点击确定
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((723, 1320))
    
    # 


def process_daily_tiaozhan():
    enter_tiaozhan()
    
    yuansuwangzuo()