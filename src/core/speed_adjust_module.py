import cv2
from PIL import Image
import os
import numpy as np
from airtest.core.api import *
from src.core.adb_module import get_screenshot


def crop_screenshot(screenshot, coords):
    """
    根据坐标裁剪截图
    
    参数:
        screenshot: PIL Image 对象或图片路径
        coords: [(左上x, 左上y), (右上x, 右上y), (左下x, 左下y), (右下x, 右下y)]
    """
    # 加载图片（如果传入的是路径）
    if isinstance(screenshot, str):
        img = Image.open(screenshot)
    else:
        img = screenshot
    
    # 提取坐标
    top_left = coords[0]      # (0, 2413)
    top_right = coords[1]     # (217, 2413)
    bottom_left = coords[2]   # (0, 2560)
    bottom_right = coords[3]  # (217, 2560)
    
    # 计算裁剪区域 (left, upper, right, lower)
    left = min(top_left[0], bottom_left[0])           # 0
    upper = min(top_left[1], top_right[1])            # 2413
    right = max(top_right[0], bottom_right[0])        # 217
    lower = max(bottom_left[1], bottom_right[1])      # 2560
    
    # 执行裁剪
    cropped_img = img.crop((left, upper, right, lower))
    
    return cropped_img


def compute_hash(img):
    # 1. 缩小到 9x8 (dHash 标准尺寸)
    resized = cv2.resize(img, (9, 8), interpolation=cv2.INTER_AREA)
    # 2. 计算相邻像素差异
    diff = resized[:, 1:] > resized[:, :-1]
    # 3. 转换为整数哈希
    return int(''.join('1' if b else '0' for b in diff.flatten()), 2)


def hamming_distance(hash1, hash2):
    xor = hash1 ^ hash2
    return bin(xor).count('1')


def detect_speed():
    screenshot = get_screenshot()
    
    coords = [(0, 2413), (217, 2413), (0, 2560), (217, 2560)]
    screenshot = crop_screenshot(screenshot, coords)
    
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    screenshot_hash = compute_hash(screenshot)
    best_match = None
    min_distance = float('inf')
    for page_name in os.listdir(os.path.join(os.getcwd(), 'template', 'speed')):
        print(f'对比{page_name}')
        page_path = os.path.join(os.getcwd(), 'template', 'speed', page_name)
        page = cv2.imread(page_path)
        page_hash = compute_hash(page)
        distance = hamming_distance(screenshot_hash, page_hash)
        if distance < min_distance:
            min_distance = distance
            best_match = page_name
    
    return best_match, min_distance


def set_speed(target_speed):
    speed_map = {
        '0.5': 1,
        '1': 2,
        '2': 3,
        '4': 4,
        '6': 5,
        '9': 6,
        '12': 7,
        '24': 8,
        'auto': 9
    }
    
    def adjust(current:str, target:str):
        times = speed_map[target] - speed_map[current]
        if times < 0:
            times += 10
        for i in range(times):
            connect_device("android://127.0.0.1:5037/127.0.0.1:5555")
            touch((122, 2482))
    
    
    
    is_finished = False
    while not is_finished:
        speed, _ = detect_speed()
        if speed != str(target_speed) + '.png':
            adjust(speed.replace('.png', ''), str(target_speed))
        else:
            is_finished = True