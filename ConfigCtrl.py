def DetectionConfig():
    import os, time, ChooseLanguage, ImportConfig, Description, sys
    if os.path.exists('conf'):
        print ("检测到配置文件夹")
        if os.path.exists('conf/Language.txt'):
            print ("检测到配置文件，开始导入语言配置。")
            Language = open('conf/Language.txt','r')
            LanguageList = Language.readlines()
            Language.close()
            ImportConfig.ImportConfig(LanguageList)
        else:
            print("未找到配置文件，尝试创建配置文件")
            Establish = open('conf/Language.txt',mode='w')
            Establish.close()
            if os.path.exists('conf/Language.txt'):
                print ("创建配置文件成功")
                Description.ChoiceLanguage()
                ChooseLanguage.Choose()
            else:
                print ("尝试创建失败，请尝试用管理员/root权限运行\n3秒后退出程序 . . .")
                time.sleep(3)
                sys.exit()
    else:
        print ("未找到配置文件夹，尝试创建。")
        os.mkdir('conf')
        if os.path.exists('conf'):
            print ("创建配置文件夹成功\n尝试创建配置文件")
            Establish = open('conf/Language.txt',mode='w')
            Establish.close()
            if os.path.exists('conf/Language.txt'):
                print ("创建配置文件成功")
                Description.ChoiceLanguage()
                ChooseLanguage.Choose()
            else:
                print ("尝试创建失败，请尝试用管理员/root权限运行\n3秒后退出程序 . . .")
                time.sleep(3)
                sys.exit()
        else:
            print ("尝试创建失败，请尝试用管理员/root权限运行\n3秒后退出程序 . . .")
            time.sleep(3)
            sys.exit()