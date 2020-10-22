#import requests
import sys
import requests
import time
import json

#1598580979.328512
#1598580552464



def isTargetDept(dept):
    cell = dept['cell']
    priceString = cell['price']
    price = float(priceString);
    covertRation = cell['convert_cd']
    if (covertRation == '未到转股期') :
        return False
    prmRateString  = cell['premium_rt']
    prmRateString = prmRateString[0:len(prmRateString)-1]
    prmRate = float(prmRateString)
    if (price > 120 ) :
        return False
    if (price < 106 and prmRate < 20):
        return True
    if (price < 110 and prmRate < 10):
        return True

def filterTargetDeptList(detpArray):
    targtDetpList = [];
    for dept in detpArray:
        if(isTargetDept(dept)):
            targtDetpList.append(dept)
    return targtDetpList


#https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t=1598580552464
millis = int(round(time.time() * 1000))
url = 'https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t=%i' % (millis)
rsps = requests.get(url)

rspsObj = json.loads(rsps.text);

# filter the target depts
filterTargetDeptList(rspsObj['rows'])


# report targests

print (rsps.text)



# url = 'http://httpbin.org/post'
# d = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post(url, data=d)
# print r.text