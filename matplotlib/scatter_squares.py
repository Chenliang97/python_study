import matplotlib.pyplot as plt

# plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

x_values =range(1,1001) #[1,2,3,4,5]
y_values =[x**2 for x in x_values] #[1,4,9,16,25]

#ax.scatter(x_values,y_values,color='red', s=1)  #加入颜色或者ax.scatter(x_values,y_values,color=(1,0.8,0),s=1),color中的3个数，依次表示红绿蓝的分量，0-1，对应颜色浓度逐渐变浅

#颜色映射
ax.scatter(x_values,y_values,c=y_values, cmap=plt.cm.Blues, s=1) 

#设置图题，并给坐标加上标签
# ax.plot(input_values,squares, linewidth=3)
# ax.set_title("square number",fontsize=24)
# ax.set_xlabel("value",fontsize=14)
# ax.set_ylabel("square of value", fontsize = 14)

# #设置刻度标记的样式
# ax.tick_params(labelsize=14)

#设置每个坐标轴的取值范围
ax.axis([0,1100,0,1_100_000])

ax.ticklabel_format(style='plain')  #刻度标记


plt.show()
plt.savefig('squares_plot.png', bbox_inches='tight')  #第一个实参是保存的文件名，第二个是裁剪掉多余的空白区