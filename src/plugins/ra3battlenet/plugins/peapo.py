from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, event, Bot, GroupMessageEvent, Message
import requests

peapo = on_fullmatch("在线玩家列表")


@peapo.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    data = []
    url = "https://api.ra3battle.cn/api/server/status/detail"
    getjson = requests.get(url)
    num = len(getjson.json()["players"])
    t = 1
    for i in range(num):
        playerArr = getjson.json()["players"][i]
        var = playerArr["name"]
        if t % 3 == 0:
            var = var + "\n"
        t += 1
        data.append(var)
    out = "---".join(data)
    message = "在线玩家列表\n" + "在线玩家总人数：" + str(
        num) + "\n------------------------------\n" + out + "\n------------------------------"
    messages = [
        {
            "type": "node",
            "data": {
                "name": "房间数据",
                "uin": bot.self_id,
                "content": [MessageSegment.text(message)],
            },
        },
    ]
    res_id = await bot.call_api("send_forward_msg", messages=messages)
    await bot.send_group_msg(group_id=even.group_id, message=MessageSegment.forward(res_id))