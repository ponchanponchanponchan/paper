import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.cm as cm

# colormapをカスタマイズする
from matplotlib.colors import LinearSegmentedColormap

def generate_cmap(colors):
    """自分で定義したカラーマップを返す"""
    values = range(len(colors))

    vmax = np.ceil(np.max(values))
    color_list = []
    for v, c in zip(values, colors):
        color_list.append( ( v/ vmax, c) )
    return LinearSegmentedColormap.from_list('custom_cmap', color_list)






 
# Excelファイルのパス
excel_file_path= '/Users/inaho/.vscode/datan1.xlsx'

# Excelファイルを読み込む
df = pd.read_excel(excel_file_path, usecols=[0,1,2,3,4])


df = df.rename(columns={"AX":"AX", \
                        "AY":"AY", \
                        "BX":"BX", \
                        "BY":"BY", \
                        "Unnamed: 4":"CC" })


x1 = df['AX'] # 横軸の値
y1 = df['AY'] # 縦軸の値
v1 = df['CC']

x2 = df['BX'] # 横軸の値
y2 = df['BY'] # 縦軸の値



fig, ax = plt.subplots()
ax.scatter(x2, y2, c="black", label="setting route", s=10)
cm = generate_cmap(['mediumblue', 'limegreen', 'orangered'])
mappable = ax.scatter(x1, y1, c=v1, cmap= cm, label="drive route", s=10,  vmin=0, vmax=3.5)
cbar = plt.colorbar(mappable, ax=ax)
cbar.set_label('distance from setting route (m)')


print (df.columns.values)
print(len(df['CC']))
plt.legend(bbox_to_anchor=(0.2, 1.13), loc='upper right', borderaxespad=0, fontsize=10)
 # 凡例
plt.show()


