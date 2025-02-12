from nonebot import on_keyword, on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, event, Bot, GroupMessageEvent, bot, Message

sl = on_fullmatch("协议查询列表")
slzx = on_fullmatch("苏联协议左线")
slzz = on_fullmatch("苏联协议中线")
slyx = on_fullmatch("苏联协议右线")
mjzx = on_fullmatch("盟军协议左线")
mzzz = on_fullmatch("盟军协议中线")
mzyx = on_fullmatch("盟军协议右线")
mzzy = on_fullmatch("盟军战役协议")
syzx = on_fullmatch(["升阳协议左线","帝国协议左线","升阳/帝国协议左线"])
syzz = on_fullmatch(["升阳协议中线","帝国协议中线","升阳/帝国协议中线"])
syyx = on_fullmatch(["升阳协议右线","帝国协议右线","升阳/帝国协议右线"])

@sl.handle()
async def _():
    await sl.finish(MessageSegment.text(
        "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n并且请联系维基百科编写人员，因为机器人百科是维基百科上扒下来的。\n------------------------------\n苏联协议左线\n苏联协议中线\n苏联协议右线\n------------------------------\n盟军协议左线\n盟军协议中线\n盟军协议右线\n盟军战役协议\n------------------------------\n升阳/帝国协议左线\n升阳/帝国协议中线\n升阳/帝国协议右线\n------------------------------"))

@slzx.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    message = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n并且请联系维基百科编写人员，因为机器人百科是维基百科上扒下来的。\n------------------------------\n研磨践踏：如果载具碾压步兵，将会播放特殊的声音效果，同时单位的血条上方会出现扳手图标（如果载具血量不是全满）。载具在该过程中回复的生命值取决于被碾压目标的血量。\n\n毒质腐蚀：腐蚀范围80，爆炸后范围污染伤害20，共65次，腐蚀目标10，轨迹伤害10，爆炸伤害5000，选择一个友方单位，使该单位被毒素污染，导致其持续受损，并在地面或海上传播有毒物质。如果被污染的单位被摧毁，它将爆炸造成伤害并在地图上扩散一团毒素，污染相当大的半径。\n\n磁力卫星：SPACE！！光标半径50，持续时间8s，冷却时间120s，预警时间2s\n\n超级磁力卫星：SPACE！！！！光标半径50，持续时间13s，冷却时间150s，预警时间2s\n\n终极磁力卫星：SPACE！！！！！！光标半径50，持续时间18s，冷却时间180s，预警时间2s\n------------------------------"
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
@slzz.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    message = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n并且请联系维基百科编写人员，因为机器人百科是维基百科上扒下来的。\n------------------------------\n恐怖机器人突袭：每当载具被摧毁时，有20%的几率会在载具的残骸中生成恐怖机器人。\n\n轨道坠落：退役3个空间探测器降落到目标位置，以及上次使用磁性卫星时升起的任何其他残骸，造成范围轻微伤害(会秒杀空中单位)，光标半径75，伤害300，伤害衰减至光标半径75，冷却时间180s，预警时间3s\n\n轨道倾斜：退役2个人造卫星降落到目标位置，以及上次使用磁性卫星时升起的任何其他残骸，造成范围中度伤害(会秒杀空中单位)，光标半径125，伤害500，伤害衰减至光标半径125，冷却时间240s，预警时间6s\n\n轨道骤雨：退役1个太空站降落到目标位置，以及上次使用磁力卫星时升起的任何其他残骸，造成范围高伤害(会秒杀空中单位)，光标半径175，伤害1500，伤害衰减之光标半径175，冷却时间300s，预警时间9s\n\n大规模生产：这一升级将使我方所有生产成本降低25%，友方则降低5%。友方受到的加成上限是25%，6人苏联算上自己加成和队友最大50%\n------------------------------"
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
@slyx.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    message = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n并且请联系维基百科编写人员，因为机器人百科是维基百科上扒下来的。\n------------------------------\n现金奖励：对半径范围内的所有单位和建筑实施30s赏金。如果任何赏金单位在期限内以任何方式被摧毁，协议使用方将获得单位建造成本25%的赏金。光标半径100，冷却时间120s\n\n生化空袭：可清理被驻扎的建筑物，獾式轰炸机沿基地到目标地为路线飞行，光标半径150，伤害20(共450次)，冷却时间180s，预警时间10s(信标5s)\n\n生化双重空袭：可清理被驻扎的建筑物，獾式轰炸机沿基地到目标地为路线飞行，光标半径150，伤害20(共450次)，冷却时间180s，预警时间10s(信标5s)\n\n生化三重空袭：可清理被驻扎的建筑物，獾式轰炸机沿基地到目标地为路线飞行，光标半径150，伤害20(共450次)，冷却时间180s，预警时间10s(信标5s)\n\n磁力奇点：吸引并固定附近的所有车辆，并立即杀死任何步兵单位，光标半径200，对步兵秒杀，冷却时间120s，预警时间5s\n------------------------------"
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
@mjzx.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    message = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n并且请联系维基百科编写人员，因为机器人百科是维基百科上扒下来的。\n------------------------------\n监视扫描：光标半径 150，两点之间直线，冷却时间120s\n\n精确打击：呼叫女神精准轰炸机对你指定的目标区进行猛烈轰炸！光标半径50，伤害575并掀翻周围步兵，3s（信标初始延迟1.5s，女神轰炸机逼近时间1.5s，生成高度500，攻击高度100，女神轰炸机沿基地到目标为路线飞行）\n\n超时空深渊：当被传送的物体传送后与传送碰撞列表内物体碰撞箱重合时会将两物体的血量相减最终留下血量大于零的物体，光标半径75，碰撞伤害（如果有），持续时间5s，冷却时间120s，预警时间1s\n\n超时空裂口：当被传送的物体传送后与传送碰撞列表内物体碰撞箱重合时会将两物体的血量相减最终留下血量大于零的物体，光标半径150，碰撞伤害（如果有），持续时间10s，冷却时间120s，预警时间1s\n\n超时空裂隙：当被传送的物体传送后与传送碰撞列表内物体碰撞箱重合时会将两物体的血量相减最终留下血量大于零的物体，光标半径250，碰撞伤害（如果有），持续时间15s，冷却时间120s，预警时间1s\n------------------------------"
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

