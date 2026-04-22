from airtest.core.api import *
from src.core.ocr_module import get_text_and_loc
from src.core.adb_module import get_screenshot
from src.core.speed_adjust_module import set_speed


def enter_jiayuan():
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch(Template('template/jiayuan.png'))


def update_current_page_members(current_page_members: list, text_list: list)->list:
    window_size = len(text_list)
    current_page_members_clip = current_page_members[-window_size:]
    exceed_list = []
    for step in range(window_size):
        size = window_size - step
        
        current_page_members_clip = current_page_members_clip[1:]
        exceed_list.append(text_list[-1])
        text_list = text_list[:-1]
        
        is_match = False
        if current_page_members_clip == text_list:
            is_match = True
        if is_match:
            exceed_list.reverse()
            return current_page_members + exceed_list
    
    return []


def set_group():
    # 设置队长
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((195, 585))
    
    text_list = get_text_and_loc(get_screenshot(), [(310, 630), (825, 630), (310, 2096), (825, 2096)])
    # 过滤数字
    text_list = [item for item in text_list if not item['text'].isdigit()]
    for item in text_list:
        if item['text'] == '哀木涕':
            connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
            touch(item['loc'])
            # 确定
            connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
            touch((1280, 2390))
    
    # 设置队员
    current_page_members = []
    member_selecting = ['圣光棍', '术士大妈', '希尔瓦娜斯', '女潜行者']
    last_member_list = []
    
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((490, 590))
    
    while len(member_selecting) != 0:
        text_list = get_text_and_loc(get_screenshot(), [(310, 630), (825, 630), (310, 2096), (825, 2096)])
        # 过滤数字
        text_list = [item for item in text_list if not any(char.isdigit() for char in item['text'])]
        member_list = [item['text'] for item in text_list]
        for item in text_list:
            for member in member_selecting:
                if item['text'] in member or member in item['text']:
                    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
                    touch(item['loc'])
                    member_selecting.remove(member)
            
        
        # 判断是下滑还是翻页
        if member_list == last_member_list:
            connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
            swipe((720, 1280), (300, 1280))
        else:
            connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
            swipe((1390, 1550), (1390, 1350), duration=3, steps=100)
            last_member_list = member_list
    
    # 确定
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((1280, 2390))
    


def attack():
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((1340, 350))
    
    text_list = get_text_and_loc(get_screenshot(), [(820, 760), (1070, 760), (820, 860), (1070, 860)])
    if int(text_list[0]) == 0:
        pass


def process_nongchang():
    connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
    touch((400, 1700))
    
    mode = None
    
    text_list = get_text_and_loc(get_screenshot(), [(0, 300), (275, 300), (0, 420), (275, 420)])
    if len(text_list) > 0:
        if text_list[0]['text'] == '农场':
            mode = 'normal'
    else:
        text_list = get_text_and_loc(get_screenshot(), [(555, 490), (900, 490), (555, 610), (900, 610)])
        if len(text_list) > 0:
            if text_list[0]['text'] == '怪物来袭':
                mode = 'attack'
    
    if mode == 'normal':
        # 农夫的奖励
        connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
        touch((720, 1320))
        
        # 收获
        connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
        touch((1190, 677))
        
        # 确定
        connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
        touch((720, 1320))
        
        # 生产
        connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
        touch((1190, 677))
        
        # 返回
        connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
        touch((1340, 350))
        
    if mode == 'attack':
        # 配置队伍
        connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
        touch((1340, 350))
        


def process_jiayuan():
    # enter_jiayuan()
    
    # process_nongchang()
    
    set_group()