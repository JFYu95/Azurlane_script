# -*- coding: utf-8 -*-
from util import *
from config import *
import random
import time

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
    # 修改：循环等待目标状态出现，出现目标点击目标，确认目标消失，结束
    r_times = 0
    time.sleep(0.3)
    while not scan(template):
        if r_times > wait_time*10:
            print('目标不出现')
            return False
        r_times += 1
        time.sleep(0.2)
    # 目标出现点击目标
    move(template,bias)
    # time.sleep(0.1)
    # 确认消失
    # r_times = 0
    # while scan(template):
    #     if r_times > wait_time*10:
    #         print('目标点击无效')
    #         return False
    #     r_times += 1
    #     move(template,bias)
    #     time.sleep(0.1)
    # 该段存在问题
    return True
    # while not move(template,bias):
    #     if r_times > wait_time:
    #         print("time out, r_time=", r_times)
    #         return False
    #     r_times += 1
    #     time.sleep(1)
    # return True

def attack_move(enemies):
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
    print('max_val: ',max_val)
    return False

def attack_click(max_val, click_point, w, h):
    # 下移14像素，防止点到上方格子
    click_point = (click_point[0]+random.randint(-int(w/2), int(w/2)), click_point[1]+14)
    click_point = (click_point[0]*resolution_rate, click_point[1]*resolution_rate)
    mouse_click(click_point)
    return True

def attack_scan(enemies):
    img = screenshot()
    for enemy in enemies:
        max_val, click_point, w, h = match(img, enemy)
        if max_val > threshold:
            return True, max_val, click_point, w, h
    return False, None, None, None, None


def attack_step(enemies, wait_time=10):
    r_times = 0
    # 等待目标出现
    flag, max_val, click_point, w, h = False, None, None, None, None
    while True:
        if r_times > wait_time*2:
            print('目标不出现或未找到')
            return False
        flag, max_val, click_point, w, h =  attack_scan(enemies)
        if flag:
            break
        r_times += 1
        time.sleep(0.2)
    # 目标出现点击目标
    print('max_val: ',max_val)
    print("find enemy successfully")
    attack_click(max_val, click_point, w, h)
    # for i in range(5):
    #     time.sleep(1)
    #     attack_click(max_val, click_point, w, h)
    # time.sleep(10)
    # 确认目标消失
    
    # flag, max_val, click_point, w, h =  attack_scan(enemies)
    # if flag:
    #     print('目标点击无效')
    #     return False

    return True
    # r_times = 0
    # while not attack(enemies):
    #     if r_times > wait_time:
    #         return False
    #     r_times += 1
    #     time.sleep(1)
    # return True
