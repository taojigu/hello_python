#import requests
import sys
import requests
import time
import json

#1598580979.328512
#1598580552464


def printDept(dept):
    cell = dept['cell']
    name = cell['bond_nm']
    priceString = cell['price']
    prmRateString  = cell['premium_rt']
    #url = 'https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t=%i' % (millis)
    message = '%s 当前价格是 %s,溢价率是%s' % (name,priceString,prmRateString)
    print(message)
    return


def reportTagetDeptList(deptList):

    for dept in deptList:
        printDept(dept);
    return


def isTargetDept(dept):
    cell = dept['cell']
    priceTips = cell["price_tips"]
    if (priceTips == "待上市"):
        return False
    btype = cell['btype']
    if (btype == 'E'):
        return False
    priceString = cell['price']
    price = float(priceString);

    prmRateString  = cell['premium_rt']
    prmRateString = prmRateString[0:len(prmRateString)-1]
    prmRate = float(prmRateString)
    if (price > 120 ) :
        return False
    if (price < 106 and prmRate < 20):
        return True
    if (price < 110 and prmRate < 10):
        return True
    return False

def filterTargetDeptList(detpArray):
    targtDetpList = [];
    for dept in detpArray:
        if(isTargetDept(dept)):
            targtDetpList.append(dept['cell'])
    return targtDetpList

# 对外的公有方法
def fetchTargetDeptLsit():
    millis = int(round(time.time() * 1000))
    url = 'https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t=%i' % (millis)
    print(url);
    rsps = requests.get(url)
    rspsObj = json.loads(rsps.text);

    # filter the target depts
    deptList = filterTargetDeptList(rspsObj['rows'])
    return deptList

# deptList = fetchTargetDeptLsit()
# reportTagetDeptList(deptList)


