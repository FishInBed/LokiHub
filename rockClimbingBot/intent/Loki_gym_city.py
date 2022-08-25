#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for gym_city

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json
import os
import random
import pandas as pd
from rockClimbingFunc import gymCountySet
from rockClimbingFunc import getGymLocPh
from rockClimbingFunc import getBTScity
from rockClimbingFunc import getGymPrice


DEBUG_gym_city = True
try:
    userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
except:
    userDefinedDICT = {"_pants":["單車褲","瑜珈褲","短褲","運動褲"],"_rocks":["岩石","岩點","手點","攀岩鞋","攀岩鞋子","石頭","點"],"_shoes":["岩鞋","抱石鞋","鞋子"],"_sides":["中部","北部","南部","東部","西部"],"_tmpFix":["規則"],"_whatIs":["星光票"],"_clothes":["上衣","服裝","短袖","短袖上衣","短袖衣服","衣服","衣著","衣褲","長袖","長袖上衣","長袖衣服"],"_climbing":["上攀","先鋒","先鋒攀","先鋒攀岩","先鋒攀登","抱石","抱石攀岩","速度攀","速度攀登"],"_cityAlias":["區域","地區","城市","縣市","都市"],"_gymsShort":["8a攀岩場","B-plus","Boulder Space","Camp 4","Corner","Dapro","K2","MegaSTONE","POGO","TheDepotCity","Up聯盟","Y17","double 8","double8","久淘","千手抱石","原岩","嗨翻","嘉義攀岩會館","圓石","圓石空間","宜蘭運動中心","小岩館","崩岩","抱石基地","攀吶","新竹紅石","水美iClimb","汐止抱石館","爬森","破舊二廠","破舊工廠","禾匠","紅石","艾思博","蕃薯藤","角岩館","風城"],"_peClothes":["單車褲","瑜珈褲","運動服","運動衣","運動褲","運動鞋"],"_rockTypes":["crimp","edge","flat","horn","jug","pinch","pocket","sloper","volume"],"_climbingGym":["岩場","岩館","攀岩場","攀岩館"],"_taiwanAlias":["全台","全台各地","全臺","全臺各地","台灣","臺灣"],"_climbingEquip":["岩粉","岩點刷","攀岩刷","攀岩粉","攀岩粉袋","止滑粉","碳酸鎂粉","粉球","粉袋","裝","裝備","鎂粉","鎂粉球"],"_topRopingEquip":["吊帶","垂降手套","安全吊帶","安全扣","安全扣環","快扣","手套","確保器","確保手套","耐磨手套"]}

defaultResponse = json.load(open("data/defaultResponse.json",encoding="utf-8"))
# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_gym_city:
        print("[gym_city] {} ===> {}".format(inputSTR, utterance))

