#!/usr/bin/python3
import Description, CheckFormat, Operation, CarryOn
def AVtoBV(AVBehind):
    base=['f','z','o','d','R','9','X','Q','D','S','U','m','2','1','y','C','k','r','6','z','B','q','i','v','e','Y','a','h','8','b','t','4','x','s','W','p','H','n','J','E','7','j','L','5','V','G','3','g','u','M','T','K','N','P','A','w','c','F']
    BinaryVariable = eval(bin(177451812))
    BinaryAV = eval(bin(AVBehind))
    xorAV = BinaryAV ^ BinaryVariable
    AdditionAV = xorAV + 100618342136696320
    NumberOperations = 0
    ListComparisonDictionary = 0
    Result = []
    ResultEnd = []
    while NumberOperations != 10:
        Result.append(AdditionAV // 58 ** NumberOperations % 58)
        NumberOperations += 1
    while ListComparisonDictionary != 10:
        ResultEnd.append(base[Result[ListComparisonDictionary]])
        ListComparisonDictionary += 1
    BV = ResultEnd[6] + ResultEnd[2] + ResultEnd[4] + ResultEnd[8] + ResultEnd[5] + ResultEnd[9] + ResultEnd[3] + ResultEnd[7] + ResultEnd[1] + ResultEnd[0]
    print ("BV号为：BV{}".format(BV))
    print ("视频链接为：https://b23.tv/BV{}".format(BV))
    CarryOn.on()

def BVtoAV(BVBehind):
    base=['f','z','o','d','R','9','X','Q','D','S','U','m','2','1','y','C','k','r','6','z','B','q','i','v','e','Y','a','h','8','b','t','4','x','s','W','p','H','n','J','E','7','j','L','5','V','G','3','g','u','M','T','K','N','P','A','w','c','F']
    BVBehindEnd = []
    Multiplication = []
    ListComparisonDictionary = 0
    MultipleList = [6,2,4,8,5,9,3,7,1,0]
    Multiple = 0
    while ListComparisonDictionary != 10:
        BVBehindEnd.append(base.index(BVBehind[ListComparisonDictionary]))
        ListComparisonDictionary += 1
    while Multiple != 10:
        Multiplication.append(BVBehindEnd[Multiple] * 58 ** MultipleList[Multiple])
        Multiple += 1
    MultiplicationEnd = Multiplication[0] + Multiplication[1] + Multiplication[2] + Multiplication[3] + Multiplication[4] + Multiplication[5] + Multiplication[6] + Multiplication[7] + Multiplication[8] + Multiplication[9]
    SubtractionEnd = MultiplicationEnd - 100618342136696320
    BinarySubtractionEnd = eval(bin(SubtractionEnd))
    AV = BinarySubtractionEnd ^ eval(bin(177451812))
    print ("AV号为：AV{}".format(AV))
    print ("视频链接为：https://b23.tv/av{}".format(AV))
    CarryOn.on()