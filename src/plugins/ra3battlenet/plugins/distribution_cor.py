from matplotlib import pyplot
from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, event, Bot, GroupMessageEvent, Message
import requests
import matplotlib.pyplot as plt


dw = on_fullmatch({"日冕段位分布"})

@dw.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    bar_labels = []
    values = []
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置显示中文字体
    plt.rcParams['axes.unicode_minus'] = False  # 设置正常显示符号
    records = requests.get("https://api.ra3battle.cn/api/stats/elo/distribution/corona/1v1/")
    for i in range(len(records.json()["records"])):
        ba=records.json()["records"][i]["rank"]
        if ba == "steel":
            ba = "钢铁"
        if ba == "copper":
            ba = "青铜"
        if ba == "silver":
            ba = "白银"
        if ba == "gold":
            ba = "黄金"
        if ba == "platium":
            ba = "白金"
        if ba == "diamond":
            ba = "钻石"
        if ba == "master":
            ba = "大师"
        va = records.json()["records"][i]["freq"]
        bar_labels.append(ba)
        values.append(va)
    # 创建柱状图
    bars = pyplot.bar(bar_labels, values)
    # 在每个柱形顶部显示数值
    for bar in bars:
        yval = bar.get_height()
        pyplot.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 1), ha='center', va='bottom')
    pyplot.savefig('C:/Users/Administrator/Desktop/yui/bkimg/bar_chart_cor.png')
    imge = f"file://C:/Users/Administrator/Desktop/yui/bkimg/bar_chart_cor.png"
    await dw.finish(MessageSegment.image(imge))