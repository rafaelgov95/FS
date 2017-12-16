import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np

dataset=pd.read_csv("4sq_date_80000_ate_160000.txt",delimiter="\n")
dic = {'Arts_Entertainment':[],'Event':[],'Food':[],'Nightlife_Spot':[],'Outdoors_Recreation':[],'Professional_Other_Places':[],'Residence':[],'Shop_Service':[],'Travel_Transport':[]}
for i in dataset.values:
     d = json.loads(i[0])
     for a in  d["tips"]["tips content"]:
         for k in dic:
              if k == a["category"]:
                  dic[k].append(str(a["venue country"]))

k='Outdoors_Recreation'
b= set(dic[k])
print b
a={dic[k].count(x) for x in set(dic[k])}


men_means=[]
st=[]
rects1=[]
for v in dic:
    newList = []
    newRole = []
    a = {dic[v].count(x) for x in set(dic[v])}
    st.append(newList.extend(dic[v]))
    men_means.append(newRole.extend(a))
    N = len(a)

# men_std = (2, 3, 4, 1, 2)
#
    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars
#
    fig, ax = plt.subplots()
# rects1 = ax.bar(ind, men_means, width, color='r', yerr=men_std)
    rects1.append(ax.bar(ind, newRole, width, color='r'))
#
# women_means = (25, 32, 34, 20, 25)
# women_std = (3, 5, 2, 3, 3)
# rects2 = ax.bar(ind + width, women_means, width, color='y', yerr=women_std)
#
# # add some text for labels, title and axes ticks
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(st)
#
# ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))
#
#
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')
#
for i in range(0,len(rects1)):
    autolabel(rects1[i])
# autolabel(rects2)
#
plt.show()

















#
#
#
# grupos = len(b)
# data = (a, ('r', 'g', '#00FF33'), b)
# xPositions = np.arange(len(data[0]))
# barWidth = 0.50  # Largura da barra
# _ax = plt.axes()  # Cria axes
#
# # bar(left, height, width=0.8, bottom=None, hold=None, **kwargs)
# _chartBars = plt.bar(xPositions, data[0], barWidth, color=data[1],
#                      yerr=5, align='center')  # Gera barras
#
# xPositions = np.arange(len(data[0]))
# barWidth = 0.50  # Largura da barra
# _ax.set_xticks(xPositions)
# _ax.set_xticklabels(data[2])
# plt.xlabel(k)
# plt.ylabel('Check-ins')
# plt.grid(True)
# plt.legend(_chartBars, data[2])
# plt.show()