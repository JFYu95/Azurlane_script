# -*- coding: utf-8 -*-
import cv2
from PIL import ImageGrab
from pynput.mouse import Button, Controller
import numpy
import time
import random

mouse = Controller()

def match(img, sub_img):
	h, w = sub_img.shape[:2]  # rows->h, cols->w
	res = cv2.matchTemplate(img, sub_img, cv2.TM_SQDIFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	click_point = (min_loc[0] + int(w/2), min_loc[1] + int(h/2))
	return min_val, click_point, int(w/2), int(h/2)

# def match(img, sub_img):
# 	h, w = sub_img.shape[:2]  # rows->h, cols->w
# 	res = cv2.matchTemplate(img, sub_img, cv2.TM_SQDIFF_NORMED)
# 	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# 	click_point = (min_loc[0], min_loc[1])
# 	return min_val, click_point, int(w/2), int(h/2)
  
def screenshot():
	# bbox = (0, 0, 1920, 1030)
	im = ImageGrab.grab()
	return cv2.cvtColor(numpy.asarray(im), cv2.COLOR_RGB2BGR)

def mouse_click_point():
	mouse.press(Button.left)
	mouse.release(Button.left)

def mouse_click(point):
	mouse.position = point;
	mouse.press(Button.left)
	mouse.release(Button.left)

def mouse_drag(drag_distance):
	mouse.press(Button.left)
	time.sleep(0.1)
	p = mouse.position
	p = (p[0]+drag_distance[0], p[1]+drag_distance[1])
	mouse.position = p
	time.sleep(0.1)
	mouse.release(Button.left)

def get_point(template):
	img = screenshot()
	_, point, _, _ = match(img, template)
	return point

def get_vertex(template):
	img = screenshot()
	_, point, w, h = match(img, template)
	return (point[0]-w,point[1]-h),(point[0]+w,point[1]-h),\
		(point[0]-w,point[1]+h),(point[0]+w,point[1]+h)

def move(template):
	img = screenshot()
	min_val, click_point, w, h = match(img, template)
	if min_val < 0.11:
		click_point = (click_point[0]+random.randint(-int(w/2), int(w/2)), \
			click_point[1]+random.randint(-int(h/2), int(h/2)))
		click_point = (click_point[0]*0.8, click_point[1]*0.8)
		mouse_click(click_point)
		return True
	return False

def scan(template):
	img = screenshot()
	min_val, click_point, w, h = match(img, template)
	if min_val < 0.11:
		return True
	return False


def move_bias(template,bias):
	img = screenshot()
	min_val, click_point, w, h = match(img, template)
	if min_val < 0.11:
		click_point = (click_point[0]+bias[0]+random.randint(-int(w/2), int(w/2)), \
			click_point[1]+bias[1]+random.randint(-int(h/2), int(h/2)))
		click_point = (click_point[0]*0.8, click_point[1]*0.8)
		mouse_click(click_point)
		return True
	return False

def step(template, wait_time):
	r_times = 0
	while not move(template):
		if r_times > wait_time:
			print("time out")
			return False
		r_times += 1
		time.sleep(1)
	return True

def step_bias(template, wait_time, bias):
	r_times = 0
	while not move_bias(template,bias):
		if r_times > wait_time:
			print("time out")
			return False
		r_times += 1
		time.sleep(1)
	return True


def attack(enemies, val):
	# 作战海域
	img = screenshot()
	min_val = 1
	for enemy in enemies:
		min_val, click_point, w, h = match(img, enemy)
		if min_val < val+0.06:
			click_point = (click_point[0]+random.randint(-int(w/2), int(w/2)), click_point[1]+14)
			click_point = (click_point[0]*0.8, click_point[1]*0.8)
			mouse_click(click_point)
			print("find enemy successfully")
			return True
	# print("fialed to find enemy")
	return False

# 随机委托
def entrust_cutin(entrust,ensure):
	img = screenshot()
	min_val, click_point, w, h = match(img, entrust)
	if min_val < 0.05:
		min_val, click_point, w, h = match(img, ensure)
		click_point = (click_point[0]+random.randint(-int(w/2), int(w/2)), \
			click_point[1]+random.randint(-int(h/2), int(h/2)))
		mouse_click(click_point)
		print("entrust cutin")
		return True
	return False

def new_ship(newship):
	img = screenshot()
	min_val, click_point, _, _ = match(img, newship)
	if min_val < 0.05:
		click_point = (click_point[0]*0.8, click_point[1]*0.8)
		mouse_click(click_point)
		time.sleep(1)
		click_point = (click_point[0],click_point[1]+100)
		click_point = (click_point[0]*0.8, click_point[1]*0.8)
		mouse_click(click_point)
		time.sleep(0.1)
		mouse_click(click_point)
		print("new ship")
		return True
	return False
