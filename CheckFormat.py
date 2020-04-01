def Check(Language):
    import Operation, Description, sys, os, ConfigCtrl
    if Language == 'zh_CN':
        Description.Description()
        AorB = input ("：")
        Head = AorB[0:2]
        if Head in['av','AV','Av','aV']:  #AV转BV
            print ("AV→BV")
            AVBehind = AorB[2:]
            if AVBehind.isdigit():
                Operation.AVtoBV(int(AVBehind),Language)
            else:
                Description.ErrAV()
                Check(Language)
        elif Head in['bv','Bv','bV','BV']:  #BV转AV
            print ("BV→AV")
            BVBehind = AorB[2:]
            if len(BVBehind) == 10:
                if BVBehind.isalnum():
                    Operation.BVtoAV(BVBehind,Language)
                else:
                    Description.ErrBV()
                    Check(Language)
            else:
                Description.ErrBV()
                Check(Language)
        elif Head == 're':
            print ("重新选择语言")
            os.remove('conf/Language.txt')
            ConfigCtrl.DetectionConfig()
        elif AorB == 'exit':
            sys.exit()
        else:  #输入错误
            Description.ErrInput()
            Check(Language)
    elif Language == 'zh_TW':
        Description.Description_zh_TW()
        AorB = input ("：")
        Head = AorB[0:2]
        if Head in['av','AV','Av','aV']:  #AV转BV
            print ("AV→BV")
            AVBehind = AorB[2:]
            if AVBehind.isdigit():
                Operation.AVtoBV(int(AVBehind),Language)
            else:
                Description.ErrAV_zh_TW()
                Check(Language)
        elif Head in['bv','Bv','bV','BV']:  #BV转AV
            print ("BV→AV")
            BVBehind = AorB[2:]
            if len(BVBehind) == 10:
                if BVBehind.isalnum():
                    Operation.BVtoAV(BVBehind,Language)
                else:
                    Description.ErrBV_zh_TW()
                    Check(Language)
            else:
                Description.ErrBV_zh_TW()
                Check(Language)
        elif Head == 're':
            print ("重新選擇語言")
            os.remove('conf/Language.txt')
            ConfigCtrl.DetectionConfig()
        elif AorB == 'exit':
            sys.exit()
        else:  #输入错误
            Description.ErrInput_zh_TW()
            Check(Language)
    elif Language == 'en_US':
        Description.Description_en_US()
        AorB = input ("：")
        Head = AorB[0:2]
        if Head in['av','AV','Av','aV']:  #AV转BV
            print ("AV→BV")
            AVBehind = AorB[2:]
            if AVBehind.isdigit():
                Operation.AVtoBV(int(AVBehind),Language)
            else:
                Description.ErrAV_en_US()
                Check(Language)
        elif Head in['bv','Bv','bV','BV']:  #BV转AV
            print ("BV→AV")
            BVBehind = AorB[2:]
            if len(BVBehind) == 10:
                if BVBehind.isalnum():
                    Operation.BVtoAV(BVBehind,Language)
                else:
                    Description.ErrBV_en_US()
                    Check(Language)
            else:
                Description.ErrBV_en_US()
                Check(Language)
        elif Head == 're':
            print ("Reselect language")
            os.remove('conf/Language.txt')
            ConfigCtrl.DetectionConfig()
        elif AorB == 'exit':
            sys.exit()
        else:  #输入错误
            Description.ErrInput_en_US()
            Check(Language)
    elif Language == 'ja_JP':
        Description.Description_ja_JP()
        AorB = input ("：")
        Head = AorB[0:2]
        if Head in['av','AV','Av','aV']:  #AV转BV
            print ("AV→BV")
            AVBehind = AorB[2:]
            if AVBehind.isdigit():
                Operation.AVtoBV(int(AVBehind),Language)
            else:
                Description.ErrAV_ja_JP()
                Check(Language)
        elif Head in['bv','Bv','bV','BV']:  #BV转AV
            print ("BV→AV")
            BVBehind = AorB[2:]
            if len(BVBehind) == 10:
                if BVBehind.isalnum():
                    Operation.BVtoAV(BVBehind,Language)
                else:
                    Description.ErrBV_ja_JP()
                    Check(Language)
            else:
                Description.ErrBV_ja_JP()
                Check(Language)
        elif Head == 're':
            print ("言語を再選択")
            os.remove('conf/Language.txt')
            ConfigCtrl.DetectionConfig()
        elif AorB == 'exit':
            sys.exit()
        else:  #输入错误
            Description.ErrInput_ja_JP()
            Check(Language)
    else:
        print ("这里应该不会被执行到")