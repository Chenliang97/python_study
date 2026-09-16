from die import Die
import plotly.express as px 

#创建1个 D6 和 1个D10
die_1 = Die()

die_2 = Die(10)

#掷骰子几次，将结果存储在一个列表中
results=[]

for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides

poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

#结果可视化
title = "Results of Rolling a D6 and a D10 50,000 Times"
labels = {'x':'Result','y':'Frequency of Results'}

fig = px.bar(x=poss_results, y=frequencies,title=title,labels=labels)

#进一步定制
fig.update_layout(xaxis_dtick=1)

fig.show()

fig.write_html('dice_visual_d6d10.html')   #也可以设置自动保存为html文件