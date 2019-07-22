import datetime
import slack
import data
import time

data = data.start()
data = str(data)

sc = slack.WebClient('BOT TOKEN')

while True:
    if sc.rtm_connect():
        print('Bağlandı')
        while True:
            now = datetime.datetime.now()
            hour = now.hour
            if hour == 22:
                sc.chat_postMessage(
                    channel="#example",
                    text=data,
                    reply_broadcast=True
                )
                time.sleep(86400)
