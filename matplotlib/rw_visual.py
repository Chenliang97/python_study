import matplotlib.pyplot as plt 

from random_walk import RandomWalk

#只要程序是活动状态，就一直模拟随机游走
while True:
    #创建一个实例
    rw = RandomWalk(50_000)

    rw.fill_walk()

    #将所有的点都绘制出
    plt.style.use('classic')
    fig , ax = plt.subplots(figsize=(6,5),dpi=128)

    point_numbers = range(rw.num_points)

    ax.scatter(rw.x_values,rw.y_values,c=point_numbers , cmap = plt.cm.Blues,edgecolors = 'none',s=2)
    ax.set_aspect('equal')

    #突出起点和终点
    ax.scatter(0,0,c='green',edgecolors='none',s=30)
    ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=30)

    #隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)





    plt.show()

    keep_running = input("make another walk? (y/n): ")
    if keep_running == 'n':
        break

