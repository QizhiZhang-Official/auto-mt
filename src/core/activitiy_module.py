from airtest.core.api import *


def enter_activity():
    wait(Template('template/activity.png'))
    touch(Template('template/activity.png'))


def yaoqianshu():
    wait(Template('template/yaoqianshu.png'))
    touch(Template('template/yaoqianshu.png'))
    
    wait(Template('template/kaishiyaoqian.png'))
    touch(Template('template/kaishiyaoqian.png'))


def qiandao():
    wait(Template('template/qiandao.png'))
    touch(Template('template/qiandao.png'))
    
    time.sleep(1)
    touch((1230, 560))


def process_activity():
    enter_activity()
    yaoqianshu()
    qiandao()