@mzzz.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    message = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n并且请联系维基百科编写人员，因为机器人百科是维基百科上扒下来的。\n------------------------------\n先进航空学：增进盟军强大飞行器的耐久度、视野范围、载弹量和装填弹药时间，增加维和轰炸机、世纪轰炸机的弹药量以及为空军单位添加先进航空学效果模型，增加生命值(生命值请查看血量查询列表)，生效对象：维和轰炸机、阿波罗战斗机、冰冻直升机、世纪轰炸机\n\n冷冻打击：射击时间4s，在这期间每0.25秒使用一次小型冰冻武器，光标半径75，伤害中心1500，向外衰减至500，冷却时间120s，预警时间生成初级冷冻光束，存活时间5s\n\n冷冻轰击：射击时间6s，在这期间每0.25秒使用一次小型冰冻武器，光标半径125，伤害中心2250，向外衰减之750，冷却时间140s，预警时间生成中级冷冻光束，存活时间5s\n\n冷冻暴击：射击时间8s，在这期间每0.25秒使用一次大型冰冻武器，光标半径200，伤害中心3000，向外衰减至1000，冷却时间180s，预警时间生成高级冷冻光束，存活时间5s\n\n自由贸易：该协议生效后我方资源采集者每次资源采集量涨幅为25%，友方资源采集者的涨幅为5%，友方受到的加成上限是25%，6人盟军算上自己加成和队友最大50%，生效对象己方矿车和友方矿车\n------------------------------"
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

