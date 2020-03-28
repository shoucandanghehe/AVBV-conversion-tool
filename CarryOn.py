#!/usr/bin/python3
import Description, CheckFormat, Operation, CarryOn
def on():
    Whether = 0
    while Whether == 0:
        print ("您要继续转换吗？")
        print ("1.是")
        print ("其它任意键否")
        Whether = input ()
        print (Whether)
        if Whether == '1':
            Description.ReUse()
            CheckFormat.Check()
        else:
            Whether = 100
            input ("按任意键退出 . . .")