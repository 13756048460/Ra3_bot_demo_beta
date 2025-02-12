from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, event, Bot, GroupMessageEvent, bot, Message
import nonebot

config = nonebot.get_driver().config
files = config.files

wqxt = on_fullmatch({"武器系统"})
hjxt = on_fullmatch({"护甲系统"})
zgjm = on_fullmatch({"最高机密协议"})
jyzj = on_fullmatch({"经验机制"})
kjj = on_fullmatch({"快捷键"})
wxgs = on_fullmatch({"维修公式"})
dwyb = on_fullmatch("单位应变状态")

@zgjm.handle()
async def _(bot: Bot, even: GroupMessageEvent):
    message = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n------------------------------\n最高机密协议不过是你能够使用的特殊支援技能的花哨术语。它们会作用于战场，你的敌人，以及你的单位和建筑。 基本上，他们能让你摆脱烦恼。记住了，你需要有至少一个建造厂才能使用它们。 每个派别都有一套自己的协议，有攻击型也有防御型的——有时则是两者兼备。\n随着战斗的进展，你会逐渐获取权限点，可以用来获取新协议。 你获得下一个权限点的进度显示在屏幕上的最高机密协议按钮周围的计量器上。 按钮上的数字是你当前的权限点数量。而每个协议都要花费1点权限点。\n顺便，你再每个阵营可用的协议是完全不同的。 所以即便你天神附体抢了一个敌人建造厂，也并不意味着他们高官会随随便便那样让你们把军事秘密一览无遗。是不是很有道理？\n下一个就是威胁指示器，这东西会给你一个关于当前在你周围发生了多少死亡和破坏的概念。 威胁指示器会在战斗中增加，特别是当你维持高伤亡时，它增长得更快，而你则能够更快地得到新的权限点。 威胁级别越高你的单位获得老兵经验的速度更快。威胁等级越高，你的单位就能更快地通过杀敌成为英雄级。\n威胁指示器：击杀一个单位时指示器值增加该单位经验的0.75倍，损失一个单位时指示器值增加该单位经验的3倍。 当指示器值为00000～12499时为黄色，每秒减少50，对经验值无影响 12500～37499时为橙色，每秒减少150，获取经验值增加50% 37500～50000时为红色，每秒减少300，获取经验值增加100%\n协议点数：当威胁指示器为黄/橙/红色时每秒增加1/1.5/2点科技点数，每累计360点科技点数则增加1点协议点数，三阵营开局自带1点协议点数，一局最多获取10点。\n------------------------------"
    messages = [
        {
            "type": "node",
            "data": {
                "name": "百科",
                "uin": bot.self_id,
                "content": [MessageSegment.text(message)],
            },
        }
    ]
    res_id = await bot.call_api("send_forward_msg", messages=messages)
    await bot.send_group_msg(group_id=even.group_id, message=MessageSegment.forward(res_id))
@jyzj.handle()
async def _():
    await jyzj.finish(MessageSegment.text("------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n------------------------------\n经验值问题：击杀无级/一级/二级/星级大部分单位可获得的基础经验值为其造价的1/2/3/4倍，大部分单位升级至一级/二级/星级所需基础经验值为其造价的3/6/9倍，部分单位经验值特殊，会在其对应的数据表中注明\n另外，经验值还受威胁等级影响，威胁指示器为橙色时，经验值获取增加50%，威胁指示器为红色时，经验值获取增加100%\n------------------------------"))

@wqxt.handle()
async def _():
    await wqxt.finish(MessageSegment.image(f'file://{files}/image/wqxt.png'))

@hjxt.handle()
async def _():
    await hjxt.finish(MessageSegment.image(f'file://{files}/image/hjxt.jpg'))

@kjj.handle()
async def _():
    await kjj.finish(MessageSegment.image("https://patchwiki.biligame.com/images/redalert3/2/21/40zpf0mbdqfi3rb8qi9n9l1omn66iwz.png"))

@wxgs.handle()
async def _():
    await wxgs.finish(MessageSegment.image("https://i0.hdslb.com/bfs/article/41a2bc50f3f5f14bc072fe08a454d8ab6fcbaa7e.png"))
@dwyb.handle()
async def _():
    await dwyb.finish(MessageSegment.image(f'file://{files}/image/dwyb.png'))