@mzyx.handle()
async def _(even: GroupMessageEvent, bot: Bot):

    message = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n并且请联系维基百科编写人员，因为机器人百科是维基百科上扒下来的。\n------------------------------\n高科技：军犬吠叫震晕敌人步兵时间：从10秒增加到15秒。 守护者坦克目标指示器的伤害加成：从50%提升到100%。 航母EMP导弹瘫痪效果：从10秒增加到13秒，作用半径从150增加到200。 冷冻直升机：冷冻光束输出从75增加到100，缩小光线效果持续时间从20秒增加到24秒，技能使用冷却时间减少75%。\n\n超时空互换：交换我方任意两个单位（可以是步兵）的位置。 互换距离每增加250从时空裂缝中相变为实体的时间相对增0.75s，在此期间单位无法动作但能被攻击。\n\n超时空炸弹：在指定地点生成定时炸药，光标半径20，伤害750，冷却时间120s，预警时间生成初级时空炸弹之种，存活时间3s，死亡生成时空炸弹，存活时间7s，死亡启用小型爆炸武器\n\n超级定时炸弹：在指定地点生成定时炸药，光标半径25，伤害1000，冷却时间240s，预警时间生成中级时空炸弹之种，存活时间3s，死亡生成高级时空炸弹，存活时间12s，死亡启用中型爆炸武器\n\n终极定时炸弹：在指定地点生成定时炸药，光标半径30，伤害1500，冷却时间360s，预警时间生成高级时空炸弹之种，存活时间3s，死亡生成超级时空炸弹，存活时间22s，死亡启用大型爆炸武器   \n------------------------------"
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
@mzzy.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    message = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n并且请联系维基百科编写人员，因为机器人百科是维基百科上扒下来的。\n------------------------------\n伞兵队：生成一架世纪轰炸机，内含1警犬、3维和步兵、1标枪，兵无法向悬崖施放，地图陆地空地有视野的范围,光标半径 100，冷却时间300s\n\n伞兵班：生成两架世纪轰炸机，内含1警犬、3维和步兵、1标枪，兵无法向悬崖施放，地图陆地空地有视野的范围,光标半径 120，冷却时间330s\n\n伞兵排：生成三架世纪轰炸机，内含1警犬、3维和步兵、1标枪，兵无法向悬崖施放，地图陆地空地有视野的范围,光标半径140，冷却时间360s\n------------------------------"
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
@syzx.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    message = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n并且请联系维基百科编写人员，因为机器人百科是维基百科上扒下来的。\n------------------------------\n强化舰队：生效单位帝国海军单位，单位减伤25%,速度x125%，清雾半径x125%\n\n惊骇伏击：分别在5个位置各生成1个坦克杀手，忙碌时间10s，不能在纳米虫群内与悬崖上释放，地图陆地空地有视野的范围，光标半径50，冷却时间210s\n\n气球炸弹：在这期间每隔0.5～2秒都会在半径0～50的范围内使用一次生成气球武器，（可以手动操作方向），共6次，光标半径100，伤害单个炸弹150，冷却时间180s，预警时间30s\n\n气球炸弹齐射：在这期间每隔0.5～2秒都会在半径0～75的范围内使用一次生成气球武器，共10次，（可以手动操作方向），光标半径150，伤害单个炸弹150，冷却时间240s，预警时间30s\n\n气球炸弹爆发：在这期间每隔0.5～2秒都会在半径0～100的范围内使用一次生成气球武器，共14次，（可以手动操作方向），光标半径200，伤害单个炸弹150，冷却时间300s，预警时间30s\n------------------------------"
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
@syzz.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    message = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n并且请联系维基百科编写人员，因为机器人百科是维基百科上扒下来的。\n------------------------------\n先进火箭匣：增加所有火箭天使、海翼、VX攻击机甲和VX直升机的射速，使他们的DPS（请查看百科列表的什么是DPS）获得约25%～50%不等的提升。\n\n决胜中队：神风无人机从距离目标地3000码处生成并沿基地到目标地的直线飞行，在这期间指引神风无人机撞击半径50内敌方非步兵目标，每个目标最多撞击2次，单个神风无人机机枪伤害5，作用半径1；无人机炸弹伤害100（光荣自爆升级后150），光标半径100，冷却时间120s，预警时间15s\n\n决胜中队X：神风无人机从距离目标地3000码处生成并沿基地到目标地的直线飞行，在这期间指引神风无人机撞击半径75内敌方非步兵目标，每个目标最多撞击3次，单个神风无人机机枪伤害5，作用半径1；无人机炸弹伤害100（光荣自爆升级后150），光标半径 150，冷却时间240s，预警时间15s\n\n决胜中队Ω：神风无人机从距离目标地3000码处生成并沿基地到目标地的直线飞行，在这期间指引神风无人机撞击半径100内敌方非步兵目标，每个目标最多撞击4次，单个神风无人机机枪伤害5，作用半径1；无人机炸弹伤害100（光荣自爆升级后150），光标半径 200，冷却时间360s，预警时间15s\n\n机械化组装：所有生产时间减少25%盟友也享受5%的减免，友方受到的加成上限是25%，6人升阳算上自己加成和队友最大50%，生效对象生产建筑，对围墙无效。\n------------------------------"
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

