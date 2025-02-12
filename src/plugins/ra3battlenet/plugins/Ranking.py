from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, event, Bot, GroupMessageEvent, Message
import requests



ph = on_fullmatch({"战网天梯排行","天梯排行"})
@ph.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    get_records = requests.get("https://api.ra3battle.cn/api/stats/ladder/ra3/1v1/records/page/1/result").json()[
        "records"]
    data = []
    num = len(get_records)
    for i in range(num):
        if i == 40:
            break
        rec = get_records[i]
        rank = rec["rank"]
        personaName = rec["personaName"]
        elo = rec["elo"]
        primaryFaction = rec["primaryFaction"]
        if primaryFaction == "Empire":
            primaryFaction = "帝国"
        if primaryFaction == "Allied":
            primaryFaction = "盟军"
        if primaryFaction == "Soviet":
            primaryFaction = "苏联"
        if primaryFaction == "Celestial":
            primaryFaction = "神州"
        out =f"({rank}) ({personaName}) ({elo}) ({primaryFaction})\n"
        data.append(out)
    output = ''.join(data)

    rm_get_records = requests.get("https://api.ra3battle.cn/api/stats/ladder/corona/1v1/records/page/1/result").json()[
        "records"]
    rm_data = []
    rm_num = len(rm_get_records)
    for rm_i in range(rm_num):
        if rm_i == 40:
            break
        rm_rec = rm_get_records[rm_i]
        rm_rank = rm_rec["rank"]
        rm_personaName = rm_rec["personaName"]
        rm_elo = rm_rec["elo"]
        rm_primaryFaction = rm_rec["primaryFaction"]
        if rm_primaryFaction == "Empire":
            rm_primaryFaction = "帝国"
        if rm_primaryFaction == "Allied":
            rm_primaryFaction = "盟军"
        if rm_primaryFaction == "Soviet":
            rm_primaryFaction = "苏联"
        if rm_primaryFaction == "Celestial":
            rm_primaryFaction = "神州"
        rm_out = f"({rm_rank}) ({rm_personaName}) ({rm_elo}) ({rm_primaryFaction})\n"
        rm_data.append(rm_out)
    rm_output = ''.join(rm_data)

    all_r = requests.get("https://api.ra3battle.cn/api/stats/1v1/factions/corona/0")
    cor = all_r.json()["Allied"]["byModFullName"]
    cor_name_num = len(list(cor.keys()))
    cor_name = list(cor.keys())[cor_name_num - 1]

    ba_name = requests.get("https://api.ra3battle.cn/api/stats/season/current/result")
    chineseName = ba_name.json()["chineseName"]
    englishName = ba_name.json()["englishName"]


    msg = (f"------------------------\n战网原版1v1天梯\n赛季：{chineseName}  {englishName}\n------------------------\n"
           "排行  马甲名  ELO  主要国家"
           "\n----------------------------\n"
           f"{output}"
           "----------------------------")
    rm_msg = (
        f"------------------------\n日冕原版1v1天梯\n赛季：{chineseName}  {englishName}\n日冕版本号：{cor_name}\n------------------------\n"
        "排行  马甲名  ELO  主要国家"
        "\n----------------------------\n"
        f"{rm_output}"
        "----------------------------")
    messages = [
        {
            "type": "node",
            "data": {
                "name": "阵营胜率",
                "uin": bot.self_id,
                "content": [MessageSegment.text(msg)],
            },
        },
        {
            "type": "node",
            "data": {
                "name": "阵营胜率",
                "uin": bot.self_id,
                "content": [MessageSegment.text(rm_msg)],
            },
        },
    ]
    res_id = await bot.call_api("send_forward_msg", messages=messages)
    await bot.send_group_msg(group_id=even.group_id, message=MessageSegment.forward(res_id))

