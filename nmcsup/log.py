import datetime,os

#载入日志功能
StrStartTime = str(datetime.datetime.now()).replace(':', '_')[:-7]
def log(info):
    if not os.path.exists('./log/'):
        os.makedirs('./log/')
    with open('./log/'+StrStartTime+'.nfc.log', 'a',encoding='UTF-8') as f:
        f.write(str(datetime.datetime.now())[11:19]+'	'+info+'\n')