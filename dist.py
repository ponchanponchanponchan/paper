


#file1 = '/Users/inaho/.vscode/datan1.xlsx'
#file2 = '/Users/inaho/.vscode/waypoints1221.xlsx'

import pandas as pd
import numpy as np

# Excelファイルのパス
excel_file_path= '/Users/inaho/.vscode/datan3.xlsx'

# Excelファイルを読み込む
df = pd.read_excel(excel_file_path)


# B軌跡の各点とA軌跡の最初の点との距離を計算
all_distances = [] 
for i in range(len(df['AX'])): #Aの軌跡の中のルーぷ
    # A軌跡の最初の座標（X座標とY座標）
    ax_start = df.iloc[i]['AX']
    ay_start = df.iloc[i]['AY']


    distances = []
    for j in range(len(df['BX'])):
        #bx_start = df.iloc[j]['BX']
        #by_start = df.iloc[j]['BY']
        distance = np.sqrt((ax_start - df.iloc[j]['BX'])**2 + (ay_start - df.iloc[j]['BY'])**2)

        distances.append(distance)

    dist = min(distances)
        
    all_distances.append(dist)

    

print(len(distances))
print(dist)
print(len(df['AX']))

# min_distancesをDataFrameに変換
result_df = pd.DataFrame({'all_distances': all_distances})

# 結果をエクセルファイルに書き込み
output_excel_path = '/Users/inaho/.vscode/sample1.xlsx'
result_df.to_excel(output_excel_path, index=False)
print(f"\n結果を {output_excel_path} に書き込みました。")
