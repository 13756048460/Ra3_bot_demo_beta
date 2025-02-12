import json

from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, Bot, GroupMessageEvent
import requests
import nonebot
fj = ra3 = on_fullmatch({"正在准备房间", "房间数据", "正在准备的房间", "查找房间"})

@fj.handle()
async def _(event: GroupMessageEvent, bot: Bot):
    # 打开并加载翻译文件
    config = nonebot.get_driver().config
    files = config.files
    with open(f'{files}/zh.json', "r") as f:
        js = json.load(f)
    nameszh = js["Map"][0]
    nameszhar = js["Map"][1]
    nameszhars = js["Map"][2]

    # 获取服务器状态信息
    url = "https://api.ra3battle.cn/api/server/status"
    resq = requests.get(url)
    games = resq.json()["games"]
    data = []

    # 遍历每个游戏房间
    for game in games:
        hostname = game["hostname"]
        if game["gamemode"] == "openstaging":
            # 获取房主名称
            host_name = game["players"][0]["name"] if game["players"] else "Null"
            room_name = hostname.split()[1]

            # 获取MOD名称
            mod = {"RA3": "原版", "corona": "日冕"}.get(game["mod"], game["mod"])
            player_count = len(game["players"])

            # 获取并翻译地图名称
            map_name = game["mapname"].replace('\\', "/").split("/")[-1].split(".")[0].upper()
            map_name = nameszh.get(map_name, nameszhar.get(map_name, nameszhars.get(map_name, map_name)))

            # 获取并格式化玩家名称
            player_names = [f"{player['name']}{'(房主)' if i == 0 else ''}" for i, player in enumerate(game["players"])]
            player_names_str = '\n'.join(player_names)

            # 将房间信息添加到数据列表
            data.append(
                f"房间名：{room_name}\n"
                f"地图名：{map_name}\n"
                f"房主名：{host_name}\n"
                f"MOD名：{mod}\n"
                f"房间内人数：{player_count}\n"
                f"房间内玩家：{player_names_str}\n"
                "------------------------------\n"
            )

    # 构建最终消息内容
    message = f"正在准备的房间数：{len(data)}\n------------------------------\n" + ''.join(data)
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
    # 发送合并转发消息
    res_id = await bot.call_api("send_forward_msg", messages=messages)
    await bot.send_group_msg(group_id=event.group_id, message=MessageSegment.forward(res_id))