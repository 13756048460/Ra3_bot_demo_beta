from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, event, Bot, GroupMessageEvent, Message
import requests

zw = on_fullmatch({"战网阵营胜率","阵营胜率"})
rm = on_fullmatch({"战网日冕阵营胜率","日冕阵营胜率"})
def getAll():
    all = []
    all_r = requests.get("https://api.ra3battle.cn/api/stats/1v1/factions/ra3/0")
    Allied = all_r.json()["Allied"]["byModFullName"]["Red Alert 3 1.12"]
    Soviet = all_r.json()["Soviet"]["byModFullName"]["Red Alert 3 1.12"]
    Empire = all_r.json()["Empire"]["byModFullName"]["Red Alert 3 1.12"]
    all.append(Allied)
    all.append(Soviet)
    all.append(Empire)
    return all
def get_twelve():
    all = []
    all_r = requests.get("https://api.ra3battle.cn/api/stats/1v1/factions/ra3/3")
    Allied = all_r.json()["Allied"]["byModFullName"]["Red Alert 3 1.12"]
    Soviet = all_r.json()["Soviet"]["byModFullName"]["Red Alert 3 1.12"]
    Empire = all_r.json()["Empire"]["byModFullName"]["Red Alert 3 1.12"]
    all.append(Allied)
    all.append(Soviet)
    all.append(Empire)
    return all
def rm_getAll():
    all = []
    all_r = requests.get("https://api.ra3battle.cn/api/stats/1v1/factions/corona/0")
    cor = all_r.json()["Allied"]["byModFullName"]
    cor_name = list(cor.keys())[0]
    Allied = all_r.json()["Allied"]["byModFullName"][cor_name]
    Soviet = all_r.json()["Soviet"]["byModFullName"][cor_name]
    Empire = all_r.json()["Empire"]["byModFullName"][cor_name]
    Celestial = all_r.json()["Celestial"]["byModFullName"][cor_name]
    all.append(Allied)
    all.append(Soviet)
    all.append(Empire)
    all.append(Celestial)
    return all


def rm_get_twelve():
    all = []
    all_r = requests.get("https://api.ra3battle.cn/api/stats/1v1/factions/corona/3")
    cor = all_r.json()["Allied"]["byModFullName"]
    cor_name = list(cor.keys())[0]
    Allied = all_r.json()["Allied"]["byModFullName"][cor_name]
    Soviet = all_r.json()["Soviet"]["byModFullName"][cor_name]
    Empire = all_r.json()["Empire"]["byModFullName"][cor_name]
    Celestial = all_r.json()["Celestial"]["byModFullName"][cor_name]
    all.append(Allied)
    all.append(Soviet)
    all.append(Empire)
    all.append(Celestial)
    return all


@zw.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    alls = getAll()
    Alliedwins = alls[0]["wins"]
    Alliedtotal = alls[0]["total"]
    Sovietwins = alls[1]["wins"]
    Soviettotal = alls[1]["total"]
    Empirewins = alls[2]["wins"]
    Empiretotal = alls[2]["total"]
    # 总和
    sum = Empiretotal + Soviettotal + Alliedtotal
    # 1200
    twelve = get_twelve()
    t_Alliedwins = twelve[0]["wins"]
    t_Alliedtotal = twelve[0]["total"]
    t_Sovietwins = twelve[1]["wins"]
    t_Soviettotal = twelve[1]["total"]
    t_Empirewins = twelve[2]["wins"]
    t_Empiretotal = twelve[2]["total"]
    t_sum = t_Empiretotal + t_Soviettotal + t_Alliedtotal

    msg = (
        "----------------------------\n阵营胜率\n----------------------------"
        "\n阵营  胜率 使用率 胜场 场次\n----------------------------\n"
        f"盟军  {round(Alliedwins / Alliedtotal * 100, 2)}%  {round(Alliedtotal / sum * 100, 2)}%  {Alliedwins}  {Alliedtotal}\n"
        f"苏联  {round(Sovietwins / Soviettotal * 100, 2)}%  {round(Soviettotal / sum * 100, 2)}%  {Sovietwins}  {Soviettotal}\n"
        f"帝国  {round(Empirewins / Empiretotal * 100, 2)}%  {round(Empiretotal / sum * 100, 2)}%  {Empirewins}  {Empiretotal}\n"
        "----------------------------\n阵营胜率>=1200\n----------------------------"
        "\n阵营  胜率 使用率 胜场 场次\n----------------------------\n"
        f"盟军  {round(t_Alliedwins / t_Alliedtotal * 100, 2)}%  {round(t_Alliedtotal / t_sum * 100, 2)}%  {t_Alliedwins}  {t_Alliedtotal}\n"
        f"苏联  {round(t_Sovietwins / t_Soviettotal * 100, 2)}%  {round(t_Soviettotal / t_sum * 100, 2)}%  {t_Sovietwins}  {t_Soviettotal}\n"
        f"帝国  {round(t_Empirewins / t_Empiretotal * 100, 2)}%  {round(t_Empiretotal / t_sum * 100, 2)}%  {t_Empirewins}  {t_Empiretotal}\n"
        "----------------------------"
    )
    await  zw.finish(MessageSegment.text(msg))
    #
    # messages = [
    #     {
    #         "type": "node",
    #         "data": {
    #             "name": "阵营胜率",
    #             "uin": bot.self_id,
    #             "content": [MessageSegment.text(msg)],
    #         },
    #     },
    # ]
    # res_id = await bot.call_api("send_forward_msg", messages=messages)
    # await bot.send_group_msg(group_id=even.group_id, message=MessageSegment.forward(res_id))
