from airtest.core.api import *
from src.core.ocr_module import get_text_and_loc
from src.core.adb_module import get_screenshot
from src.core.speed_adjust_module import set_speed


FUBEN_NAME = ['祖安废墟', '火焰之心', '祭坛外围', '祭坛大厅',
              '灵魂坟墓', '逆风城堡', '割颅者之眼', '深渊领主巢穴',
              '鱼人神殿', '虚空要塞']


def enter_gonghui():
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    wait(Template('template/gonghui.png'))
    touch(Template('template/gonghui.png'))


def gonghuifuben():
    def attack(name, loc):
        connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
        touch(loc)
        time.sleep(1)
        text_list = get_text_and_loc(get_screenshot(), [(63, 620), (1380, 620), (63, 2130), (1380, 2130)])
        attack_list = []
        for item in text_list:
            if item['text'] == '剩余进攻次数:1':
                attack_list.append(item)
                print(item)
        for idx, item in enumerate(attack_list):
            if idx > 0:
                connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
                touch(loc)
            
            connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
            touch(item['loc'])
            
            wait(Template('template/attack_btn.png'))
            connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
            touch(Template('template/attack_btn.png'))
            
            time.sleep(1)
            
            # 切换团队2
            text_list = get_text_and_loc(get_screenshot(), [(0, 300), (275, 300), (0, 420), (275, 420)])
            for item in text_list:
                team = int(item['text'][-1])
            while team != 2:
                connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
                touch((140, 350))
                text_list = get_text_and_loc(get_screenshot(), [(0, 300), (275, 300), (0, 420), (275, 420)])
                for item in text_list:
                    team = int(item['text'][-1])
            
            # 点击开始战斗
            connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
            touch((720, 2010))
            
            # 调整战斗倍速
            set_speed(24)
            
            # 判断是否继续挑战
            is_continue_attack = True
            while is_continue_attack:
                continue_attack_btn = None
                cancel_btn = None
                rest_times = None
                while continue_attack_btn == None or cancel_btn == None or rest_times == None:
                    text_list = get_text_and_loc(get_screenshot(), [(183, 983), (1254, 983), (183, 1271), (1254, 1271)])
                    for item in text_list:
                        if item['text'] == '金币挑战':
                            continue_attack_btn = item['loc']
                        if item['text'] == '取消':
                            cancel_btn = item['loc']
                        if '剩余挑战次数' in item['text']:
                            rest_times = int(item['text'][-1])
                if rest_times == 0:
                    is_continue_attack = False
                    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
                    touch(cancel_btn)
                else:
                    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
                    touch(continue_attack_btn)
            
            connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
            is_battle_end = exists(Template('template/battle_failed.png'))
            while not is_battle_end:
                connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
                is_battle_end = exists(Template('template/battle_failed.png'))
                continue
            connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
            touch((720, 1280))
        
    
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    wait(Template('template/gonghuifuben.png'))
    touch(Template('template/gonghuifuben.png'))
    
    time.sleep(1)
    
    for fuben in FUBEN_NAME:
        fuben_list = get_text_and_loc(get_screenshot(), [(63, 470), (1380, 470), (63, 2205), (1380, 2205)])
        filtered_fuben_list = []
        for item in fuben_list:
            if item['text'] in FUBEN_NAME:
                filtered_fuben_list.append(item)
        is_found = False
        for item in filtered_fuben_list:
            if item['text'] == fuben:
                is_found = True
                attack(item['text'], item['loc'])
                connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
                touch((1340, 350))
                time.sleep(1)
                break
        if not is_found:
            connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
            swipe((1380, 1500), (1380, 1180))
            fuben_list = get_text_and_loc(get_screenshot(), [(63, 470), (1380, 470), (63, 2205), (1380, 2205)])
            filtered_fuben_list = []
            for item in fuben_list:
                if item['text'] in FUBEN_NAME:
                    filtered_fuben_list.append(item)
            for item in filtered_fuben_list:
                if item['text'] == fuben:
                    attack(item['text'], item['loc'])
                    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
                    touch((1340, 350))
                    time.sleep(1)
                    break


def back_home():
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    wait(Template('template/home.png'))
    touch(Template('template/home.png'))


def process_gonghui():
    enter_gonghui()
    
    gonghuifuben()
    
    back_home()