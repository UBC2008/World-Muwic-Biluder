from nmcsup.log import log
from nmcsup.const import notes


# 输入一个列表 [ [str, float ], [], ... ] 音符str 值为持续时间float
def note2list(Notes : list) -> list:
    def change(base):
        enwo = {
           'a': 'A',
           'b': 'B',
           'c': 'C',
           'd': "D",
           "e": "E",
           'f': 'F',
           'g': "G"
        }
        nuwo = {
           '6': 'A',
           '7': 'B',
           '1': 'C',
           '2': "D",
           "3": "E",
           '4': 'F',
           '5': "G"
        }
        for k, v in enwo.items():
            if k in base:
                base = base.replace(k, v)
        for k, v in nuwo.items():
            if k in base:
                base = base.replace(k, v)
        return base
    res = []
    log("	===	音符列表=>音调列表")
    for i in Notes:
        s2 = change(i[0])
        log('	===	正在操作音符'+i[0]+'->'+s2)
        if s2 in notes.keys():
            log("	===	找到此音符，加入："+str(notes[s2][0]))
            res.append([notes[s2][0], float(i[1])])
        else:
            log('	===	'+s2+'不在音符表内，此处自动替换为 休止符0 ')
            res.append(['0', float(i[1])])
    log('	===	最终反回'+str(res))
    return res


#从格式文本文件读入一个音轨并存入一个列表
def ReadFile(fn : str) -> list:
    log('打开'+fn+"并读取音符")
    try:
        nat = open(fn, 'r', encoding='UTF-8').read().split(" ")
        del fn
    except:
        log("找不到读取目标文件")
        return
    Notes = []
    log(str(nat)+"已读取")
    for i in range(int(len(nat)/2)):
        Notes.append([nat[i*2], float(nat[i*2+1])])
    Notes = note2list(Notes)
    log('音符数据更新'+str(Notes))
    return [Notes,]


#从midi读入多个音轨，返回多个音轨列表
def ReadMidi(midfile : str ) -> list:
    import mido
    Notes = []
    try:
        mid = mido.MidiFile(midfile)
    except:
        log("找不到文件"+midfile)
        return
    # 解析
    ks = list(notes.values())
    for j, track in enumerate(mid.tracks):
        datas = []
        for i in track:
            if i.is_meta:
                log('元信息'+str(i))
                pass  # 不处理元信息
            elif 'note_on' in str(i):
                msg = str(i).replace("note=", '').replace("time=", '').split(" ")
                log('音符on消息，处理后：'+str(msg))
                if msg[4] == '0':
                    datas.append([ks[int(msg[2])-20][0], 1.0])
                    log('延续时间0tick--：添加音符'+str([ks[int(msg[2])-20][0], 1.0]))
                else:
                    datas.append([ks[int(msg[2])-20][0], float(msg[4])/480])
                    log('延续时间'+msg[4]+'tick--：添加音符' +str([ks[int(msg[2])-20][0], float(msg[4])/480]))
        log('音符增加'+str(datas))
        Notes.append(datas)
        del datas
    del ks
    return Notes




def ReadProject(fn:str) -> list:
    import json
    log("读取文件："+fn)
    try:
        with open(fn, 'r', encoding='UTF-8') as c:
            dataset = json.load(c)
    except:
        print('找不到文件：'+fn+"，请查看您是否输入正确")
        log("丢失"+fn)
        return
    notes = []
    for i in dataset['musics']:
        notes.append(note2list(i['notes']))
    #返回 音轨列表 选择器
    return notes