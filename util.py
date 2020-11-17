# -*- coding: utf-8 -*-
import cv2
from PIL import ImageGrab
from pynput.mouse import Button, Controller
import numpy
import time

# ---------图像---------
def screenshot():
    # 全屏幕截图 可改成固定区域
    im = ImageGrab.grab()
    return cv2.cvtColor(numpy.asarray(im), cv2.COLOR_RGB2BGR)

def match(img, sub_img):
    # 寻找子图在大图中的坐标位置
    h, w = sub_img.shape[:2]  # rows->h, cols->w
    # 更改匹配算法，-1为相反，1为完全一致，0为不相关，取最接近于1的
    res = cv2.matchTemplate(img, sub_img, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    click_point = (max_loc[0] + int(w/2), max_loc[1] + int(h/2))
    return max_val, click_point, int(w/2), int(h/2)

def get_point(template):
    # 截图并查找子图在截图中的坐标中心
    img = screenshot()
    _, point, _, _ = match(img, template)
    return point

def get_vertex(template):
    # 截图并查找子图在截图中的中心区域，用于随机点击
    img = screenshot()
    _, point, w, h = match(img, template)
    return (point[0]-w,point[1]-h),(point[0]+w,point[1]-h),\
        (point[0]-w,point[1]+h),(point[0]+w,point[1]+h)

# ---------鼠标---------
mouse = Controller()

def mouse_click_point():
    # 直接点击
    mouse.press(Button.left)
    mouse.release(Button.left)

def mouse_click(point):
    # 点击指定坐标
    mouse.position = point;
    mouse.press(Button.left)
    mouse.release(Button.left)

def mouse_drag(drag_distance):
    # 鼠标拖动指定距离
    mouse.press(Button.left)
    time.sleep(0.1)
    p = mouse.position
    p = (p[0]+drag_distance[0], p[1]+drag_distance[1])
    mouse.position = p
    time.sleep(0.1)
    mouse.release(Button.left)
