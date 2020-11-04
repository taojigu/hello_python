from .message_worker import *
def reminderTextList():
    return [
        '吃饭不积极，思想有问题',
        '排队不早走，饭菜贱如狗'
    ]

def sendDinnerText(index):
    textList = reminderTextList()
    messageText = '吃饭了，吃饭了'
    if (index < len(textList)):
        messageText = textList[index]
    sendTextMessage(messageText)
    return



