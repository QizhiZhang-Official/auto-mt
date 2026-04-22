from airtest.core.api import *
from src.core.ocr_module import get_text_and_loc
import cv2


def enter_shizijun():
    wait(Template('template/zhandou.png'))
    touch(Template('template/zhandou.png'))
    
    wait(Template('template/richangjindian.png'))
    touch(Template('template/richangjindian.png'))
    
    wait(Template('template/shizijun.png'))
    touch(Template('template/shizijun.png'))


def get_remain():
    snapshot('screenshot.png')
    img = cv2.imread('screenshot.png')
    text_list = get_text_and_loc(img, [(347, 2454), (777, 2454), (347, 2530), (777, 2530)])
    for i in range(len(text_list)):
        if '剩余重置次数' in text_list[i]['text']:
            return int(text_list[i + 1]['text'])


def restart():
    wait(Template('template/restart.png'))
    touch(Template('template/restart.png'))
    
    wait(Template('template/confirm.png'))
    touch(Template('template/confirm.png'))



def process_shizijun():
    enter_shizijun()
    
    time.sleep(1)
    
    remain = get_remain()
    
    print(f'剩余攻打次数：{remain}')
    if remain > 0:
        print('可以攻打！')
    
    restart()