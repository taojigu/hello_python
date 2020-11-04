import requests,json


def textMessageParam(text):
    param ={
        "msgtype": "text",
        "text": {
            "content": text
        }
    }
    return param

def sendTextMessage(text):
    path = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=a4da1319-a8b9-4585-987f-913f61b7ea92'
    
    para = textMessageParam(text)
    result = requests.post(url=path,json=para)
    return

