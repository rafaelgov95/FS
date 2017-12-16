import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import json
import numpy as np
#
fig, ax = plt.subplots()
earth = Basemap(ax=ax)
earth.drawcoastlines(color='#556655', linewidth=0.5)
dataset=pd.read_csv("4sq_date_10000_ate_10004.txt",delimiter="\n")
dic = {'Arts_Entertainment':['r'],'Event':['b'],'Food':[0,0,255,0.3],'Nightlife_Spot':['g'],'Outdoors_Recreation':['i'],'Professional_Other_Places':['k'],'Residence':['u'],'Shop_Service':['c'],'Travel_Transport':['j']}
for i in dataset.values:
     d = json.loads(i[0])
     for a in  d["tips"]["tips content"]:
         for k in dic:
              if k == a["category"]:
                  lat= a["location"][0]['lat']
                  lng= a["location"][0]['lng']
                  ax.scatter(lng,lat,c=str(dic[k][0]), alpha=0.5, zorder=1)
ax.set_xlabel("This month's 4.5M+ earthquakes")
fig.savefig('usgs-monthly-4.5M.png')