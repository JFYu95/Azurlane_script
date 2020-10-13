import os
import sys
import time
from moving import *
from battle import *

def main():
	val = 0.1
	wait_time = 5
	# n = 5
	for t in range(30):
		# 进图
		print('times:',t)
		if not enter_field(wait_time):
			print("进图失败")
			return
		# 索敌等待
		time.sleep(3.5)

		# 常规图优先布置boss队
		# while True:
		# 	move_to_boss(wait_time, (0,80))
		# 	print("move_to_boss")
		# 	time.sleep(7)
		# 	# 切换舰队
		# 	if not move(switch):
		# 		return
		# 	# 拖动327*121
		# 	time.sleep(1)
		# 	if not move(notarrive):
		# 		break
		
	

		# 地图位置校准
		# mouse_click((1197,319))
		# # mouse_drag((348,210))
		# mouse_drag((-400,0))

		# 优先精英怪，道中n战
		for i in range(6):
			if not normal_battle(val, wait_time):
				print("道中战错误")
				return

		time.sleep(1)
		# 切换舰队
		if not move(switch):
			return
		time.sleep(2)

		# # 地图位置校准
		# mouse_click((1197,319))
		# mouse_drag((348,210))
		# # time.sleep(1)

		# if not normal_battle(val, wait_time):
		# 	print("道中战错误")
		# 	return

		# boss

		if not boss_battle(val, wait_time):
			print("boss战错误")
			return
		# input()
	

if __name__ == '__main__':
	# while True:
	main()

