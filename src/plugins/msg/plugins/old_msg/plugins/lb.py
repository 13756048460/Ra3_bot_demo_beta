from nonebot import  on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, event, Bot, GroupMessageEvent, bot, Message

baike = on_fullmatch("百科列表")
szcx = on_fullmatch("查询列表")
zwsj = on_fullmatch("战网数据列表")
kksk = on_fullmatch("数值可查询列表")
hjkksk = on_fullmatch("护甲可查询列表")

@baike.handle()
async def _():
    await  baike.finish(Message("-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------" + "\n" + "查询列表"+"\n"+"官方七图"+"\n"+"最高机密协议"+"\n"+"护甲系统"+"\n"+"武器系统"+"\n" +"经验机制"+"\n"+"快捷键"+"\n"+"维修公式"+"\n"+"单位应变状态"+"\n"+"基础知识"+"\n"+"-------------------------"))

@szcx.handle()
async def _():
    await szcx.finish(Message("-------------------------\n如果有误请写出正确的信息并联系玖渚智心（Kunagisa Chitekina kokoro）：1549184870\n-------------------------\n协议查询列表\n血量查询列表\n价格查询列表\n建造时间查询列表\n-------------------------\n数值可查询列表\n单位+基础数值\n护甲可查询列表\n单位+护甲类型\n-------------------------"))

@zwsj.handle()
async def _():
    await  zwsj.finish(Message("-------------------------\n战网数据\n天梯排行\n阵营胜率\n日冕阵营胜率\n房间数据\n段位分布\n日冕段位分布\n段位排行\n日冕段位排行\n-------------------------"))
