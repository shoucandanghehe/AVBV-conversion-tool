def Choose():
    import CheckFormat
    Language = input ("：")
    if Language == '1':
        print ("使用中文（简体）")
        conf = open('./conf/Language.txt','a')
        conf.write('Language = zh_CN')
        conf.close()
        CheckFormat.Check('zh_CN')
    elif Language == '2':
        print ("使用中文（繁體）")
        conf = open('./conf/Language.txt','a')
        conf.write('Language = zh_TW')
        conf.close()
        CheckFormat.Check('zh_TW')
    elif Language == '3':
        print ("Use English")
        conf = open('./conf/Language.txt','a')
        conf.write('Language = en_US')
        conf.close()
        CheckFormat.Check('en_US')
    elif Language == '4':
        print ("日本語を使う")
        conf = open('./conf/Language.txt','a')
        conf.write('Language = ja_JP')
        conf.close()
        CheckFormat.Check('ja_JP')
    else:
        print ("Input error")
        Choose()