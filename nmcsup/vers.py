#判断版本、临时文件与补全库
def compver(ver1, ver2):
    """
    传入不带英文的版本号,特殊情况："10.12.2.6.5">"10.12.2.6"
    :param ver1: 版本号1
    :param ver2: 版本号2
    :return: ver1< = >ver2返回-1/0/1
    """
    list1 = str(ver1).split(".")
    list2 = str(ver2).split(".")
    # 循环次数为短的列表的len
    for i in range(len(list1)) if len(list1) < len(list2) else range(len(list2)):
        if int(list1[i]) == int(list2[i]):
            pass
        elif int(list1[i]) < int(list2[i]):
            return -1
        else:
            return 1
    # 循环结束，哪个列表长哪个版本号高
    if len(list1) == len(list2):
        return 0
    elif len(list1) < len(list2):
        return -1
    else:
        return 1
#
# ————————————————
# 版权声明：上面的函数compver为CSDN博主「基友死得早」的原创文章中的函数，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/tinyjm/article/details/93514261
# ————————————————
#

import os

def InstallLibs(now,LIBS):
    for i in LIBS:
        if not i in now:
            os.system("python -m pip install "+i+" -i https://pypi.tuna.tsinghua.edu.cn/simple")


def chkver(VER,LIBS):
    if not os.path.exists(os.getenv('APPDATA')+'\\NoteMapCreater\\NMC.ActiveDatas.nmc'):
        os.makedirs(os.getenv('APPDATA')+'\\NoteMapCreater\\')
        with open(os.getenv('APPDATA')+'\\NoteMapCreater\\NMC.ActiveDatas.nmc', 'w') as f:
            f.write(VER[0])
        InstallLibs([],LIBS)
    else:
        with open(os.getenv('APPDATA')+'\\NoteMapCreater\\NMC.ActiveDatas.nmc', 'r') as f:
            v = f.readlines()
        cp = compver(VER[0], v[0])
        if cp != 0:
            InstallLibs(v[1:],LIBS)
            with open(os.getenv('APPDATA')+'\\NoteMapCreater\\NMC.ActiveDatas.nmc', 'w') as f:
                f.write(VER[0]+'\n')
                for i in LIBS:
                    f.write(i+'\n')
        del cp

