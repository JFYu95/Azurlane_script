import cv2
# config

# 子图相似度阈值，大于0.8
threshold = 0.8
# 分辨率校准,125%即乘以0.8的系数
resolution_rate = 0.8

# 全局
wait_time = 3 # 等待时间3s
n = 5         # 道中n战
e_n = 3       # 精英怪e_n战
e_n_count = [0] # 精英怪计数

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

# 一键清理船坞
full = cv2.imread('./pic/button/full.png')
zhengli = cv2.imread('./pic//button/zhengli.png')
tuiyi = cv2.imread('./pic/button/tuiyi.png')
queding = cv2.imread('./pic/button/queding.png')
daoju = cv2.imread('./pic/button/daoju.png')
none = cv2.imread('./pic/button/none.png')
yingji = cv2.imread('./pic/button/yingji.png')
quxiao = cv2.imread('./pic/button/quxiao.png')