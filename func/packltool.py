import struct


def packByteData(originStr):
    strlen = len(originStr)
    if strlen % 2 != 0:
        return None
    else:
        i = 0
        rlt = ''
        end_flag = False
        while(not(end_flag)):
            s = originStr[i] + originStr[i + 1]
            rlt += struct.pack('B', int(s, 16))
            i += 2
            if i>= strlen:
                end_flag = True
                break
        return rlt


def packAsciiData(originStr):
    i = 0
    rlt = ''
    end_flag = False
    while (not (end_flag)):
        s = hex(ord(originStr[i]))
        rlt += struct.pack('B', int(s, 16))
        i += 1
        if i >= len(originStr):
            end_flag = True
            break
    return rlt

def unpackData(originData):
    pass