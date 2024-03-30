import json
import pandas as pd
from collections import Counter

df_orders = pd.read_excel('Перечень сформированных угроз.xlsx', sheet_name='Перечень угроз', usecols=['Меры защиты'])
df_li = df_orders.values.tolist()
df_1 = []
for s_li in df_li:
    df_1.append(s_li[0])

# print(df_1)
# print(len(df_1))

df_col = [element for element,count in Counter(df_1).most_common()]
print(df_col)

df = pd.DataFrame(df_col)
df.to_csv('protection_rating.csv')