@syyx.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    message = "------------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n并且请联系维基百科编写人员，因为机器人百科是维基百科上扒下来的。\n------------------------------\n光荣自爆：载具被击毁时都自爆，产生半径50的高爆伤害，中心伤害200衰减至边缘伤害100。 矛式迷你潜艇自爆技能伤害从500到650(半径25到50)。 自爆无人机的自爆伤害从200到250(半径20到25)。 神风自杀机的自爆伤害从250到350(半径20到30)。作用单位为：发电机核心、道场核心、矿石精炼厂核心、机甲工厂核心、码头核心、电脑主机核心、防卫者核心、塔楼核心、纳米虫群核心、毁灭装置核心，天狗战斗机残骸、直升机-VX残骸、天翼残骸、神风无人机、无人机残骸，采矿车(帝)、迅雷运输艇、天狗机器人、海啸坦克、打击者-VX、鬼王、波能坦克、基地车(帝)、海翼、将军战列舰、薙刀巡洋舰，红鬼王、货运艇。并为以上单位(不含神风无人机)添加殉爆武器作为死亡武器。\n\n单点防御无人机：为你的部队提供保护无人机，这些无人机拥有200血量，能够存活119秒，护甲修正比除了辐射伤害为5%，所受的其他伤害均为100%，击毁这些无人机会获得200经验。护盾存在时间为119s，时间一到自动消失，护盾所受的最后一次致命攻击的多余伤害不会溢出到保护单位身上，护盾可以被维修，当单位与护盾同时受伤，维修顺序为维修护盾维修单位同时进行（两只维修蜂分别维修），光标半径100，冷却时间120s友方载具、大型载具、船只。不包括步兵、飞行器、潜艇，下潜状态、空中目标、在纳米虫群里、不在世界的、已附上单点防御机器人的单位，单点防御机器人。\n\n天皇之怒：持续时间30s，受影响单位减速25%,开火速率x125%（此协议不分敌我），光标半径 100，冷却时间120s，预警时间0s立即生效\n\n天皇复仇：持续时间40s，受影响单位减速25%,开火速率x150%（此协议不分敌我），光标半径 150，冷却时间120s，预警时间0s立即生效\n\n天皇惩戒：持续时间60s，受影响单位减速25%,开火速率x175%（此协议不分敌我），光标半径 200，冷却时间120s，预警时间0s立即生效\n------------------------------"
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