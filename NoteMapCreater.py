# -*- coding: utf-8 -*-

#NoteMapCreater 世界音创
#Code by W-YI 金羿
# QQ 2647547478
# Email EillesWan2006@163.com W-YI_DoctorYI@outlook.com
#未经允许不得商用 源码借鉴要加作者
# 版权所有 Team-Ryoun 金羿
#Copyright W-YI 2021


VER = ('0.0.0','Beta',)
LIBS = ('mido','amulet','amulet-core','amulet-nbt','piano_transcription_inference')


import sys,os

from nmcsup.log import log


#读入参数
args = sys.argv

#没有参数的运行
if len(args) == 1:
    pass #此处欲作为标准程序进入
    print("没有任何参数传入。")
    log("异常退出：无参数传入")
    exit()


def GetFilePath(File:str) -> str:
    if sys.platform == 'win32':
        return File[:len(File)-File[len(File)::-1].index('\\')]
    else:
        return File[:len(File)-File[len(File)::-1].index('/')]


#测试版本范围内不检查版本
#from nmcsup.vers import chkver
#chkver(VER,LIBS)





#正式程序开始


#查看帮助
if '-?' in args:
    print("世界音创 "+VER[1]+VER[0])
    print("版权所有© 金羿 2021 Copyright © W-YI 2021")
    print("使用第三方库："+str(LIBS))
    print(open(GetFilePath(__file__)+'Doc.TXT','r',encoding='utf-8').read())
    exit()



#输出文件
if '-o' in args:
    OutFile = args[args.index('-o')+1]
elif '-c' in args:
    OutFile = args[args.index('-c')+1]
    import zipfile
    with zipfile.ZipFile("./nmcsup/EptWorld.zip", "r") as zipobj:
        zipobj.extractall(OutFile)
else:
    OutFile = GetFilePath(args[1])+'World'


#方块位置
if '-cp' in args:
    dire = [int(args[args.index('-cp')+1]), int(args[args.index('-cp')+2]), int(args[args.index('-cp')+3])]
else:
    dire = [16,10,16]





#判定副档名
if args[2] == 'mid':
    from nmcsup.nmcreader import ReadMidi
    NoteData = ReadMidi(args[1])
elif args[2] == 'txt':
    from nmcsup.nmcreader import ReadFile
    NoteData = ReadFile(args[1])
elif args[2] == 'mp3':
    from nmcsup.nmcreader import ReadMidi
    from nmcsup.trans import Mp32Mid
    if not os.path.exists('./Temp/'):
        os.makedirs('./Temp/')
    Mp32Mid(args[1],'./Temp/Trans.mid')
    NoteData = ReadMidi('./Temp/Trans.mid')
elif args[2] == 'ry.nfc' or args[2] == 'ry.mfm':
    from nmcsup.nmcreader import ReadProject
    NoteData = ReadProject(args[1])
elif args[2] == 'func':
    if not '-f2c' in args:
        log("函数没？")
        print("请仔细阅读帮助信息。")
        exit()
    cl = open(args[1],'r',encoding='utf-8').readlines()
    CmdList = []
    for i in cl:
        if (i[:i.index('#')].replace(' ','') != '\n') and (i[:i.index('#')].replace(' ','') != ''):
            CmdList.append(i[:i.index('#')].replace(' ',''))










#指令设置

CmdData = {
    'Ins' : 'note.harp',
    'Ent' : 'music_support',
    'Sbn' : 'music_support',
    'Pls' : ''
}


if '-inst' in args:
    CmdData['Ins'] = args[args.index('-inst')+1]

if '-enti' in args:
    CmdData['Ent'] = args[args.index('-enti')+1]

if '-scor' in args:
    CmdData['Sbn'] = args[args.index('-scor')+1]

if '-pers' in args:
    CmdData['Pls'] = args[args.index('-pers')+1]









#转为方块世界
if '-bw' in args:
    from nmcsup.trans import Datas2BlkWorld,Notes2Player,Cmd2World
    Datas2BlkWorld(NoteData,OutFile,dire)
    Cmd2World(Notes2Player(NoteData,OutFile,dire,CmdData),OutFile,[dire[0]-5,dire[1],dire[2]])


#生成函数播放器
if '-p' in args:
    from nmcsup.trans import Notes2Player
    open(args[1][:len(args[1])-args[1][len(args[1])::-1].index('.')]+'mcfunction','w',encoding='utf-8').writelines(Notes2Player(NoteData,OutFile,dire,CmdData))
    



#转为指令世界
if '-w' in args:
    from nmcsup.trans import Datas2CmdWorld
    Datas2CmdWorld(NoteData,OutFile,dire,CmdData)



#函数输入指令块
if '-f2c' in args:
    from nmcsup.trans import Cmd2World
    Cmd2World(CmdData,OutFile,dire)