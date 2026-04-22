from airtest.core.api import *


def process_yuansu():
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    wait(Template('template/yuansu.png'))
    touch(Template('template/yuansu.png'))
    
    # 元素试炼
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((425, 355))
    
    # 一键扫荡 1
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((720, 1935))
    
    # 一键扫荡 2
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((720, 1583))
    
    # 确定
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((720, 1318))
    
    # back home
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((128, 2455))