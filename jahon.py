import telebot
from telebot import types
from telebot.types import *
import openai

token='6898769656:AAFW67X-WsdYBPkvkiGm59c77TXJNjjN3ig'
bot=telebot.TeleBot(token)
openai.api_key= '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'

# CHATGPT_API_TOKEN = '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'
# CHATGPT_API_ENDPOINT = 'https://api.openai.com/v1/engines/davinci-codex/completions'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Assalomu alaykum')
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    pha=types.KeyboardButton("Travel")
    markup.add(pha)
    pha1=types.KeyboardButton("Biz bilan bog'lanish")
    markup.add(pha1)
    pha2=types.KeyboardButton("To'lov turlari")
    markup.add(pha2)
    bot.send_message(message.chat.id,'Bizning Travelme botizmizga xush kelibsiz!',reply_markup=markup)
@bot.message_handler(commands=['Naqd'])
def start_message(message):
    bot.send_photo(message.chat.id,photo="https://fviib.uz/public/uploads/news/5ec280937568ba1d99820f8951e103d9.jpg")
    bot.send_message(message.chat.id,"Naqd to'lash uchun biz bilan bog'laning tugmasiga bosing")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    pha=types.KeyboardButton("Travel")
    markup.add(pha)

@bot.message_handler(commands=['Karta'])
def start_message(message):
    bot.send_photo(message.chat.id,photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7LCdWmjyOkBC_kvW9f0rBcKxJM34wzuvT7W3Trv3ZpWaQ3bSJwBxv6pWIwljchKnDA_E&usqp=CAU")
    bot.send_message(message.chat.id,"Kartadan to'lash uchun 1234 5678 9123 4567 kartasiga pul tashlang")
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    pha=types.KeyboardButton("Travel")
    markup.add(pha)

@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Travel":
        markup = InlineKeyboardMarkup()
        markup.row_width = 2
        markup.add(InlineKeyboardButton("Buxoro", callback_data="Buxoro"), InlineKeyboardButton("Samarqand", callback_data="Samarqand"), InlineKeyboardButton("Xorazm", callback_data="Xorazm"), InlineKeyboardButton("Toshkent", callback_data="Toshkent"),InlineKeyboardButton("Andijon", callback_data="Andijon"),InlineKeyboardButton("Namangan", callback_data="Namangan"),InlineKeyboardButton("Navoiy", callback_data="Navoiy"),InlineKeyboardButton("Jizzax", callback_data="Jizzax"))
        bot.send_message(message.chat.id,"Sayoxat joyolaridan birortasini tanlang!", reply_markup=markup)

    if message.text=="Biz bilan bog'lanish":
        bot.send_message(message.chat.id,"(91)337 77 83  raqamiga qo'ng'iroq qiling")

    if message.text=="To'lov turlari":
        bot.send_message(message.chat.id,"/Naqd , /Karta")
    else:
        reply=""
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"User:{message.text}\nBot:",
            max_tokens=150,
            temperature=0.7,
            n=1,
            stop=None
        )
        if response and response.choices:
            reply = " ".join([choice.text.strip() for choice in response.choices])
        else:
            reply = 'ой что-то пошло не так'
        bot.send_message(message.chat.id, reply)
        
        

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "Buxoro":
        city = "Buxoro"
        lat=39.768123190012524, 
        lon=64.4555875754962
        bot.send_location(chat_id=call.message.chat.id, latitude=39.768123190012524, longitude=64.4555875754962)
        bot.send_photo(call.message.chat.id, photo="https://mediaim.expedia.com/destination/1/0fa07e58724840de3c528174f4eb921a.jpg")
    elif call.data == "Samarqand":
        city = "Samarqand"
        lat=39.650788506245775,
        lon=66.96536115459375
        bot.send_location(chat_id=call.message.chat.id, latitude=39.650788506245775, longitude=66.96536115459375)
        bot.send_photo(call.message.chat.id, photo="https://media-cdn.tripadvisor.com/media/photo-s/0f/78/99/60/photo1jpg.jpg")
    elif call.data == "Xorazm":
        city = "Xorazm"
        lat=41.6087049236975,
        lon=60.589080537994825
        bot.send_location(chat_id=call.message.chat.id, latitude=41.6087049236975, longitude=60.589080537994825)
        bot.send_photo(call.message.chat.id, photo="https://uzbekistan.travel/storage/app/media/nargiza/cropped-images/cropped-images/Khiva-0-0-0-0-1582873764-0-0-0-0-1582873972.jpg")
    elif call.data == "Toshkent":
        city = "Toshkent"
        lat=41.304749483720414,
        lon=69.24904826321587
        bot.send_location(chat_id=call.message.chat.id, latitude=41.304749483720414, longitude=69.24904826321587)
        bot.send_photo(call.message.chat.id, photo="https://uzbekistan.travel/storage/app/media/citys/5e53c06ca0049049451193.jpg")
    elif call.data == "Andijon":
        city = "Andijon"
        lat=40.81494200890437,
        lon=72.28634017881718
        bot.send_location(chat_id=call.message.chat.id, latitude=40.81494200890437, longitude=72.28634017881718)
        bot.send_photo(call.message.chat.id, photo="https://www.atorus.ru/sites/default/files/styles/head_carousel/public/2023-07/DJI_0037.JPG.webp?itok=0kQBrQWv")
    elif call.data == "Namangan":
        city = "Namangan"
        lat=41.00697889164993,
        lon=71.6422163817646
        bot.send_location(chat_id=call.message.chat.id, latitude=41.00697889164993, longitude=71.6422163817646)
        bot.send_photo(call.message.chat.id, photo="https://www.uzembassy.kz/upload/userfiles/images/1402(1).jpg")
    elif call.data == "Navoiy":
        city = "Navoiy"
        lat=40.10286059816718,
        lon= 65.37041118204039
        bot.send_location(chat_id=call.message.chat.id, latitude=40.10286059816718, longitude=65.37041118204039)
        bot.send_photo(call.message.chat.id, photo="https://i.ytimg.com/vi/ZS4cR1rlFgY/maxresdefault.jpg")
    elif call.data == "Jizzax":
        city = "Jizzax"
        lat=40.12271312987222,
        lon=67.87842459802656
        bot.send_location(chat_id=call.message.chat.id, latitude=40.12271312987222, longitude=67.87842459802656)
        bot.send_photo(call.message.chat.id, photo="https://jizzax.uz/uploads/posts/2020-02/1581502596_sanatoriya.jpg")

bot.infinity_polling()