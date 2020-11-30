from move import *
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
    if not scan(full):
        return False
    if not step(zhengli):
        return False
    time.sleep(0.5)
    while True:
        if not step(tuiyi):
            return False
        time.sleep(0.5)
        if scan(none):
            break
        if not step(queding):
            return False
        time.sleep(0.5)
        if not step(daoju):
            return False
        time.sleep(0.5)
        if not step(queding):
            return False
        time.sleep(0.5)
        if not step(queding):
            return False
        time.sleep(0.5)
        if not step(daoju):
            return False
        time.sleep(0.5)

    if not step(quxiao):
        return False
    print("clear ship successfully")
    return True

# 随机委托
def entrust_cutin(entrust,ensure):
    if not scan(entrust):
        return False
    if not step(ensure):
        return False
    print("entrust cutin")
    return True

def new_ship(newship,newship1):
    if not scan(newship) and not scan(newship1):
        return False
    if not step(newship,5,(0,200)) and not step(newship1,5,(0,200)):
        return False
    print("new ship")
    return True