def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    if utterance == "[double 8]在哪個[縣市]":
        pass
        # if args[0] in userDefinedDICT["_gymsShort"]:
        #     resultDICT["_gym_name"] = args[0]
        #     if args[1] in userDefinedDICT["_cityAlias"]:
        #         cityDict = getGymLocPh(args[0], "c")
        #         if len(cityDict) == 1:
        #             resultDICT["reply_gym_location"] = "{0}在{1}".format(list(cityDict)[0], list(cityDict.values())[0])
        #         else:
        #             tmp = ""
        #             for gym, loc in cityDict.items():
        #                 tmp += "{0}在{1}\n".format(gym, loc)
        #             resultDICT["reply_gym_location"] = tmp
        #     elif args[1] == "位置":
        #         addDict = getGymLocPh(args[0], "a")
        #         if len(cityDict) == 1:
        #             resultDICT["reply_gym_location"] = "{0}在{1}".format(list(cityDict)[0], list(cityDict.values())[0])
        #         else:
        #             tmp = ""
        #             for gym, loc in cityDict.items():
        #                 tmp += "{0}在{1}\n".format(gym, loc)
        #     else:
        #         resultDICT["reply_gym_location"] = random.choice(defaultResponse["_question_not_know"])
        # elif args[0] in userDefinedDICT["_climbingGym"]:
        #     gymName = utterance.split("[")[0]
        #     if gymName in userDefinedDICT["_gymsShort"]:
        #         resultDICT["_gym_name"] = gymName
        #         if args[1] in userDefinedDICT["_cityAlias"]:
        #             citySet = getGymLocPh(gymName, "c")
        #             resultDICT["reply_gym_location"] = "{0}在{1}".format(gymName, str(citySet))
        #         elif args[1] == "位置":
        #             addSet = getGymLocPh(gymName, "a")
        #             resultDICT["reply_gym_location"] = "{0}的位置是：{1}".format(gymName, str(addSet))
        #         else:
        #             resultDICT["reply_gym_location"] = random.choice(defaultResponse["_question_not_know"])
        #     else:
        #         resultDICT["reply_gym_location"] = "台灣沒有這間岩館哦"
        # else:
        #     resultDICT["reply_gym_location"] = "台灣沒有這間岩館哦"

    if utterance == "[double 8]在哪裡":
        pass
        # if args[0] in userDefinedDICT["_gymsShort"]:
        #     cityDict = getGymLocPh(args[0], "a")
        #     if len(cityDict) == 1:
        #         resultDICT["reply_gym_location"] = "{0}在{1}".format(list(cityDict)[0], list(cityDict.values())[0])
        #     else:
        #         tmp = ""
        #         for gym, loc in cityDict.items():
        #             tmp += "{0}在{1}\n".format(gym, loc)
        #             resultDICT["reply_gym_location"] = tmp
        # elif args[0] in userDefinedDICT["_climbingGym"]:
        #     gymName = utterance.split("[")[0]
        #     if gymName in userDefinedDICT["_gymsShort"]:
        #         resultDICT["_gym_name"] = gymName
        #         addSet = getGymLocPh(gymName, "a")
        #         resultDICT["reply_gym_location"] = "{0}的位置是：{1}".format(gymName, str(addSet))
        #     else:
        #         resultDICT["reply_gym_location"] = "台灣沒有這間岩館哦"
        # else:
        #     resultDICT["reply_gym_location"] = "台灣沒有這間岩館哦"

    if utterance == "[可以]告訴[我][double 8]的[地址]嗎":
        pass
        # if args[2] in userDefinedDICT["_gymsShort"]:
        #     resultDICT["_gym_name"] = args[2]
        #     if args[3] in ("地址","位置"):
        #         cityDict = getGymLocPh(args[3], "a")
        #         if len(cityDict) == 1:
        #             resultDICT["reply_gym_location"] = "{0}在{1}".format(args[3], str(citySet))
        #         else:
        #             tmp = ""
        #             for gym, loc in cityDict.items():
        #                 tmp += "{0}在{1}\n".format(gym, loc)
        #             resultDICT["reply_gym_location"] = tmp
        #     elif "價" in args[3]:
        #         priceSet = getGymPrice(arg[2])
        #         for i in range(len(priceSet)):
        #             if i[1] != "na":
        #                 resultDICT["reply_gym_price"] = "{0}的平日票價為{1}、假日票價為{2}、星光飄價為{3}".format(i[0],i[1],i[2],i[3])
        #             else:
        #                 resultDICT["reply_gym_price"] = "{0}的票價是以小時計算，價格為{1}".format(i[0],i[4])
        #     elif "電話" in args[3]:
        #         phoneDict = getGymLocPh(args[3], "p")
        #         if len(cityDict) == 1:
        #             resultDICT["reply_gym_location"] = "{0}在{1}".format(args[3], str(citySet))
        #         else:
        #             tmp = ""
        #             for gym, loc in cityDict.items():
        #                 tmp += "{0}在{1}\n".format(gym, loc)
        #     else:
        #         resultDICT["reply_gym_location"] = random.choice(defaultResponse["_question_not_know"])
        # elif args[2] in userDefinedDICT["_climbingGym"]:
        #     resultDICT["reply_gym_location"] = "請問想問哪間岩館呢？"
        # else:
        #     resultDICT["reply_gym_location"] = "台灣沒有這間岩館哦"

    if utterance == "[可以]給[我][double 8]的[地址]嗎":
        pass
        # if args[2] in userDefinedDICT["_gymsShort"]:
        #     resultDICT["reply_gym_name"] = args[2]
        #     if args[3] in ("地址","位置"):
        #         cityDict = getGymLocPh(args[0], "a")
        #         if len(cityDict) == 1:
        #             resultDICT["reply_gym_location"] = "{0}在{1}".format(args[0], str(citySet))
        #         else:
        #             tmp = ""
        #             for gym, loc in cityDict.items():
        #                 tmp += "{0}在{1}\n".format(gym, loc)
        #     elif "價" in args[3]:
        #         priceSet = getGymPrice(arg[2])
        #         for i in range(len(priceSet)):
        #             if i[1] != "na":
        #                 resultDICT["reply_gym_price"] = "{0}的平日票價為{1}、假日票價為{2}、星光飄價為{3}".format(i[0],i[1],i[2],i[3])
        #             else:
        #                 resultDICT["reply_gym_price"] = "{0}的票價是以小時計算，價格為{1}".format(i[0],i[4])
        #     elif "電話" in args[3]:
        #         phoneDict = getGymLocPh(args[0], "p")
        #         if len(cityDict) == 1:
        #             resultDICT["reply_gym_location"] = "{0}在{1}".format(args[0], str(citySet))
        #         else:
        #             tmp = ""
        #             for gym, loc in cityDict.items():
        #                 tmp += "{0}在{1}\n".format(gym, loc)
        #     else:
        #         resultDICT["reply_gym_location"] = random.choice(defaultResponse["_question_not_know"])
        # elif args[2] in userDefinedDICT["_climbingGym"]:
        #     resultDICT["reply_gym_location"] = "請問想問哪間岩館呢？"
        # else:
        #     resultDICT["reply_gym_location"] = "台灣沒有這間岩館哦"

    if utterance == "[台灣]哪些[縣市]有[岩館]呢":
        pass
        # if args[2] not in userDefinedDICT["_climbingGym"]:
        #     resultDICT["reply_gym_name"] = random.choice(defaultResponse["_not_rock_climbing"])
        #     return resultDICT
        # if args[0] in userDefinedDICT["_taiwanAlias"]:
        #     if args[1] in userDefinedDICT["_cityAlias"]:
        #         citySet = gymCountySet()
        #         resultDICT["reply_gym_location"] = "{0}有岩館的{1}有：{2}".format(args[0], args[1], str(citySet))
        # else:
        #     resultDICT["reply_gym_location"] = "台灣以外的事物我不清楚欸"

    if utterance == "[新竹紅石]的[地址]是？":
        pass
        # if args[0] in userDefinedDICT["_gymsShort"]:
        #     resultDICT["reply_gym_name"] = args[0]
        #     if args[1] in ("地址","位置"):
        #         cityDict = getGymLocPh(args[0], "a")
        #         if len(cityDict) == 1:
        #             resultDICT["reply_gym_location"] = "{0}在{1}".format(args[0], str(citySet))
        #         else:
        #             tmp = ""
        #             for gym, loc in cityDict.items():
        #                 tmp += "{0}在{1}\n".format(gym, loc)
        #     elif "價" in args[1]:
        #         priceSet = getGymPrice(arg[0])
        #         for i in range(len(priceSet)):
        #             if i[1] != "na":
        #                 resultDICT["reply_gym_price"] = "{0}的平日票價為{1}、假日票價為{2}、星光飄價為{3}".format(i[0],i[1],i[2],i[3])
        #             else:
        #                 resultDICT["reply_gym_price"] = "{0}的票價是以小時計算，價格為{1}".format(i[0],i[4])
        #     elif "電話" in args[3]:
        #         phoneDict = getGymLocPh(args[0], "p")
        #         if len(cityDict) == 1:
        #             resultDICT["reply_gym_location"] = "{0}在{1}".format(args[0], str(citySet))
        #         else:
        #             tmp = ""
        #             for gym, loc in cityDict.items():
        #                 tmp += "{0}在{1}\n".format(gym, loc)
        #     else:
        #         resultDICT["reply_gym_location"] = random.choice(defaultResponse["_question_not_know"])
        # elif args[2] in userDefinedDICT["_climbingGym"]:
        #     resultDICT["reply_gym_location"] = "請問想問哪間岩館呢？"
        # else:
        #     resultDICT["reply_gym_location"] = "台灣沒有這間岩館哦"

    if utterance == "哪個[縣市]有[速度攀][場館]":
        if args[0] in userDefinedDICT["_cityAlias"]:
            citySet = getBTScity(args[2])
            resultDICT["reply_gym_location"] = "有{1}的{0}有：{2}".format(args[0], args[1], str(citySet)) 

    if utterance == "哪裡有[速度攀][場館]":
        citySet = getBTScity(args[0])
        resultDICT["reply_gym_location"] = "有{0}的地方有：{1}".format(args[0], str(citySet)) 

    if utterance == "[可以]告訴[我][double 8][岩館]的[地址]嗎":
        pass
        # if args[2] in userDefinedDICT["_gymsShort"]:
        #     resultDICT["reply_gym_name"] = args[2]
        #     if args[4] in ("地址","位置"):
        #         addSet = getGymLocPh(args[2], "a")
        #         resultDICT["reply_gym_location"] = "{0}的{2}是：{1}".format(args[2], str(addSet), args[4])
        #     elif "價" in args[4]:
        #         priceSet = getGymPrice(arg[2])
        #         for i in range(len(priceSet)):
        #             if i[1] != "na":
        #                 resultDICT["reply_gym_price"] = "{0}的平日票價為{1}、假日票價為{2}、星光飄價為{3}".format(i[0],i[1],i[2],i[3])
        #             else:
        #                 resultDICT["reply_gym_price"] = "{0}的票價是以小時計算，價格為{1}".format(i[0],i[4])
        #     elif "電話" in args[4]:
        #         phoneDict = getGymLocPh(args[0], "p")
        #         if len(cityDict) == 1:
        #             resultDICT["reply_gym_location"] = "{0}在{1}".format(args[0], str(citySet))
        #         else:
        #             tmp = ""
        #             for gym, loc in cityDict.items():
        #                 tmp += "{0}在{1}\n".format(gym, loc)
        #     else:
        #         resultDICT["reply_gym_location"] = random.choice(defaultResponse["_question_not_know"])
        # else:
        #     resultDICT["reply_gym_location"] = "台灣沒有這間岩館哦"

    if utterance == "[可以]給[我][double 8][岩館]的[地址]嗎":
        pass
        # if args[2] in userDefinedDICT["_gymsShort"]:
        #     resultDICT["reply_gym_name"] = args[2]
        #     if args[4] in ("地址","位置"):
        #         addSet = getGymLocPh(args[2], "a")
        #         resultDICT["reply_gym_location"] = "{0}的{2}是：{1}".format(args[2], str(addSet), args[4])
        #     elif "價" in args[4]:
        #         priceSet = getGymPrice(arg[2])
        #         for i in range(len(priceSet)):
        #             if i[1] != "na":
        #                 resultDICT["reply_gym_price"] = "{0}的平日票價為{1}、假日票價為{2}、星光飄價為{3}".format(i[0],i[1],i[2],i[3])
        #             else:
        #                 resultDICT["reply_gym_price"] = "{0}的票價是以小時計算，價格為{1}".format(i[0],i[4])
        #     else:
        #         resultDICT["reply_gym_location"] = random.choice(defaultResponse["_question_not_know"])
        # else:
        #     resultDICT["reply_gym_location"] = "台灣沒有這間岩館哦"

    return resultDICT