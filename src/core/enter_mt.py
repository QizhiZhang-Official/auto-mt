from airtest.core.api import *


def enter_mt():
    # 打开mt
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((267, 868))

    # 关闭公告
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    wait(Template('template/close_btn.png'))
    touch(Template('template/close_btn.png'))

    # 点击进入游戏
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    wait(Template('template/enter_game.png'))
    touch(Template('template/enter_game.png'))