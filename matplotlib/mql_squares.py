import matplotlib.pyplot as plt 

input_values= [1,2,3,4,5]
squares = [1,4,9,16,25]

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()
ax.plot(input_values,squares, linewidth=3)
ax.set_title("square number",fontsize=24)
ax.set_xlabel("value",fontsize=14)
ax.set_ylabel("square of value", fontsize = 14)

#设置刻度标记的样式
ax.tick_params(labelsize=14)

plt.show()
