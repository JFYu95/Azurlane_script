from move import *
from common import *
import time

# config
aim = cv2.imread('./pic/map/sp4.png')

go = cv2.imread('./pic/button/go.png')
success = cv2.imread('./pic/button/continue.png')
item = cv2.imread('./pic/button/item.png')
finish = cv2.imread('./pic/button/yes.png')
switch = cv2.imread('./pic/button/switch.png')
entrust = cv2.imread('./pic/button/entrust.png')
ensure = cv2.imread('./pic/button/ensure.png')
newship = cv2.imread('./pic/button/new.png')
newship1 = cv2.imread('./pic/button/new1.png')
notarrive = cv2.imread('./pic/button/notarrive.png')
space = cv2.imread('./pic/enemy/space.png')

normals = []
normals.append(cv2.imread('./pic/enemy/main3.png'))
normals.append(cv2.imread('./pic/enemy/defence3.png'))
normals.append(cv2.imread('./pic/enemy/air3.png'))
elites = []
elites.append(cv2.imread('./pic/enemy/elite1.png'))
elites.append(cv2.imread('./pic/enemy/elite2.png'))
elites.append(cv2.imread('./pic/enemy/elite3.png'))
elites.append(cv2.imread('./pic/enemy/elite4.png'))
elites.append(cv2.imread('./pic/enemy/elite5.png'))
elites.append(cv2.imread('./pic/enemy/elite6.png'))

boss = []
boss.append(cv2.imread('./pic/enemy/boss2.png'))
boss.append(cv2.imread('./pic/enemy/boss1.png'))

def fail():
    input("识别失败，Press Enter to continue...")

def enter_field(wait_time):
    # 出击图
    if not step(aim, wait_time):
        # return False
        fail()
    # 关卡图
    time.sleep(0.3)
    if not step(go, wait_time):
        # return False
        fail()
    # 满船坞处理
    time.sleep(0.3)
    if clear_ship():
        # 出击图
        if not step(aim, wait_time):
            # return False
            fail()
        # 关卡图
        time.sleep(0.3)
        if not step(go, wait_time):
            # return False
            fail()
    # 配置界面
    time.sleep(0.3)
    if not step(go, wait_time):
        # return False
        fail()
    time.sleep(0.5)
    entrust_cutin(entrust,ensure)
    return True

def find_normal_enemy():
    find_elite = True
    if not attack_step(elites,wait_time=1):
        find_elite = False
    if not find_elite:
        if not attack_step(normals):
            print("failed to find enemy")
            # return False
            fail()
    return True

def wait_battle():
    while True:
        if scan(success):
            move(success)
            break
        time.sleep(2)
    # 再判断战斗结束
    time.sleep(1)
    move(success)

def battle_finish(wait_time):
    # 获得道具
    time.sleep(0.3)
    if not step(item, wait_time):
        # return False
        fail()
  
    # 经验结算
    time.sleep(0.3)
    if not step(finish, wait_time):
        print("可能出现新船")
        if not new_ship(newship, newship1):
            print("error")
            # return False
            fail()
        if not step(finish, wait_time):
            # return 
            fail()
    time.sleep(0.3)
    if not move(finish):
        # return False
        pass

    return True

def normal_battle(wait_time):
    if not find_normal_enemy():
        print("error")
        # return False
        fail()
    # 等待移动时间
    time.sleep(9)
    # 是否满船坞，清理
    if clear_ship():
        time.sleep(4)
        if not step(yingji, wait_time):
            print("迎击失败")
            # return False
            fail()
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

def boss_battle(wait_time):
    if not attack_step(boss):
        print("failed to find boss")
        # return False
        fail()
    # 等待移动时间
    time.sleep(6)
    # 是否满船坞，清理
    if clear_ship():
        time.sleep(4)
        if not step(yingji, wait_time):
            print("迎击失败")
            # return False
            fail()
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