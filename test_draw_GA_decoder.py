import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import numpy as np
import plotly.io as pio


insNameLst = ['']


insName = '14_14_ECCENTRIC_RANDOMCLUSTERED_SVLCV_LVLCV_thre0.1MPDAins.dat'
insName = '11_8_RANDOMCLUSTERED_CENTRAL_SVSCV_LVSCV_thre0.1MPDAins.dat'
insName = '20_20_CLUSTERED_RANDOM_QUADRANT_LVSCV_thre0.1MPDAins.dat'

figData = []

prefixDic = {'no_back':'.//debugData//GA_','back':'.//debugData//rc_GA_'}

for prefix in prefixDic:
    data_g = []
    data_fitness = []
    with open(prefixDic[prefix]+insName)  as txtData:
        lines = txtData.readlines()
        for line  in lines:
            lineData = line.split()
            if (len(lineData)==0):
                continue
            else:
                try:
                    g = int(lineData[0])
                except Exception as e:
                    break
                    # pass
                data_g.append(g)
                data_fitness.append(float(lineData[1]))
# print(data_g)
    trace = go.Scatter(mode = 'lines+markers', x = data_g, y = data_fitness, name= prefix)
    figData.append(trace)

layout = dict()
layout['xaxis'] = dict(title='gen')
layout['yaxis'] = dict(title='makespan')
fig = go.Figure(data=figData, layout=layout)
# pio.write_image(fig,'nothing')
plotly.offline.plot(fig, filename='.//plot//'+insName)
