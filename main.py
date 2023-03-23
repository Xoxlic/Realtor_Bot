import telebot
import random
about=['Стаж работы 10 лет','Главный эксперт','Высшее профисианальное образование','Закончила Московский Новый Юридический институт']
bot = telebot.TeleBot('6288590872:AAHsu3rc4ZumYP1lilCOVxr9ZebS_NGJsJc')
Diplomi_img = []
for i in range(1,8):
    image = open(f'B{i}.jpg', 'rb')
    Diplomi_img.append(image.read())
    image.close()
Victory_img = []
for i in range(2):
    image = open(f'V{i}.jpg', 'rb')
    Victory_img.append(image.read())
    image.close()
@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Обо мне")
    markup.add(item1)
    markup.row('Награды', 'Фото')
    markup.row('Телефон риелтора', 'Мой сайт')
    phone = telebot.types.KeyboardButton(text="Отправить телефон", request_contact=True)
    markup.add(phone)
    bot.send_message(m.chat.id,'Добрый день меня зовут Виктория. Я буду рада вам помочь найти самую класную недвижимость. Нажмите то что вы бы хотели обо мне узнать:', reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Обо мне':
        answer = random.choice(about)
        bot.send_message(message.chat.id, answer)
    elif message.text.strip() == 'Награды':
        bot.send_photo(message.chat.id, random.choice(Diplomi_img))
    elif message.text.strip() == 'Фото':
        bot.send_photo(message.chat.id, random.choice(Victory_img))
    elif message.text.strip() == 'Телефон риелтора':
        bot.send_message(message.chat.id, 'https://t.me/+79151889567')
    elif message.text.strip() == 'Мой сайт':
        bot.send_message(message.chat.id, "https://www.incom.ru/vospukova_va/")
@bot.message_handler(content_types=['contact'])
def phone(message):
    if message.contact != None:
        bot.send_message(message.chat.id, "Сейчас вы поделитесь своим контактом")
        f = open('Numbers_klients.txt', 'at', encoding='UTF-8')
        f.write('_'*30+'\n| Имя клиента: \n' +'| '+ str(message.contact.first_name) +
            '\n| Фамилия клиента:\n' +'| '+ str(message.contact.last_name) +
            '\n| Номер телефона:\n' +'| '+ str(message.contact.phone_number) + '\n'+'_'*30)
        f.close()
bot.polling(none_stop=True, interval=0)


