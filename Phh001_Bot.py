import requests
import time

BOT_TOKEN="8514667947:AAFPZDMdsyZIEV9aVxQ7MWF7RBpGE3niIVY"
URL=f"https://api.telegram.org/bot{BOT_TOKEN}"
REGISTER_URL="https://tgtest002.superace-best.com"
CS_URL="https://tawk.to/chat/6988b7aa39c3861c362380f5/1jgv0qskl"
TG_URL="https://t.me/Ph54_com"
APP_URL="https://tgtest002.superace-best.com"
IMAGE_CS="https://i.postimg.cc/3NqmLbrs/8466e358-56a6-4737-b83f-eaa5135de61e.png"
IMAGE_TG="https://i.postimg.cc/59KBNj5j/4564156-1771043229749.png"
IMAGE_FD="https://i.postimg.cc/SQ16NjLR/4564156-1773166692995.png"
IMAGE_WL="https://i.ibb.co/k2KVGhvN/4564156-1772211660549.png"
IMAGE_ED="https://i.ibb.co/RT1MwyhB/image.png"
IMAGE_DA="https://i.ibb.co/67Cfr1Sr/image.png"

def get_updates(offset=None):
    try:
        params={"timeout":30,"offset":offset}
        r=requests.get(f"{URL}/getUpdates",params=params)
        data = r.json()
        if "result" in data:
            return data["result"]
        else:
            print(f"Error: {data}")
            return []
    except Exception as e:
        print(f"Connection error: {e}")
        return []

def send_message(chat_id,text,reply_markup=None):
    try:
        data={"chat_id":chat_id,"text":text}
        if reply_markup:data["reply_markup"]=reply_markup
        requests.post(f"{URL}/sendMessage",json=data)
    except Exception as e:
        print(f"Error sending message: {e}")

def send_photo(chat_id,photo_url,caption,reply_markup=None):
    try:
        data={"chat_id":chat_id,"photo":photo_url,"caption":caption}
        if reply_markup:data["reply_markup"]=reply_markup
        requests.post(f"{URL}/sendPhoto",json=data)
    except Exception as e:
        print(f"Error sending photo: {e}")

def main():
    print("Bot running...")
    offset=None
    menu={"keyboard":[["Customer Service","Official Telegram"],["First Deposit Bonus","Win & Lose Bonus"],["Every Deposit +3%","Download App +88"]],"resize_keyboard":True}
    while True:
        try:
            updates=get_updates(offset)
            for update in updates:
                offset=update["update_id"]+1
                if "message" in update:
                    message=update["message"]
                    chat_id=message.get("chat",{}).get("id")
                    text=message.get("text","").strip()
                    if not text:continue
                    if text=="/start":
                        send_message(chat_id,"\U0001f31f Welcome to PH54! \U0001f31f\n\n\U0001f3b0 The Best Online Casino Platform!\n\U0001f4b0 Big Rewards Waiting For You!\n\n\U0001f447 Choose an option below!",menu)
                    elif text=="Customer Service":
                        send_photo(chat_id,IMAGE_CS,"\U0001f4ac PH54 CUSTOMER SERVICE \U0001f4ac\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n\U0001f550 Available 24 hours, 7 days a week!\n\u26a1 Fast response guaranteed!\n\U0001f91d We are always here to help you!\n\U0001f4a1 Any questions? Just ask us!\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n\U0001f447 Click below to contact us now!",{"inline_keyboard":[[{"text":"\U0001f4ac Contact Us Now","url":CS_URL}]]})
                    elif text=="Official Telegram":
                        send_photo(chat_id,IMAGE_TG,"\U0001f4e3 JOIN PH54 OFFICIAL TELEGRAM \U0001f4e3\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n\U0001f381 Get daily rewards up to 20,555!\n\U0001f514 Latest promotions and updates!\n\U0001f3b0 Exclusive bonuses for members!\n\U0001f4b0 Never miss any reward again!\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n\U0001f447 Join us now and start earning!",{"inline_keyboard":[[{"text":"\U0001f4e3 Join Channel Now","url":TG_URL}],[{"text":"\U0001f4dd Register Now","url":REGISTER_URL}]]})
                    elif text=="First Deposit Bonus":
                        send_photo(chat_id,IMAGE_FD,"\U0001f4b0 NEW MEMBER FIRST DEPOSIT BONUS! \U0001f4b0\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n\U0001f381 Get up to 385 on your first deposit!\n\n\U0001f4b5 Deposit 100 - Get 20\n\U0001f4b5 Deposit 300 - Get 65\n\U0001f4b5 Deposit 500 - Get 105\n\U0001f4b5 Deposit 1,000 - Get 255\n\U0001f4b5 Deposit 2,000 - Get 325\n\U0001f4b5 Deposit 3,000 - Get 385\n\n\u2705 New members only\n\u2705 First deposit only\n\u2705 Bonus auto credited instantly\n\u2705 Slots only - 5x valid bet\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501",{"inline_keyboard":[[{"text":"\U0001f4dd Register and Claim Now","url":REGISTER_URL}]]})
                    elif text=="Win & Lose Bonus":
                        send_photo(chat_id,IMAGE_WL,"\U0001f525 WIN OR LOSE - YOU ALWAYS WIN! \U0001f525\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n\U0001f3b0 No matter what happens today!\n\U0001f4c5 Tomorrow you ALWAYS get bonus!\n\n\U0001f60e Win in Slot - Get extra 7% bonus!\n\U0001f4aa Lose in Slot - Get up to 18% back!\n\n\u26a1 Bonus delivered automatically next day!\n\U0001f381 New Members get up to 188,888!\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501",{"inline_keyboard":[[{"text":"\U0001f4dd Register and Claim Now","url":REGISTER_URL}]]})
                    elif text=="Every Deposit +3%":
                        send_photo(chat_id,IMAGE_ED,"\u26a1 EVERY DEPOSIT EXTRA 3% BONUS! \u26a1\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n\U0001f381 Get 3% bonus on EVERY deposit!\n\U0001f4b3 PayMaya and USDT deposits only\n\u26a1 Bonus credited in REAL TIME!\n\u267e No bonus limit at all!\n\U0001f4c8 More you deposit - More you earn!\n\U0001f4b0 The more you recharge the more you get!\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501",{"inline_keyboard":[[{"text":"\U0001f4dd Register and Claim Now","url":REGISTER_URL}]]})
                    elif text=="Download App +88":
                        send_photo(chat_id,IMAGE_DA,"\U0001f4f1 DOWNLOAD PH54 APP FREE! \U0001f4f1\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\n\U0001f381 Download now and get 88 FREE bonus!\n\U0001f3ae Play anytime anywhere!\n\u26a1 Fast and smooth experience!\n\U0001f512 Safe and secure platform!\n\U0001f4b0 Exclusive app-only rewards!\n\U0001f3c6 Best online casino in Philippines!\n\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501",{"inline_keyboard":[[{"text":"\U0001f4f1 Download Now Free","url":APP_URL}]]})
                    else:
                        send_message(chat_id,"\U0001f447 Please choose from the menu below!",menu)
        except Exception as e:
            print(f"Main loop error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()
