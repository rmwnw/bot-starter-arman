from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import os

# ID Channel (جهت بررسی عضویت)
CHANNEL_ID = "rmwnww"  # ID Channel شما

# لینک‌های VPN برای ارسال
LINKS_TO_SEND = [
    "vless://a4e2c972-23dc-4cf6-f864-f8636d6b9cf0@speedtest.net:80?path=%2Folem%2Fws%3Fed%3D1024&security=&encryption=none&host=foffmelo.com&type=ws#vpnWedBaz",
    "vless://CoD_VPN@speedtest.net:80?type=grpc&serviceName=Telegram : @vpnwedbaz - Telegram",
    "vless://ec1bb388-649c-4deb-9eb1-a096b784e0d3@104.24.167.96:80?path=%2Ftelegram%40wedbaz---------------------------VpnWedBaZ--------------------------------%2F%3Fed%3D2560&security=&encryption=none&host=round-truth-4e97-ppal03.vegasow726.workers.dev&type=ws#vpnWedBaz",
    "vless://4d3e4850-83e4-4e9e-a4c1-0f11c43663e7@104.21.34.163:443?path=%2Ftelegram%40wedbaz-----------------------------VpnWedBaZ-------------------------------%2F%3Fed%3D2560&security=tls&alpn=http%2F1.1&encryption=none&host=crolinde.carlotta.cloudns.org&fp=random&type=ws&sni=crolinde.carlotta.cloudns.org#vpnWedBaz",
    "vless://Hqv2RayNG@hqmobin.ir:443?security=reality&encryption=none&pbk=uVSRg8Hzu_IwCYRJaXOTeUjSJA9uC999AxDMEjLn0XE&headerType=none&fp=randomized&spx=%2F&type=tcp&flow=xtls-rprx-vision&sni=refersion.com&sid=53e2c615fc63#vpnWedBaz",
    "vless://b1842291-3535-4d29-9455-303e33da37c3@VpnWedbaz.Germany.iphone-shopp.ir:1001?mode=multi&security=reality&encryption=none&pbk=5tdKwdHyyJkshzaZPdm54JpktJoa4PAE2T0qX1jJh38&fp=chrome&spx=%2F&type=grpc&serviceName=%2F%40VpnWedBaZ----------%40VpnWedBaZ-----------%40VpnWedBaZ----%40VpnWedBaZ-------%40VpnWedBaz-----%40VpnWedBaZ----------%40VpnWedBaZ-----------%40VpnWedBaZ----%40VpnWedBaZ-------%40VpnWedBaz-----%40VpnWedBaZ----------%40VpnWedBaZ-----------%40VpnWedBaZ----%40VpnWedBaZ-------%40VpnWedBaz&sni=stackoverflow.com&sid=e7ab164373b8#@VpnWedBaZ",
    "vless://75d766a7-779b-403c-8d76-70bb658d36d8@VpnWedbaz.Germany.iphone-shopp.ir:1000?mode=multi&security=&encryption=none&type=grpc&serviceName=%2F%40VpnWedBaZ----------%40VpnWedBaZ-----------%40VpnWedBaZ----%40VpnWedBaZ-------%40VpnWedBaz-----%40VpnWedBaZ----------%40VpnWedBaZ-----------%40VpnWedBaZ----%40VpnWedBaZ-------%40VpnWedBaz-----%40VpnWedBaZ----------%40VpnWedBaZ-----------%40VpnWedBaZ----%40VpnWedBaZ-------%40VpnWedBaz#@VpnWedBaZ",
    "vless://9f104d3d-bded-4f3e-b329-fd707244c8b5@VpnWedbaz.Finland.iphone-shopp.ir:1001?mode=multi&security=reality&encryption=none&pbk=LZ7p8L5Hv28uY8Zl53g24zq5tecggfbIQCACetZP7Tk&fp=chrome&spx=%2F&type=grpc&serviceName=%2F%40VpnWedBaZ----------%40VpnWedBaZ-----------%40VpnWedBaZ----%40VpnWedBaZ-------%40VpnWedBaz-----%40VpnWedBaZ----------%40VpnWedBaZ-----------%40VpnWedBaZ----%40VpnWedBaZ-------%40VpnWedBaz-----%40VpnWedBaZ----------%40VpnWedBaZ-----------%40VpnWedBaZ----%40VpnWedBaZ-------%40VpnWedBaz&sni=refersion.com&sid=0e9091abc81e03bb#@VpnWedBaZ",
    "vless://6eee70ec-74b3-480d-978f-9d680c32a8a3@VpnWedbaz.Finland.iphone-shopp.ir:1000?mode=multi&security=&encryption=none&type=grpc&serviceName=%2F%40VpnWedBaZ----------%40VpnWedBaZ-----------%40VpnWedBaZ----%40VpnWedBaZ-------%40VpnWedBaz-----%40VpnWedBaZ----------%40VpnWedBaZ-----------%40VpnWedBaZ----%40VpnWedBaZ-------%40VpnWedBaz-----%40VpnWedBaZ----------%40VpnWedBaZ-----------%40VpnWedBaZ----%40VpnWedBaZ-------%40VpnWedBaz#@VpnWedBaZ"
]

def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    try:
        # بررسی عضویت کاربر در Channel
        chat_member = context.bot.get_chat_member(chat_id=f"@{CHANNEL_ID}", user_id=user_id)
        if chat_member.status in ['member', 'creator', 'administrator']:
            # ارسال لینک‌ها به کاربر
            for link in LINKS_TO_SEND:
                update.message.reply_text(link)
        else:
            # اگر عضو نیست، دکمه عضویت در Channel نمایش دهد
            keyboard = [[InlineKeyboardButton("عضویت در Channel", url=f"https://t.me/{CHANNEL_ID}")]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            update.message.reply_text(
                "برای دریافت لینک‌ها، باید در Channel زیر عضو شوید:",
                reply_markup=reply_markup
            )
    except Exception as e:
        update.message.reply_text(f"خطایی رخ داد: {str(e)}")

def main():
    BOT_TOKEN = "8026545080:AAFMxTRp-kcmCckUjaeKLDyiBI-EYIjhh_8"  # توکن ربات شما
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
