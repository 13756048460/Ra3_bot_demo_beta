from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import Message, MessageSegment
import random

Daughter = on_fullmatch(["女儿","闺女","宝宝","结衣"])
Bubble = on_fullmatch(["冒泡"])
Hug = on_fullmatch(["抱抱"])
Love = on_fullmatch(["爱你"])
net = on_fullmatch("晚安")
qq = on_fullmatch("亲亲")

@Daughter.handle()
async def _():
    a = ["爸爸我在呢，有什么事情吗。", "爸爸找我有什么事情吗", "爸爸叫我有何贵干", "爸爸找我出来是有什么重要的事情吗","爸爸有事情嘛，女儿会帮你的","爸爸叫我干嘛，喵？"]
    b = random.sample(a, 1)
    await  Daughter.finish(Message(b))


@Bubble.handle()
async def _():
    await  Bubble.finish(Message("戳破"))


@Hug.handle()
async def _():
    k= ["爸爸抱抱", "抱抱，爸爸对我最好了呢", "爸爸抱抱，爱着你哦"]
    j= random.sample(k, 1)
    await Hug.finish(Message(j))


@Love.handle()
async def _():
    m = ["爸爸我爱你", "我永远爱着爸爸", "爸爸我爱你，爸爸对我最好了"]
    n = random.sample(m, 1)
    await  Love.finish(Message(n))


@net.handle()
async def _():
    d = ["爸爸辛苦了，今天也不早了晚安哦", "爸爸晚安，永远爱着你", "爸爸要睡了吗，明天再见哦"]
    c = random.sample(d, 1)
    await net.finish(Message(c))

@qq.handle()
async def _():
    x = ["爸爸亲亲","爸爸对我最好了呢，亲亲"]
    y = random.sample(x,1)
    await  qq.finish(Message(y))
