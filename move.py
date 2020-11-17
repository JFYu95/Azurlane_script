# -*- coding: utf-8 -*-
from util import *
import random
import time

# 子图相似度阈值，大于0.8
threshold = 0.8
# 分辨率校准,125%即乘以0.8的系数
resolution_rate = 0.8

def move(template,bias=(0,0)):
    # 增加偏置的点击，用于标志物和点击位置不重合的情况
    img = screenshot()
    max_val, click_point, w, h = match(img, template)
    # print(max_val)
    if max_val > threshold:
        click_point = (click_point[0]+bias[0]+random.randint(-int(w/2), int(w/2)), \
            click_point[1]+bias[1]+random.randint(-int(h/2), int(h/2)))
        click_point = (click_point[0]*0.8, click_point[1]*0.8)
        mouse_click(click_point)
        return True
    print('max_val:', max_val)
    return False

def scan(template):
    # 只判断子图是否存在，不点击
    img = screenshot()
    max_val, click_point, w, h = match(img, template)
    if max_val > threshold:
        return True
    return False

def step(template, wait_time=5, bias=(0,0)):
    # 重试若干次move判断，每次时延1s
    r_times = 0
    while not move(template,bias):
        if r_times > wait_time:
            print("time out, r_time=", r_times)
            return False
        r_times += 1
        time.sleep(1)
    return True

def attack(enemies):
    # 点击敌艦函数，由于存在多种敌艦，不使用step
    img = screenshot()
    for enemy in enemies:
        max_val, click_point, w, h = match(img, enemy)
        if max_val > threshold:
            # 统计敌艦相似度
            print('max_val: ',max_val)
            # 下移14像素，防止点到上方格子
            click_point = (click_point[0]+random.randint(-int(w/2), int(w/2)), click_point[1]+14)
            click_point = (click_point[0]*resolution_rate, click_point[1]*resolution_rate)
            mouse_click(click_point)
            print("find enemy successfully")
            return True
    return False

def attack_step(enemies, wait_time=5):
    r_times = 0
    while not attack(enemies):
        if r_times > wait_time:
            return False
        r_times += 1
        time.sleep(1)
    return True
