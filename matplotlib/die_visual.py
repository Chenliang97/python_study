from die import Die
import plotly.express as px 

#创建2个 D6
die_1 = Die()
die_2 = Die()

#掷骰子几次，将结果存储在一个列表中
results=[]

for roll_num in range(1000):
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
title = "Results of Rolling Two D6 1,000 Times"
labels = {'x':'Result','y':'Frequency of Results'}

fig = px.bar(x=poss_results, y=frequencies,title=title,labels=labels)

#进一步定制
fig.update_layout(xaxis_dtick=1)

fig.show()

