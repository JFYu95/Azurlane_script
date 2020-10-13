import os
import sys
import time
from moving import *
from battle import *


gogo = cv2.imread('./pic/gogo.png')
success_ = cv2.imread('./pic/continue_.png')
item_ = cv2.imread('./pic/item_.png')
again = cv2.imread('./pic/again.png')
cutin = cv2.imread('./pic/cutin.png')

def main():

    val = 0.1
    wait_time = 5
    # n = 5
    for t in range(30):

        if not step(gogo, wait_time):
            return False
        time.sleep(0.6)
        move(cutin)
        # wait battle
        time.sleep(60)

        while True:
            if move(success_):
                break;
            time.sleep(2)
        # 再判断战斗结束
        time.sleep(1)
        move(success_)

        time.sleep(0.6)
        if not step(item_, wait_time):
            return False
        time.sleep(1)
        if not step(again, wait_time):
            return False
        time.sleep(1)

if __name__ == '__main__':

    main()

