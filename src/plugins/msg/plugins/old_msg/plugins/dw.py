from nonebot import on_keyword, on_fullmatch, on_command
from nonebot.internal.params import ArgPlainText
from nonebot.adapters.onebot.v11 import MessageSegment, event, Bot, GroupMessageEvent
from nonebot.params import Received

from nonebot.typing import T_State
import xlrd
import nonebot
matcher = on_keyword({"基础数值"})

@matcher.handle()
async def cf_(bot: Bot, event: GroupMessageEvent, state: T_State):
    get_msg = str(event.get_plaintext())
    print(get_msg)
    if get_msg =="基础数值":
        await matcher.finish(MessageSegment.text("请输入单位名称+基础数值"))
    fuc2 = get_msg[:-4]
    config = nonebot.get_driver().config
    files = config.files
    data_xls = xlrd.open_workbook_xls(f'{files}\image\Ra3dataBase.xls')
    sheet1_object = data_xls.sheet_by_name(sheet_name="基础数值")
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

        print("------------------------------" + "\n" +
              "单位：" + all_row_values[0] + "\n" + "单位类型:" + all_row_values[1] + "\n" + "最大血量:" + str(
            all_row_values[2]) + "\n" + "建造/训练时长:" + str(all_row_values[3]) + "\n" + "价格:" + str(
            all_row_values[4]) + "\n" + "生产前提:" + str(all_row_values[5]) + "\n" +
              "------------------------------" + "\n" +
              "运动设定" + "\n" + "陆地:" + str(all_row_values[6]) + "  水域:" + str(all_row_values[7]) + "  空中:" + str(
            all_row_values[8]) + "  升降:" + str(all_row_values[9]) + "  特殊:" + str(all_row_values[10]) + "\n" +
              "------------------------------" + "\n" +
              "通常状态高度:" + str(all_row_values[11]) + "\n" + "警戒半径:" + str(
            all_row_values[12]) + "\n" + "清雾半径:" + str(all_row_values[13]) + "\n" + "碾压等级:" + str(
            all_row_values[14]) + "\n" + "被碾压等级:" + str(all_row_values[15]) + "\n" +
              "额外的碾压等级:" + "\n" + "碾压等级:" + str(all_row_values[16]) + "  被碾压等级:" + str(
            all_row_values[17]) + "  情况:" + str(all_row_values[18]) + "\n" +
              "产能:" + str(all_row_values[19]) + "\n" +
              "------------------------------" + "\n" +
              "经验奖励:" + "\n" + "新兵:" + str(all_row_values[20]) + "  老兵:" + str(
            all_row_values[21]) + "  精英:" + str(all_row_values[22]) + "  英雄:" + str(all_row_values[23]) + "\n" +
              "经验需求:" + "\n" + "新兵:" + str(all_row_values[24]) + "  老兵:" + str(
            all_row_values[25]) + "  精英:" + str(all_row_values[26]) + "  英雄:" + str(all_row_values[27]) + "\n" +
              "------------------------------")

        await matcher.finish(MessageSegment.text("------------------------------"+"\n"+
          "单位："+all_row_values[0]+"\n"+"单位类型:"+all_row_values[1]+"\n"+"最大血量:"+str(all_row_values[2])+"\n"+"建造/训练时长:"+str(all_row_values[3])+"\n"+"价格:"+str(all_row_values[4])+"\n"+"生产前提:"+str(all_row_values[5])+"\n"+
          "------------------------------"+"\n"+
          "运动设定"+"\n"+"陆地:"+str(all_row_values[6])+"  水域:"+str(all_row_values[7])+"  空中:"+str(all_row_values[8])+"  升降:"+str(all_row_values[9])+"  特殊:"+str(all_row_values[10])+"\n"+
          "------------------------------"+"\n"+
          "通常状态高度:"+str(all_row_values[11])+"\n"+"警戒半径:"+str(all_row_values[12])+"\n"+"清雾半径:"+str(all_row_values[13])+"\n"+"碾压等级:"+str(all_row_values[14])+"\n"+"被碾压等级:"+str(all_row_values[15])+"\n"+
          "额外的碾压等级:"+"\n"+"碾压等级:"+str(all_row_values[16])+"  被碾压等级:"+str(all_row_values[17])+"  情况:"+str(all_row_values[18])+"\n"+
          "产能:"+str(all_row_values[19])+"\n"+
          "------------------------------"+"\n"+
          "经验奖励:"+"\n"+"新兵:"+str(all_row_values[20])+"  老兵:"+str(all_row_values[21])+"  精英:"+str(all_row_values[22])+"  英雄:"+str(all_row_values[23])+"\n"+
          "经验需求:"+"\n"+"新兵:"+str(all_row_values[24])+"  老兵:"+str(all_row_values[25])+"  精英:"+str(all_row_values[26])+"  英雄:"+str(all_row_values[27])+"\n"+
          "------------------------------"))
    else:
        await matcher.finish("请输入正确的单位名称")
