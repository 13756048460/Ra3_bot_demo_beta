from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, event, Bot, GroupMessageEvent, Message
import requests

ph = on_fullmatch({"日冕段位排行","日冕段位数据"})

#单链表
class Node:
    #数据
    data = {
        "rank_elo":None,
        "name":None,
        "elo":None,
        "primaryFaction":None,
    }
    def __init__(self,data:data):
        self.data = data #数据域
        self.next = None #指针域

class LinkedList:
    def __init__(self):
        self.next = None #头节点

    #尾插法
    def insert(self,data):
        new_node = Node(data)
        if not self.next:
            self.next = new_node
            return
        last = self.next
        while last.next:
            last = last.next
        last.next = new_node
    #遍历单链表
    def display(self):
        current = self.next
        while current:
            print(current.data)
            current = current.next

    #遍历单链表，返回列表
    def display_lsit (self):
        current = self.next
        ls = []
        while current:
            ls.append(current.data)
            current = current.next
        return ls




def get_elo(jsons):
    nds = LinkedList()
    for i in jsons:
        rank = i["rank"]
        name = i["personaName"]
        elo = i["elo"]
        primaryFaction = i["primaryFaction"]
        if primaryFaction == "Empire":
            primaryFaction = "帝国"
        if primaryFaction == "Allied":
            primaryFaction = "盟军"
        if primaryFaction == "Soviet":
            primaryFaction = "苏联"
        if primaryFaction == "Celestial":
            primaryFaction = "神州"
        nds.insert({"rank_elo": rank, "name": name, "elo": elo, "primaryFaction": primaryFaction})
    return nds

@ph.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    # 获取赛季信息
    ba_name = requests.get("https://api.ra3battle.cn/api/stats/season/current/result")
    chineseName = ba_name.json()["chineseName"]
    englishName = ba_name.json()["englishName"]
    all_r = requests.get("https://api.ra3battle.cn/api/stats/1v1/factions/corona/0")
    cor = all_r.json()["Allied"]["byModFullName"]
    cor_name_num = len(list(cor.keys()))
    cor_name = list(cor.keys())[cor_name_num - 1]
    # 获取页数
    gets_pa = requests.get("https://api.ra3battle.cn/api/stats/ladder/ra3/1v1/records/page/1/result")
    total = gets_pa.json()["total"]
    pages = (int)(total / 100) + 1

    data = []
    for i in range(pages):
        gets = requests.get(f"https://api.ra3battle.cn/api/stats/ladder/corona/1v1/records/page/{i + 1}/result")
        records = gets.json()["records"]
        nds = get_elo(records).display_lsit()
        data.extend(nds)

    master_data = []
    diamond_data = []
    platium_data = []
    gold_data = []
    silver_data = []
    copper_data = []
    steel_data = []

    for i in data:
        if i["elo"] >= 1600:
            out = f"({i['rank_elo']})({i['name']})({i['elo']})({i['primaryFaction']})\n"
            master_data.append(out)
    master = ''.join(master_data)

    for i in data:
        if 1500 <= i["elo"] < 1600:
            out = f"({i['rank_elo']})({i['name']})({i['elo']})({i['primaryFaction']})\n"
            diamond_data.append(out)
    diamond = ''.join(diamond_data)

    for i in data:
        if 1300 <= i["elo"] < 1500:
            out = f"({i['rank_elo']})({i['name']})({i['elo']})({i['primaryFaction']})\n"
            platium_data.append(out)
    platium = ''.join(platium_data)

    for i in data:
        if 1100 <= i["elo"] < 1300:
            out = f"({i['rank_elo']})({i['name']})({i['elo']})({i['primaryFaction']})\n"
            gold_data.append(out)
    gold = ''.join(gold_data)

    for i in data:
        if 900 <= i["elo"] < 1100:
            out = f"({i['rank_elo']})({i['name']})({i['elo']})({i['primaryFaction']})\n"
            silver_data.append(out)
    silver = ''.join(silver_data)

    for i in data:
        if 700 <= i["elo"] < 900:
            out = f"({i['rank_elo']})({i['name']})({i['elo']})({i['primaryFaction']})\n"
            copper_data.append(out)
    copper = ''.join(copper_data)

    for i in data:
        if 1 <= i["elo"] < 700:
            out = f"({i['rank_elo']})({i['name']})({i['elo']})({i['primaryFaction']})\n"
            steel_data.append(out)
    steel = ''.join(steel_data)

    master_msg = (
        f"------------------------\n原版天梯段位排行榜\n赛季：{chineseName}  {englishName} 日冕版本：{cor_name}\n------------------------\n"
        "段位：大师\n"
        "排行  马甲名  ELO  主要国家"
        "\n----------------------------\n"
        f"{master}"
        "----------------------------")

    diamond_msg = (
        f"------------------------\n"
        "段位：钻石\n"
        "排行  马甲名  ELO  主要国家"
        "\n----------------------------\n"
        f"{diamond}"
        "----------------------------")

    platium__msg = (
        f"------------------------\n"
        "段位：白金\n"
        "排行  马甲名  ELO  主要国家"
        "\n----------------------------\n"
        f"{platium}"
        "----------------------------")

    gold_msg = (
        f"------------------------\n"
        "段位：黄金\n"
        "排行  马甲名  ELO  主要国家"
        "\n----------------------------\n"
        f"{gold}"
        "----------------------------")
    silver_msg = (
        f"------------------------\n"
        "段位：白银\n"
        "排行  马甲名  ELO  主要国家"
        "\n----------------------------\n"
        f"{silver}"
        "----------------------------")
    copper_msg = (
        f"------------------------\n"
        "段位：青铜\n"
        "排行  马甲名  ELO  主要国家"
        "\n----------------------------\n"
        f"{copper}"
        "----------------------------")
    steel_msg = (
        f"------------------------\n"
        "段位：钢铁\n"
        "排行  马甲名  ELO  主要国家"
        "\n----------------------------\n"
        f"{steel}"
        "----------------------------")

    messages = [
        {
            "type": "node",
            "data": {
                "name": "段位排行",
                "uin": bot.self_id,
                "content": [MessageSegment.text(master_msg)],
            },
        },
        {
            "type": "node",
            "data": {
                "name": "段位排行",
                "uin": bot.self_id,
                "content": [MessageSegment.text(diamond_msg)],
            },
        },
        {
            "type": "node",
            "data": {
                "name": "段位排行",
                "uin": bot.self_id,
                "content": [MessageSegment.text(platium__msg)],
            },
        },
        {
            "type": "node",
            "data": {
                "name": "段位排行",
                "uin": bot.self_id,
                "content": [MessageSegment.text(gold_msg)],
            },
        },
        {
            "type": "node",
            "data": {
                "name": "段位排行",
                "uin": bot.self_id,
                "content": [MessageSegment.text(silver_msg)],
            },
        },
        {
            "type": "node",
            "data": {
                "name": "段位排行",
                "uin": bot.self_id,
                "content": [MessageSegment.text(copper_msg)],
            },
        },
        {
            "type": "node",
            "data": {
                "name": "段位排行",
                "uin": bot.self_id,
                "content": [MessageSegment.text(steel_msg)],
            },
        },
    ]
    res_id = await bot.call_api("send_forward_msg", messages=messages)
    await bot.send_group_msg(group_id=even.group_id, message=MessageSegment.forward(res_id))