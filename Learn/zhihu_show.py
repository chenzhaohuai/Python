import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import os

import matplotlib.pyplot as plt
from IPython.display import display
plt.style.use("fivethirtyeight")
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
sns.set_style({'font.sans-serif':['simhei','Arial']})
# %matplotlib inline
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

display(mpl.matplotlib_fname())

print("当前路径 -> %s" , os.getcwd())
current_path = os.path.dirname(__file__)
print("current_path -> %s", current_path)


from sys import version_info
if version_info.major != 3:
    raise Exception('请使用Python 3 来完成此项目')


# 导入知乎数据
zhihu_df = pd.read_csv(current_path + '/zhihu.csv')
display(zhihu_df.head(n=2))

display(zhihu_df.describe())


df = zhihu_df.copy()
df['赞同和评论数'] = zhihu_df['答案赞同数'] + zhihu_df['答案评论数']

sexs = []
for sex in zhihu_df['答主性别']:
    if sex == 1:
        sexs.append('男')
    elif sex == 0:
        sexs.append('女')
    else:
        sexs.append('未知')

df['性别'] = sexs

columns = ['问题id','问题提问类型','答主用户名','答主签名','性别','答主粉丝数','答案赞同数','答案评论数','赞同和评论数','答案具体内容']
df = pd.DataFrame(df,columns = columns)

# 重新审视数据集
display(df.head(n=100))


df_sex_count = df.groupby('性别')['答主用户名'].count().sort_values(ascending=False).to_frame().reset_index()

display(df_sex_count)


# # 对二手房区域分组对比二手房数量和每平米房价
# df_house_count = df.groupby('Region')['Price'].count().sort_values(ascending=False).to_frame().reset_index()
# df_house_mean = df.groupby('Region')['PerPrice'].mean().sort_values(ascending=False).to_frame().reset_index()

# f, [ax1, ax2] = plt.subplots(2,1,figsize=(5,8))

# sns.barplot(x='性别', y='答主用户名', palette="Blues_d", data=df_sex_count, ax=ax1)
# ax1.set_title('知乎性别分布图',fontsize=15)
# ax1.set_xlabel('性别')
# ax1.set_ylabel('数量')

# _, [ax1, ax2] = plt.subplot(2,1, figsize=(6,6))


# plt.bar(df_sex_count['性别'], df_sex_count['答主用户名'])
labels = ['男','女','未知']
plt.pie(df_sex_count['答主用户名'],labels=labels,autopct='%1.1f%%')


plt.show()

