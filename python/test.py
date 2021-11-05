import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(4)
scores = np.random.randint(25,100,size = 20)

df = pd.DataFrame(data=scores, columns=['score'])

bins = [0, 59, 70, 80, 100]
bins.sort(key=lambda x: -x)
print(bins)
df['type'] = '不及格'
df.loc[(59 < df['score']) & (df['score'] < 70), 'type'] = '良好'
# labels = ['不及格', '及格', '良好', '优秀']
# score_cut = pd.cut(df['score'], bins, labels=labels)
# df['type'] = score_cut
# print(df.loc[(df['type'] == '良好') & (df['score'] > 75), 'type'])
# print(df.groupby('type').mean().sort_values(by='score',ascending=False))
# print(df)