@rm.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    all_r = requests.get("https://api.ra3battle.cn/api/stats/1v1/factions/corona/0")
    cor = all_r.json()["Allied"]["byModFullName"]
    cor_name_num = len(list(cor.keys()))
    cor_name = list(cor.keys())[cor_name_num - 1]
    rm_alls = rm_getAll()
    rm_Alliedwins = rm_alls[0]["wins"]
    rm_Alliedtotal = rm_alls[0]["total"]
    rm_Sovietwins = rm_alls[1]["wins"]
    rm_Soviettotal = rm_alls[1]["total"]
    rm_Empirewins = rm_alls[2]["wins"]
    rm_Empiretotal = rm_alls[2]["total"]
    rm_Celestialwins = rm_alls[3]["wins"]
    rm_Celestialtotal = rm_alls[3]["total"]
    # 总和
    rm_sum = rm_Empiretotal + rm_Soviettotal + rm_Alliedtotal + rm_Celestialtotal
    # 1200
    rm_twelve = rm_get_twelve()
    rm_t_Alliedwins = rm_twelve[0]["wins"]
    rm_t_Alliedtotal = rm_twelve[0]["total"]
    rm_t_Sovietwins = rm_twelve[1]["wins"]
    rm_t_Soviettotal = rm_twelve[1]["total"]
    rm_t_Empirewins = rm_twelve[2]["wins"]
    rm_t_Empiretotal = rm_twelve[2]["total"]
    rm_t_Celestialwins = rm_twelve[3]["wins"]
    rm_t_Celestialtotal = rm_twelve[3]["total"]
    rm_t_sum = rm_t_Empiretotal + rm_t_Soviettotal + rm_t_Alliedtotal + rm_t_Celestialtotal

    rm_msg = (
        f"日冕版本{cor_name}\n"
        "----------------------------\n日冕阵营胜率\n----------------------------"
        "\n阵营  胜率 使用率 胜场 场次\n----------------------------\n"
        f"盟军  {round(rm_Alliedwins / rm_Alliedtotal * 100, 2)}%  {round(rm_Alliedtotal / rm_sum * 100, 2)}%  {rm_Alliedwins}  {rm_Alliedtotal}\n"
        f"苏联  {round(rm_Sovietwins / rm_Soviettotal * 100, 2)}%  {round(rm_Soviettotal / rm_sum * 100, 2)}%  {rm_Sovietwins}  {rm_Soviettotal}\n"
        f"帝国  {round(rm_Empirewins / rm_Empiretotal * 100, 2)}%  {round(rm_Empiretotal / rm_sum * 100, 2)}%  {rm_Empirewins}  {rm_Empiretotal}\n"
        f"神州  {round(rm_Celestialwins / rm_Celestialtotal * 100, 2)}%  {round(rm_Celestialtotal / rm_sum * 100, 2)}%  {rm_Celestialwins}  {rm_Celestialtotal}\n"
        "----------------------------\n日冕阵营胜率>=1200\n----------------------------"
        "\n阵营  胜率 使用率 胜场 场次\n----------------------------\n"
        f"盟军  {round(rm_t_Alliedwins / rm_t_Alliedtotal * 100, 2)}%  {round(rm_t_Alliedtotal / rm_t_sum * 100, 2)}%  {rm_t_Alliedwins}  {rm_t_Alliedtotal}\n"
        f"苏联  {round(rm_t_Sovietwins / rm_t_Soviettotal * 100, 2)}%  {round(rm_t_Soviettotal / rm_t_sum * 100, 2)}%  {rm_t_Sovietwins}  {rm_t_Soviettotal}\n"
        f"帝国  {round(rm_t_Empirewins / rm_t_Empiretotal * 100, 2)}%  {round(rm_t_Empiretotal / rm_t_sum * 100, 2)}%  {rm_t_Empirewins}  {rm_t_Empiretotal}\n"
        f"神州  {round(rm_t_Celestialwins / rm_t_Celestialtotal * 100, 2)}%  {round(rm_t_Celestialtotal / rm_t_sum * 100, 2)}%  {rm_t_Celestialwins}  {rm_t_Celestialtotal}\n"
        "----------------------------"
    )
    await  rm.finish(MessageSegment.text(rm_msg))
    #
    # messages = [
    #     {
    #         "type": "node",
    #         "data": {
    #             "name": "阵营胜率",
    #             "uin": bot.self_id,
    #             "content": [MessageSegment.text(msg)],
    #         },
    #     },
    # ]
    # res_id = await bot.call_api("send_forward_msg", messages=messages)
    # await bot.send_group_msg(group_id=even.group_id, message=MessageSegment.forward(res_id))