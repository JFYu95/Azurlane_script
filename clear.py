from moving import *
import time

# 一键清理船坞
full = cv2.imread('./pic/button/full.png')
zhengli = cv2.imread('./pic//button/zhengli.png')
tuiyi = cv2.imread('./pic/button/tuiyi.png')
queding = cv2.imread('./pic/button/queding.png')
daoju = cv2.imread('./pic/button/daoju.png')
none = cv2.imread('./pic/button/none.png')
yingji = cv2.imread('./pic/button/yingji.png')
quxiao = cv2.imread('./pic/button/quxiao.png')

# 清理船坞
def clear_ship():
	img = screenshot()
	min_val, click_point, _, _ = match(img, full)
	if min_val < 0.05:
		min_val, click_point, _, _ = match(img, zhengli)
		click_point = (click_point[0]*0.8, click_point[1]*0.8)
		mouse_click(click_point)
		time.sleep(2)
		while True:
			if not move(tuiyi):
				return False
			time.sleep(1)
			if move(none):
				break
			if not move(queding):
				return False
			time.sleep(1)
			if not move(daoju):
				return False
			time.sleep(1)
			if not move(queding):
				return False
			time.sleep(1)
			if not move(queding):
				return False
			time.sleep(1)
			if not move(daoju):
				return False
			time.sleep(1)
		if not move(quxiao):
			return False
		print("clear ship successfully")
		return True
	return False
