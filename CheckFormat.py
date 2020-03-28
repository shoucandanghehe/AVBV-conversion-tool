#!/usr/bin/python3
import Operation, Description, CheckFormat
def Check():
    AorB = input ("：")
    Head = AorB[0:2]
    if Head == 'AV' or Head == 'av' or Head == 'Av' or Head == 'aV':  #AV转BV
        print ("AV→BV")
        AVBehind = AorB[2:]
        if AVBehind.isdigit():
            Operation.AVtoBV(int(AVBehind))
        else:
            Description.ErrAV()
            CheckFormat.Check()
    elif Head == 'BV' or Head == 'bv' or Head == 'Bv' or Head == 'bV':  #BV转AV
        print ("BV→AV")
        BVBehind = AorB[2:]
        if len(BVBehind) == 10:
            if BVBehind.isalnum():
                Operation.BVtoAV(BVBehind)
            else:
                Description.ErrBV()
                CheckFormat.Check()
        else:
            Description.ErrBV()
            CheckFormat.Check()
    else:  #输入错误
        Description.ErrInput()
        CheckFormat.Check()