import cv2
import numpy as np
import easyocr


def get_text_and_loc(img, crop_points=None):
    img_np = np.array(img)
    if img_np.shape[2] == 4:
        img_np = img_np[:, :, :3]
    
    original_img_np = img_np.copy() # 备份原图数据（虽然这里主要用坐标变换）
    transform_matrix = None

    # 如果提供了裁剪点
    if crop_points is not None and len(crop_points) == 4:
        tl, tr, bl, br = crop_points
        
        # ... (计算 max_width, max_height 的代码保持不变) ...
        width_top = int(((tr[0] - tl[0]) ** 2 + (tr[1] - tl[1]) ** 2) ** 0.5)
        width_bottom = int(((br[0] - bl[0]) ** 2 + (br[1] - bl[1]) ** 2) ** 0.5)
        height_left = int(((bl[1] - tl[1]) ** 2 + (bl[0] - tl[0]) ** 2) ** 0.5)
        height_right = int(((br[1] - tr[1]) ** 2 + (br[0] - tr[0]) ** 2) ** 0.5)
        
        max_width = max(width_top, width_bottom)
        max_height = max(height_left, height_right)
        
        dst_points = np.array([
            [0, 0],
            [max_width - 1, 0],
            [0, max_height - 1],
            [max_width - 1, max_height - 1]
        ], dtype=np.float32)
        
        src_points = np.array([tl, tr, bl, br], dtype=np.float32)
        
        # 获取变换矩阵
        transform_matrix = cv2.getPerspectiveTransform(src_points, dst_points)
        img_np = cv2.warpPerspective(img_np, transform_matrix, (max_width, max_height))
    
    reader = easyocr.Reader(['ch_sim', 'en'])
    gray = cv2.cvtColor(img_np, cv2.COLOR_RGB2GRAY)
    results = reader.readtext(gray)
    
    text_and_loc_list = []
    for bbox, text, confidence in results:
        # bbox 是 4 个点的列表 [[x1,y1], [x2,y2], [x3,y3], [x4,y4]]
        bbox_np = np.array(bbox, dtype=np.float32)
        
        # 【关键修改】如果进行了裁剪，需要将坐标逆变换回原图
        if transform_matrix is not None:
            # 计算逆矩阵
            inverse_matrix = cv2.invert(transform_matrix)[1]
            # 将裁剪图中的点映射回原图
            bbox_np = cv2.perspectiveTransform(bbox_np.reshape(1, -1, 2), inverse_matrix).reshape(-1, 2)
        
        # 计算中心点
        x_coords = [point[0] for point in bbox_np]
        y_coords = [point[1] for point in bbox_np]
        
        center_x = int((min(x_coords) + max(x_coords)) / 2)
        center_y = int((min(y_coords) + max(y_coords)) / 2)
        
        text_and_loc_list.append({
            'text': text.replace(' ', ''), 
            'loc': (center_x, center_y), 
            'confidence': confidence,
            'bbox': bbox_np.tolist() # 建议也返回原始 bbox 以便调试
        })
    
    return text_and_loc_list