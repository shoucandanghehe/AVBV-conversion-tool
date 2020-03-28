#!/usr/bin/python3
def Description():
    print ("本程序可将AV和BV号互相转换")
    print ("输入AV*****或av*****即为转换成BV，输入BV**********或bv**********即为转换成AV。")

def ErrInput():
    print ("输入错误")
    print ("请重新输入")
    print ("输入AV*****或av*****即为转换成BV，输入BV**********或bv**********即为转换成AV。")

def ReUse():
    print ("再次转换")
    print ("输入AV*****或av*****即为转换成BV，输入BV**********或bv**********即为转换成AV。")

def ErrAV():
    print ("AV号输入错误")
    print ("请注意AV号只包含数字不包含字母汉字和其他特殊符号")
    print ("请重新输入")
    print ("输入AV*****或av*****即为转换成BV，输入BV**********或bv**********即为转换成AV。")

def ErrBV():
    print ("BV号输入错误")
    print ("请注意BV号只包含数字和字母不包含汉字和其他特殊符号，且长度是10位")
    print ("请重新输入")
    print ("输入AV*****或av*****即为转换成BV，输入BV**********或bv**********即为转换成AV。")