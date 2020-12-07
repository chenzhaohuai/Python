
import numpy as np
import matplotlib.pyplot as plt  #引入画图库







a = [1,2,3,4,5,6,7,8]
b = np.array(a)
print(a,b)
print(type(a),type(b))

b = b.reshape(2,4)      #改变数组的维度
print(b)              #从原来的1x8变成2x4 （两行四列）
#元素访问
print("取第1行第2列元素：",b[1][2])  #注意是从0行0列开始数！！！


c = np.arange(6).reshape(2,3)
print(c)



stocks = 2000   # 2000支股票
days =  500  # 两年大约500个交易日
# 生成服从正态分布：均值期望＝0，标准差＝1的序列

stock_day = np.random.standard_normal((stocks, days))   
print(stock_day.shape)   #打印数据组结构
# 打印出前五只股票，头五个交易日的涨跌幅情况
print(stock_day[0:5, :20])


# 保留后250天的随机数据作为策略验证数据
keep_days = 250
# 统计前450, 切片切出0-250day，days = 500
stock_day_train = stock_day[:,0:days - keep_days]
# 打印出前250天跌幅最大的三支，总跌幅通过np.sum计算，np.sort对结果排序
print(np.sort(np.sum(stock_day_train, axis=1))[:3])
# 使用np.argsort针对股票跌幅进行排序，返回序号，即符合买入条件的股票序号
stock_lower = np.argsort(np.sum(stock_day_train, axis=1))[:3]
# 输出符合买入条件的股票序号
print(stock_lower)



#python定义函数使用def 函数名：然后enter
def buy_lower(stock):
    #设置一个一行两列的可视化图表
    _, axs=plt.subplots(nrows=1,ncols=2,figsize=(16,5))

    #绘制前450天的股票走势图，np.cumsum():序列连续求和
    axs[0].plot(np.arange(0,days-keep_days),
               stock_day_train[stock].cumsum())

    #从第250天开始到500天的股票走势
    buy=stock_day[stock][days-keep_days:days].cumsum()
    #绘制从第450天到500天中股票的走势图
    axs[1].plot(np.arange(days-keep_days,days),buy)
    #返回从第450天开始到第500天计算盈亏的盈亏序列的最后一个值
    return buy[-1]
#假设等权重地买入3只股票
profit=0  #盈亏比例
#遍历跌幅最大的3只股票序列序号序列
for stock in stock_lower:
    #profit即三只股票从第250天买入开始计算，直到最后一天的盈亏比例
    profit+=buy_lower(stock)
    print("买入第{}只股票，从第250个交易日开始持有盈亏：{:.2f}%".format(stock,profit))