from airtest.core.api import *
from src.core.ocr_module import get_text_and_loc
from src.core.adb_module import get_screenshot


def get_current_tili():
    text_list = get_text_and_loc(get_screenshot(), [(1143, 81), (1356, 81), (1143, 158), (1356, 158)])
    
    print(text_list[0])