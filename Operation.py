#!/usr/bin/python3
import Description, CheckFormat, Operation, CarryOn
def AVtoBV(AVBehind):
    base=['f','z','o','d','R','9','X','Q','D','S','U','m','2','1','y','C','k','r','6','z','B','q','i','v','e','Y','a','h','8','b','t','4','x','s','W','p','H','n','J','E','7','j','L','5','V','G','3','g','u','M','T','K','N','P','A','w','c','F']
    BinaryVariable = eval(bin(177451812))
    BinaryAV = eval(bin(AVBehind))
    xorAV = BinaryAV ^ BinaryVariable
    AdditionAV = xorAV + 100618342136696320
    Result0 = AdditionAV // 58 ** 0 % 58
    Result1 = AdditionAV // 58 ** 1 % 58
    Result2 = AdditionAV // 58 ** 2 % 58
    Result3 = AdditionAV // 58 ** 3 % 58
    Result4 = AdditionAV // 58 ** 4 % 58
    Result5 = AdditionAV // 58 ** 5 % 58
    Result6 = AdditionAV // 58 ** 6 % 58
    Result7 = AdditionAV // 58 ** 7 % 58
    Result8 = AdditionAV // 58 ** 8 % 58
    Result9 = AdditionAV // 58 ** 9 % 58
    ResultEnd0 = base[Result0]
    ResultEnd1 = base[Result1]
    ResultEnd2 = base[Result2]
    ResultEnd3 = base[Result3]
    ResultEnd4 = base[Result4]
    ResultEnd5 = base[Result5]
    ResultEnd6 = base[Result6]
    ResultEnd7 = base[Result7]
    ResultEnd8 = base[Result8]
    ResultEnd9 = base[Result9]
    BV = ResultEnd6 + ResultEnd2 + ResultEnd4 + ResultEnd8 + ResultEnd5 + ResultEnd9 + ResultEnd3 + ResultEnd7 + ResultEnd1 + ResultEnd0
    print ("BV号为：BV{}".format(BV))
    print ("视频链接为：https://b23.tv/BV{}".format(BV))
    CarryOn.on()

def BVtoAV(BVBehind):
    base=['f','z','o','d','R','9','X','Q','D','S','U','m','2','1','y','C','k','r','6','z','B','q','i','v','e','Y','a','h','8','b','t','4','x','s','W','p','H','n','J','E','7','j','L','5','V','G','3','g','u','M','T','K','N','P','A','w','c','F']
    BVBehindEnd0 = base.index(BVBehind[0])
    BVBehindEnd1 = base.index(BVBehind[1])
    BVBehindEnd2 = base.index(BVBehind[2])
    BVBehindEnd3 = base.index(BVBehind[3])
    BVBehindEnd4 = base.index(BVBehind[4])
    BVBehindEnd5 = base.index(BVBehind[5])
    BVBehindEnd6 = base.index(BVBehind[6])
    BVBehindEnd7 = base.index(BVBehind[7])
    BVBehindEnd8 = base.index(BVBehind[8])
    BVBehindEnd9 = base.index(BVBehind[9])
    Multiplication0 = BVBehindEnd0 * 58 ** 6
    Multiplication1 = BVBehindEnd1 * 58 ** 2
    Multiplication2 = BVBehindEnd2 * 58 ** 4
    Multiplication3 = BVBehindEnd3 * 58 ** 8
    Multiplication4 = BVBehindEnd4 * 58 ** 5
    Multiplication5 = BVBehindEnd5 * 58 ** 9
    Multiplication6 = BVBehindEnd6 * 58 ** 3
    Multiplication7 = BVBehindEnd7 * 58 ** 7
    Multiplication8 = BVBehindEnd8 * 58 ** 1
    Multiplication9 = BVBehindEnd9 * 58 ** 0
    MultiplicationEnd = Multiplication0 + Multiplication1 + Multiplication2 + Multiplication3 + Multiplication4 + Multiplication5 + Multiplication6 + Multiplication7 + Multiplication8 + Multiplication9
    SubtractionEnd = MultiplicationEnd - 100618342136696320
    BinarySubtractionEnd = eval(bin(SubtractionEnd))
    AV = BinarySubtractionEnd ^ eval(bin(177451812))
    print ("AV号为：AV{}".format(AV))
    print ("视频链接为：https://b23.tv/av{}".format(AV))
    CarryOn.on()