from random import choice

class RandomWalk:
    """一个随机游走数据的类"""
    def __init__(self,num_points=5000):
        self.num_points = num_points

        #起点
        self.x_values=[0]
        self.y_values=[0]
    
    def fill_walk(self):
        """计算随机移动包含的点"""
        while len(self.x_values)<self.num_points:

            #前进方向以及沿这个方向的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #不能原地踏步
            if x_step == 0 and y_step == 0 :
                continue

            #下一个点
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)


