#%%
# 1. 匯入套件 & 資料
# pip install plotly
import pandas as pd
import numpy as np
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.io as pio
import plotly.graph_objects as go
import plotly.express as px
pio.renderers.default = 'browser'
from show import showimg

# %%
# 動態圖寫法
# Line chart: https://plotly.com/python/line-charts/
# Pie chart: https://plotly.com/python/pie-charts/

fig = px.line(x = [1, 2, 3, 4],
              y = [4, 8, 12, 16] )

fig.update_layout(
    xaxis_title="some numbers",
    yaxis_title="love you" )

# 在notebook中產出檔案
fig.show()

# 產出html檔案
plot(fig, filename='love.html', auto_open=False)

#%%

# Output
showimg('./docs/plot_result.png')

# Input
showimg('./docs/input.png')


#%%
###########
# 讀入檔案 #
###########
data = pd.???(???, encoding="utf-8-sig")
datatmp = data[["Store", "Star Reviews"]]
#%%
###############
# 網路聲量分析 #
###############
showimg('./docs/calculation.png')

#%%
# 單點圓餅聲量計算
showimg("./docs/平均計算後.png")
df_count = data.groupby(???)[???].???

# 小數點取第三位
df_count["Star Reviews"] = ???

# 排名計算，並按照排名排序
df_count['Rank'] = df_count['Star Reviews'].???
df_count = df_count.sort_values(by="Rank")
df_count

#%%
###############
# 網路聲量繪圖 #
###############

# 單點圓餅圖

pie_fig = px.pie(???, values=???,
             names='Store')

pie_fig.update_traces( 
            labels= df_count['Store'],
            customdata = df_count['Rank'],
            texttemplate = "%{label}",
            hovertemplate = "%{label} <br>聲量: %{value} (%{percent:.2%}) </br>聲量排名: %{customdata}",
            hoverlabel = {'font_size': 20},
            textposition='auto',
            textfont={'family': "Courier New",
                    'size': 24,
                    'color':'white'},
            outsidetextfont = {'color': "black",
                            'size': 14},
            )

pie_fig.update_layout(
    title={
        'text': f"<b>網路「平均」聲量佔比圖</b>",
        'y':0.97,
        'x':0.5,
        'font': {'color':'black','size': 24}
        },
    #width=1060,
    #height=800,
    )

pie_fig.show()

# 匯出成果
plot(pie_fig, filename = "網路「平均」聲量佔比圖", auto_open=False)
# plot(pie_fig, filename = "".join([pie_fig['layout']['title']['text'].strip('</b>'),'.html']), auto_open=False)



# %%
#----------------- 問題：請問如何繪製出 網路「總」聲量佔比圖 -----------------


#%%
# 單點圓餅聲量計算
showimg("./docs/加總計算後.png")

# 小數點取第三位

# 排名計算，並按照排名排序


#%%
###############
# 網路聲量繪圖 #
###############

# 單點圓餅圖

# 匯出成果





