
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from wechat.dinner_reminder import sendDinnerText
from wechat.message_worker import sendTextMessage

def dinnerTextJob1():
    sendDinnerText(0)
    return
def dinnerTextJob2():
    sendDinnerText(1)
    return

def dinnerTextJob3():
    sendDinnerText(3)
    return

def directDinnerTextJob(text):
    sendTextMessage(text)
    return


scheduler = BackgroundScheduler()

scheduler.add_job(dinnerTextJob3, 'cron', day_of_week='0-4', hour=12, minute=20)
scheduler.add_job(dinnerTextJob1, 'cron', day_of_week='0-4', hour=12, minute=25)
scheduler.add_job(dinnerTextJob2, 'cron', day_of_week='0-4', hour=12, minute=28)


scheduler.add_job(dinnerTextJob3, 'cron', day_of_week='0-4', hour=18, minute=35)
scheduler.add_job(dinnerTextJob1, 'cron', day_of_week='0-4', hour=18, minute=40)
scheduler.add_job(dinnerTextJob2, 'cron', day_of_week='0-4', hour=18, minute=45)


scheduler.start()
print('启动吃饭提醒服务')

while True:
    pass