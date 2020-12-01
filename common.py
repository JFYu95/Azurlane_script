from move import *
from config import *
import time


# 清理船坞
def clear_ship():
    if not scan(full):
        return False
    if not step(zhengli):
        return False
    # time.sleep(0.5)
    while True:
        if not step(tuiyi):
            return False
        time.sleep(0.5)
        if scan(none):
            break
        if not step(queding):
            return False
        # time.sleep(0.5)
        if not step(daoju):
            return False
        # time.sleep(0.5)
        if not step(queding):
            return False
        # time.sleep(0.5)
        if not step(queding):
            return False
        # time.sleep(0.5)
        if not step(daoju):
            return False
        # time.sleep(0.5)

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