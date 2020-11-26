import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl

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

from sys import version_info
if version_info.major != 3:
    raise Exception('请使用Python 3 来完成此项目')


# 导入知乎数据
zhihu_df = pd.read_csv('zhihu.csv')
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


# 对二手房区域分组对比二手房数量和每平米房价
df_house_count = df.groupby('Region')['Price'].count().sort_values(ascending=False).to_frame().reset_index()
df_house_mean = df.groupby('Region')['PerPrice'].mean().sort_values(ascending=False).to_frame().reset_index()

f, [ax1,ax2,ax3] = plt.subplots(3,1,figsize=(20,15))
sns.barplot(x='Region', y='PerPrice', palette="Blues_d", data=df_house_mean, ax=ax1)
ax1.set_title('北京各大区二手房每平米单价对比',fontsize=15)
ax1.set_xlabel('区域')
ax1.set_ylabel('每平米单价')

sns.barplot(x='Region', y='Price', palette="Greens_d", data=df_house_count, ax=ax2)
ax2.set_title('北京各大区二手房数量对比',fontsize=15)
ax2.set_xlabel('区域')
ax2.set_ylabel('数量')

sns.boxplot(x='Region', y='Price', data=df, ax=ax3)
ax3.set_title('北京各大区二手房房屋总价',fontsize=15)
ax3.set_xlabel('区域')
ax3.set_ylabel('房屋总价')

plt.show()

