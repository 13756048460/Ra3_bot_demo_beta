from nonebot import on_keyword, on_fullmatch, on_command
from nonebot.adapters.onebot.v11 import MessageSegment,  Bot, GroupMessageEvent
from nonebot.typing import T_State
import xlrd
import nonebot
matcher = on_keyword({"护甲类型"})

@matcher.handle()
async def cf_(bot: Bot, event: GroupMessageEvent, state: T_State):
    get_msg = str(event.get_plaintext())
    print(get_msg)
    if get_msg =="护甲类型":
        await matcher.finish(MessageSegment.text("请输入单位名称+护甲类型"))
    fuc2 = get_msg[:-4]
    config = nonebot.get_driver().config
    files = config.files
    data_xls = xlrd.open_workbook_xls(f'{files}\image\Ra3dataBasepl2.xls')
    sheet1_object = data_xls.sheet_by_name(sheet_name="护甲类型")
    col_values = sheet1_object.col_values(0)
    print(col_values)
    print(fuc2)
    if fuc2 in col_values:
        for i in range(len(col_values)):
            if col_values[i] == fuc2:
                break

        all_row_values = sheet1_object.row_values(rowx=i)

        for i in range(len(all_row_values)):
            if all_row_values[i] == '':
                all_row_values[i] = "无"

        print("------------------------------" + "\n" + "单位：" + str(all_row_values[0]) + "\n" + "单位类型：" + str(
            all_row_values[1]) + "\n" + "最大血量：" + str(+all_row_values[2]) + "\n" + "护甲设置：" + str(
            all_row_values[3]) + "\n" + "侧面损伤加成：" + str(all_row_values[4]) + "\n" + "背面损伤加成：" + str(
            all_row_values[5]) + "\n" + "肉搏：" + str(all_row_values[6]) + "\n" + "狙击：" + str(
            all_row_values[7]) + "\n" + "枪弹：" + str(all_row_values[8]) + "\n" + "机炮：" + str(
            all_row_values[9]) + "\n" + "破片：" + str(all_row_values[10]) + "\n" + "火箭：" + str(
            all_row_values[11]) + "\n" + "穿甲：" + str(all_row_values[12]) + "\n" + "光谱：" + str(
            all_row_values[13]) + "\n" + "电击：" + str(all_row_values[14]) + "\n" + "高爆：" + str(
            all_row_values[15]) + "\n" + "榴弹：" + str(all_row_values[16]) + "\n" + "鱼雷：" + str(
            all_row_values[17]) + "\n" + "冲击：" + str(all_row_values[18]) + "\n" + "辐射：" + str(
            all_row_values[19]) + "\n" + "百分比：" + str(all_row_values[20]) + "\n" + "魔法：" + str(
            all_row_values[21]) + "\n" + "碾压：" + str(all_row_values[22]) + "\n" + "中子：" + str(
            all_row_values[23]) + "\n" + "不可抵抗：" + str(all_row_values[24]) + "\n" + "治疗：" + str(
            all_row_values[25]) + "\n" + "------------------------------")

        await matcher.finish(MessageSegment.text("------------------------------" + "\n" + "单位：" + str(all_row_values[0]) + "\n" + "单位类型：" + str(
            all_row_values[1]) + "\n" + "最大血量：" + str(+all_row_values[2]) + "\n" + "护甲设置：" + str(
            all_row_values[3]) + "\n" + "侧面损伤加成：" + str(all_row_values[4]) + "\n" + "背面损伤加成：" + str(
            all_row_values[5]) + "\n" + "肉搏：" + str(all_row_values[6]) + "\n" + "狙击：" + str(
            all_row_values[7]) + "\n" + "枪弹：" + str(all_row_values[8]) + "\n" + "机炮：" + str(
            all_row_values[9]) + "\n" + "破片：" + str(all_row_values[10]) + "\n" + "火箭：" + str(
            all_row_values[11]) + "\n" + "穿甲：" + str(all_row_values[12]) + "\n" + "光谱：" + str(
            all_row_values[13]) + "\n" + "电击：" + str(all_row_values[14]) + "\n" + "高爆：" + str(
            all_row_values[15]) + "\n" + "榴弹：" + str(all_row_values[16]) + "\n" + "鱼雷：" + str(
            all_row_values[17]) + "\n" + "冲击：" + str(all_row_values[18]) + "\n" + "辐射：" + str(
            all_row_values[19]) + "\n" + "百分比：" + str(all_row_values[20]) + "\n" + "魔法：" + str(
            all_row_values[21]) + "\n" + "碾压：" + str(all_row_values[22]) + "\n" + "中子：" + str(
            all_row_values[23]) + "\n" + "不可抵抗：" + str(all_row_values[24]) + "\n" + "治疗：" + str(
            all_row_values[25]) + "\n" + "------------------------------"))
    else:
        await matcher.finish("请输入正确的单位名称")