@kksk.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    message = "---------------\n警犬\n维和步兵\n标枪兵\n盟军工程师\n间谍\n谭雅\n盟军采矿车\n激流ACV\n多功能步兵战车\n守护者坦克\n幻影坦克\n雅典娜炮\n盟军基地车\n维和轰炸机\n阿波罗战斗机\n冰冻直升机\n世纪轰炸机\n海豚\n水翼船\n突袭驱逐舰\n航空母舰\n盟军建造基地\n发电厂\n新兵训练营\n盟军矿石精炼厂\n装甲工厂\n海港\n空军基地\n科技中心\n起重机(盟)\n盟军围墙\n多功能步兵炮塔\n光谱塔\n超时空传送仪\n质子撞击炮\n指挥中心\n侦察扫描无人机\n天空骑士\n天空骑士(航母锤)\n女神轰炸机\n时空炸弹\n高级时空炸弹\n超级时空炸弹\n打捞驳船\n总统的豪华轿车\n总统的直升机\n低调的苏联坦克\n盟8特殊警犬\n布莱顿沿岸炮台\n总统山胸像\n谷利芬了望台\n罗斯摩尔发射基地\n发电机核心\n道场核心\n矿石精炼厂核心\n机甲工厂核心\n码头核心\n电脑主机核心\n防卫者核心\n塔楼核心\n纳米虫群核心\n毁灭装置核心\n爆裂机器人\n帝国武士\n坦克杀手\n帝国工程师\n忍者\n火箭天使\n欧米伽百合子\n帝国采矿车\n迅雷运输艇\n天狗机器人\n海啸坦克\n打击者-VX\n鬼王\n波能坦克\n帝国基地车\n天狗战斗机\n直升机-VX\n天翼\n长枪迷你潜艇\n海翼\n薙刀巡洋舰\n将军战列舰\n帝国建造基地\n瞬息发电机\n瞬息道场\n帝国矿石精炼厂\n机甲工厂\n帝国码头\n纳米科技电脑主机\n帝国围墙\n防卫者-VX\n波能塔\n纳米虫群巢穴\n超能波毁灭装置\n天皇芳郎\n红鬼王\n将军刽子手\n货运艇\n帝国雷达舰\n大迅雷\n单点防御机器人\n气球炸弹\n神风无人机\n王子的雕像\n远距离雷达\n波能三门炮\n名椎道馆\n天西机械公司\n晋三之宅\n晋三之宅2\n战熊\n征召兵\n防空部队\n苏联工程师\n磁暴部队\n娜塔莎\n苏联采矿车\n史普尼克勘察车\n恐怖机器人\n镰刀机甲\n铁锤坦克\n磁暴坦克\n天启坦克\nV4导弹发射车\n苏联基地车\n双刃直升机\n米格战斗机\n基洛夫飞艇\n牛蛙战车\n磁暴快艇\n阿库拉潜艇\n无畏战列舰\n苏联建造基地\n反应堆\n军营\n苏联矿石精炼厂\n战争工厂\n海军船坞\n机场\n超级反应堆\n战斗研究所\n起重机回收厂\n苏联围墙\n哨兵枪\n高射炮\n磁暴线圈\n铁幕装置\n真空内爆弹发射井\n战斗碉堡\n前哨基地\n袋狸轰炸机\n磁力卫星\n造价回扣提示\n乌克兰火炮\n摩艾石像\n矿脉\n机场\n车库\n医院\n干船坞\n钻油塔\n前线哨塔\n精兵学院\n发射基地\n工业发电厂\n平民建筑物\n桥梁\n---------------"
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
@hjkksk.handle()
async def _(even: GroupMessageEvent, bot: Bot):
    message = "---------------\n警犬\n维和步兵\n维和步兵f\n标枪兵\n工兵(盟)\n间谍\n谭雅\n采矿车(盟)\n激流ACV\n多功能步兵战车\n守护者坦克\n幻影坦克\n雅典娜炮\n基地车(盟)\n维和轰炸机\n阿波罗战斗机\n冰冻直升机\n世纪轰炸机\n海豚\n水翼船\n突袭驱逐舰\n航空母舰\n建造基地(盟)\n发电厂\n新兵训练营\n矿石精炼厂\n装甲工厂\n海港\n空军基地\n科技中心\n起重机(盟)\n围墙(盟)\n多功能步兵炮塔\n光谱塔\n超时空传送仪\n质子撞击炮\n指挥中心\n侦察扫描无人机\n天空骑士\n天空骑士(航母锤)\n女神轰炸机\n时空炸弹\n高级时空炸弹\n超级时空炸弹\n布莱顿沿岸炮台\n总统山胸像\n谷利芬了望台\n罗斯摩尔发射基地\n打捞驳船\n总统的豪华轿车\n总统的直升机\n低调的苏联坦克\n盟8特殊警犬之一\n各种纳米核心\n防卫者核心\n塔楼核心\n爆裂机器人\n帝国武士\n坦克杀手\n坦克杀手F\n工兵(帝)\n忍者\n火箭天使\n欧米伽百合子\n采矿车(帝)\n迅雷运输艇\n天狗机器人\n海啸坦克\n打击者-VX\n鬼王\n波能坦克\n基地车(帝)\n天狗战斗机\n直升机-VX\n天翼\n长枪迷你潜艇\n海翼\n薙刀巡洋舰\n将军战列舰\n建造基地(帝)\n瞬息发电机\n瞬息道场\n矿石精炼厂\n机甲工厂\n帝国码头\n纳米科技电脑主机\n围墙(帝)\n防卫者-VX\n波能塔\n纳米虫群巢穴\n超能波毁灭装置\n天皇芳郎\n红鬼王\n将军刽子手\n货运艇\n帝国雷达舰\n大迅雷\n单点防御机器人\n气球炸弹\n神风无人机\n王子的雕像\n远距离雷达\n波能三门炮\n名椎道馆\n天西机械公司\n晋三之宅\n晋三之宅2\n战熊\n征召兵\n防空部队\n战斗工兵(苏)\n磁暴部队\n娜塔莎\n采矿车(苏)\n史普尼克勘察车\n恐怖机器人\n镰刀机甲\n铁锤坦克\n磁暴坦克\n天启坦克\nV4 导弹发射车\n基地车(苏)\n双刃直升机\n米格战斗机\n基洛夫飞艇\n牛蛙战车\n磁暴快艇\n阿库拉潜艇\n无畏战列舰\n建造基地(苏)\n反应堆\n军营\n矿石精炼厂\n战争工厂\n海军船坞\n机场\n超级反应堆\n战斗研究所\n起重机回收厂\n围墙(苏)\n哨兵枪\n高射炮\n磁暴线圈\n铁幕装置\n真空内爆弹发射井\n战斗碉堡\n前哨基地\n袋狸轰炸机\n磁力卫星\n造价回扣提示\n乌克兰火炮\n摩艾石像\n矿脉\n机场\n车库\n医院\n干船坞\n钻油塔\n前线哨塔\n精兵学院\n发射基地\n工业发电厂\n平民建筑物\n桥梁\n---------------"
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

