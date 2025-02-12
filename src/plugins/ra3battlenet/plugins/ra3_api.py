from nonebot import on_keyword, on_fullmatch, on_command

from nonebot.adapters.onebot.v11 import MessageSegment, event, Bot, GroupMessageEvent
import requests

ra3 = on_fullmatch(["战网数据","战网状态"])


@ra3.handle()
async def _():

    API_URL = "http://api.ra3battle.cn/api/server/status"

    getJson = requests.get(API_URL)
    # 玩家总数
    players = len(getJson.json()["players"])
    if not getJson.json()["players"] and not getJson.json()["games"]:
        msg = f"根据api获取json为\n-------------------\n{getJson.json()}\n-------------------\n获取players和games内的数据为空\n疑似战网崩溃或战网内暂无玩家\n如崩溃则联系战网管理"
        print(msg)
        await  ra3.finish(MessageSegment.text(msg))
    # 对局总数
    Total = getJson.json()["games"]
    # 正在对局玩家
    total_players = sum(len(game["players"]) for game in Total)
    # 闲置玩家
    Idle_player = players - total_players
    count1v1D = getJson.json()['automatching']['count1v1Details']
    count1v1 = count1v1D.get('ra3',0)
    count1v1R = count1v1D.get('corona', 0)
    mate_room = str(len(getJson.json()["automatch"]))
    # 正在进行游戏的房间个数
    closed_playing_count = sum(1 for game in Total if game["gamemode"] == 'closedplaying')
    # 正在准备的房间个数
    preparing_games = len(Total) - closed_playing_count
    # 输出
    print("------------------------------")
    print(f"当前在线人数：{players}")
    print(f"正在对局玩家：{total_players}")
    print(f"闲置玩家：{Idle_player}")
    print("------------------------------")
    print(f"1v1自动匹配正在寻找对局的玩家为：{count1v1}")
    print(f"1v1日冕自动匹配正在寻找对局的玩家为：{count1v1R}")
    print("------------------------------")
    print(f"正在进行匹配对战的房间总数：{mate_room}")
    print(f"正在进行游戏的房间个数：{closed_playing_count}")
    print(f"正在准备的房间个数：{preparing_games}")
    print("------------------------------")
    print("\n")
    over = "--------------------" + "\n" + "详细房间内容请输入”房间数据“" + "\n" + "--------------------" + \
           "\n" + f"当前在线人数：{players}" + "\n" + f"正在对局玩家：{total_players}" + "\n" + f"闲置玩家：{Idle_player}" + "\n" + \
           "--------------------" + "\n" + f"1v1自动匹配正在寻找对局的玩家为：{count1v1}" + "\n" +f"1v1日冕自动匹配正在寻找对局的玩家为：{count1v1R}"+"\n"+ "--------------------" + "\n" + \
           f"正在进行匹配对战的房间总数：{mate_room}" + "\n" + f"正在进行游戏的房间个数：{closed_playing_count}" + "\n" + f"正在准备的房间个数：{preparing_games}" + "\n" + \
           "--------------------"
    print(over)
    print("\n")
    await  ra3.finish(MessageSegment.text(over))
