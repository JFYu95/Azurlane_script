from moving import *

class Map_8_4(object):
	"""docstring for Map_8_4"""
	def __init__(self):
		super(Map_8_4, self).__init__()
		# 静态量：
		# 地图标志物：敌舰队种类，问号，弹药，障碍物，x轴，y轴
		self.normals = []
		self.normals.append(cv2.imread('./pic/main.png'))
		self.normals.append(cv2.imread('./pic/defence.png'))
		self.x = cv2.imread('./pic/x.png')
		self.y = cv2.imread('./pic/y.png')
		self.space = cv2.imread('./pic/space.png')

		# 其他特征：确保的通路范围，boss坐标，地图移正需要的偏移量
		space_point = get_point(self.space)
		self.boss_point = (space_point[0], space_point[1]+115)
		self.correct = (-205,-205)

		x_vertex = get_vertex(self.x)
		y_vertex = get_vertex(self.y)
		self.route0 = (x_vertex[0],x_vertex[1],(x_vertex[0][0],y_vertex[2][1]),(x_vertex[1][0],y_vertex[2][1]))
		self.route1 = (y_vertex[1],(9999,y_vertex[1][1]),y_vertex[3],(9999,y_vertex[2][1]))
		# 动态量（每战更新）：
		# 所有敌人坐标，我方位置（保留）
		self.enemy_points = []
		self.ours = []
		# 函数
		# 获取所有敌人坐标 更新至动态量
		# 寻找通路内敌人 返回坐标列表

def main():
	m8_4 = Map_8_4()
	move(m8_4.x)
	print(m8_4.route0)
	print(m8_4.route1)
	mouse_drag(m8_4.correct)

if __name__ == '__main__':
	main()