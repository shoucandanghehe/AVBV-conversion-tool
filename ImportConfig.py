def ImportConfig(LanguageList):
    import os, Description, CheckFormat, ChooseLanguage, ConfigCtrl
    if LanguageList:
        Config = LanguageList[0]
        if Config[0:11] == 'Language = ':
            print ("配置文件格式正确")
            if Config[11:] == 'zh_CN':
                print ("导入配置成功，语言设置为中文（简体），输入“re”可以重新选择语言")
                CheckFormat.Check('zh_CN')
            elif Config[11:] == 'zh_TW':
                print ("導入配置成功，語言設置為中文（繁體），輸入“re”可以重新選擇語言")
                CheckFormat.Check('zh_TW')
            elif Config[11:] == 'en_US':
                print ("Import config successful,language set to English.Enter 're' to re-select the language")
                CheckFormat.Check('en_US')
            elif Config[11:] == 'ja_JP':
                print ("インポート設定は成功し、言語は日本語に設定されています。言語を再選択するには「re」と入力します")
                CheckFormat.Check('ja_JP')
            else:
                print ("语言配置错误，清除配置文件重新选择")
                os.remove('conf/Language.txt')
                ConfigCtrl.DetectionConfig()
        else:
            print ("语言文件格式错误，清除配置文件重新选择")
            os.remove('conf/Language.txt')
            ConfigCtrl.DetectionConfig()
    else:
        print ("配置文件内无内容，选择语言")
        Description.ChoiceLanguage()
        ChooseLanguage.Choose()
    