import telegram

def send_telegram(photo_path="alert.png"):
    try:
        my_token = "5678624043:AAFo2YTRaDjxZMkd0QUj-hwKcw6xhrri7M4"
        bot = telegram.Bot(token=my_token)
        bot.sendPhoto(chat_id="5919079894", photo=open(photo_path, "rb"), caption="Có xâm nhập, nguy hiêm!")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    # print("Send sucess")