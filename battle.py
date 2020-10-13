from moving import *
import time
from clear import *


# config
aim = cv2.imread('./pic/map/h6.png')

go = cv2.imread('./pic/button/go.png')
success = cv2.imread('./pic/button/continue.png')
item = cv2.imread('./pic/button/item.png')
finish = cv2.imread('./pic/button/yes.png')
switch = cv2.imread('./pic/button/switch.png')
entrust = cv2.imread('./pic/button/entrust.png')
ensure = cv2.imread('./pic/button/ensure.png')
newship = cv2.imread('./pic/button/new.png')
notarrive = cv2.imread('./pic/button/notarrive.png')
space = cv2.imread('./pic/enemy/space.png')

normals = []
normals.append(cv2.imread('./pic/enemy/e3.png'))
normals.append(cv2.imread('./pic/enemy/e5.png'))
normals.append(cv2.imread('./pic/enemy/e1.png'))
normals.append(cv2.imread('./pic/enemy/e2.png'))
normals.append(cv2.imread('./pic/enemy/e4.png'))
elites = []

elites.append(cv2.imread('./pic/enemy/elite1.png'))
elites.append(cv2.imread('./pic/enemy/elite2.png'))
elites.append(cv2.imread('./pic/enemy/elite3.png'))

boss = []
# boss.append(cv2.imread('./pic/enemy/boss2.png'))
boss.append(cv2.imread('./pic/enemy/boss1.png'))

def move_to_boss(wait_time, bias):
	if not step_bias(space, wait_time, bias):
		return False

def enter_field(wait_time):
	# 出击图
	if not step(aim, wait_time):
		return False
	# 关卡图
	time.sleep(1)
	if not step(go, wait_time):
		return False
	# 满船坞处理
	time.sleep(0.5)
	if clear_ship():
		# 出击图
		if not step(aim, wait_time):
			return False
		# 关卡图
		time.sleep(1)
		if not step(go, wait_time):
			return False
	# 配置界面
	time.sleep(1)
	if not step(go, wait_time):
		return False
	time.sleep(1)
	entrust_cutin(entrust,ensure)
	return True

def find_normal_enemy(val):
	find_elite = True
	while not attack(elites, val):
		print("精英怪")
		val+=0.02
		if val > 0.12:
			find_elite = False
			break
	val = 0.1
	if not find_elite:
		while not attack(normals, val):
			print("普通怪")
			val+=0.02
			if val > 0.12:
				print("failed to find enemy")
				return False
	return True

def wait_battle():
	while True:
		if move(success):
			break;
		time.sleep(2)
	# 再判断战斗结束
	time.sleep(1)
	move(success)

def battle_finish(wait_time):
	# 获得道具
	time.sleep(0.5)
	if not step(item, wait_time):
		print("1")
		return False
	# 可能出稀有船，新船，待处理，
	# mouse_click_point()
	# mouse_click_point()
	# mouse_click_point()
	# 经验结算
	time.sleep(0.5)
	if not step(finish, wait_time):
		print("可能出现新船")
		if not new_ship(newship):
			print("error")
			return False
	if not step(finish, wait_time):
		print("2")
		return False
	time.sleep(0.5)
	if not move(finish):
		# return False
		pass

	return True

def normal_battle(val, wait_time):
	if not find_normal_enemy(val):
		print("error")
		return False
	# 等待移动时间
	time.sleep(9)
	# 是否满船坞，清理
	if clear_ship():
		time.sleep(4)
		if not step(yingji, wait_time):
			print("迎击失败")
			return False
	# 等待最小自律时间
	time.sleep(10)
	wait_battle()
	if not battle_finish(wait_time):
		print ("1234")
		return False
	# 索敌时间
	time.sleep(4)
	# 随机委托处理
	entrust_cutin(entrust,ensure)
	return True

def boss_battle(val, wait_time):
	while not attack(boss, val):
		val+=0.02
		if val > 0.16:
			print("failed to find boss")
			return False
	# 等待移动时间
	time.sleep(6)
	# 是否满船坞，清理
	if clear_ship():
		time.sleep(4)
		if not step(yingji, wait_time):
			print("迎击失败")
			return False
	# 等待最小自律时间
	time.sleep(30)
	wait_battle()
	if not battle_finish(wait_time):
		print("123")
		return False
	# 结束
	time.sleep(5)
	entrust_cutin(entrust,ensure)
	return True