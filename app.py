import time
from move import *
from battle import *

def main():
    wait_time = 3
    # n = 5
    for t in range(6):
        # 进图
        print('times:',t)
        if not enter_field(wait_time):
            print("进图失败")
            return
        # 索敌等待
        time.sleep(4)
    

        # 地图位置校准
        mouse_click((1600*0.8,206*0.8))
        mouse_drag((-420,0))

        # 优先精英怪，道中n战
        for i in range(5):
            if not normal_battle(wait_time):
                print("道中战错误")
                return

        time.sleep(1)
        # 切换舰队
        if not step(switch,wait_time):
            return
        time.sleep(2.5)

        # # 地图位置校准
        mouse_click((1650*0.8,206*0.8))
        mouse_drag((-560,0))
        time.sleep(1)

        # if not normal_battle(wait_time):
        #   print("道中战错误")
        #   return

        # boss

        if not boss_battle(wait_time):
            print("boss战错误")
            return
        # input()
    

if __name__ == '__main__':
    # while True:
    main()

