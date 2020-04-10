def AVtoBV(AVBehind,Language):
    import CheckFormat
    base=['f','Z','o','d','R','9','X','Q','D','S','U','m','2','1','y','C','k','r','6','z','B','q','i','v','e','Y','a','h','8','b','t','4','x','s','W','p','H','n','J','E','7','j','L','5','V','G','3','g','u','M','T','K','N','P','A','w','c','F']
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
    if Language == 'zh_CN':
        print ("BV号为：BV{}".format(BV))
        print ("视频链接为：https://b23.tv/BV{}".format(BV))
        print ("进入下一次转换，输入“exit”可以退出程序")
    elif Language == 'zh_TW':
        print ("BV號為：BV{}".format(BV))
        print ("視頻鏈接為：https://b23.tv/BV{}".format(BV))
        print ("進入下一次轉換，輸入“exit”可以退出程序")
    elif Language == 'en_US':
        print ("BV number is：BV{}".format(BV))
        print ("The video link is：https://b23.tv/BV{}".format(BV))
        print ("Enter the next conversion, enter 'exit' to exit the program")
    elif Language == 'ja_JP':
        print ("BV番号は：BV{}".format(BV))
        print ("ビデオリンクは：https://b23.tv/BV{}".format(BV))
        print ("次の変換を入力し、「exit」と入力してプログラムを終了します")
    else:
        print ("这里应该不会被执行到")
    CheckFormat.Check(Language)

def BVtoAV(BVBehind,Language):
    import CheckFormat
    base=['f','Z','o','d','R','9','X','Q','D','S','U','m','2','1','y','C','k','r','6','z','B','q','i','v','e','Y','a','h','8','b','t','4','x','s','W','p','H','n','J','E','7','j','L','5','V','G','3','g','u','M','T','K','N','P','A','w','c','F']
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
    if Language == 'zh_CN':
        print ("AV号为：AV{}".format(AV))
        print ("视频链接为：https://b23.tv/AV{}".format(AV))
        print ("进入下一次转换，输入“exit”可以退出程序")
    elif Language == 'zh_TW':
        print ("AV號為：AV{}".format(AV))
        print ("視頻鏈接為：https://b23.tv/AV{}".format(AV))
        print ("進入下一次轉換，輸入“exit”可以退出程序")
    elif Language == 'en_US':
        print ("AV number is：AV{}".format(AV))
        print ("The video link is：https://b23.tv/AV{}".format(AV))
        print ("Enter the next conversion, enter 'exit' to exit the program")
    elif Language == 'ja_JP':
        print ("AV番号は：AV{}".format(AV))
        print ("ビデオリンクは：https://b23.tv/AV{}".format(AV))
        print ("次の変換を入力し、「exit」と入力してプログラムを終了します")
    else:
        print ("这里应该不会被执行到")
    CheckFormat.Check(Language)