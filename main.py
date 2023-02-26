import telebot
from telebot import types

bot_token = '6225139341:AAExDUMuTYt88zrK8AJ0oKrU0apoEq2gheA'
bot = telebot.TeleBot(bot_token, parse_mode=None)

# inline keyboard button
# def order_markups():
#     inline_buttons = [
#         telebot.types.InlineKeyboardButton(
#             text="Green Card haqida ma'lumot", url="https://telegra.ph/Green-Card-haqida-malumot-10-03"
#         )
#     ]
#     reply_markup = telebot.types.InlineKeyboardMarkup(row_width=True)
#     reply_markup.add(*inline_buttons)
#     return reply_markup



# start button
def start_button_markup():
    reply_markup = telebot.types.ReplyKeyboardMarkup(
        # one_time_keyboard=True,
        row_width=2,
        resize_keyboard=True
    )
    itembtn1 = types.KeyboardButton("👨🏻‍💻 About Me 👨🏻‍💻")
    itembtn2 = types.KeyboardButton("📃 My CV 📃")
    itembtn3 = types.KeyboardButton("🏛 Education 🏛")
    itembtn4 = types.KeyboardButton("💻 Work 💻")
    itembtn5 = types.KeyboardButton("🤵🏻 My Skills 🤵🏻")
    itembtn7 = types.KeyboardButton("🥷🏻 My Character 🥷🏻")
    itembtn10 = types.KeyboardButton("☎ Contact Me ☎")
    itembtn11 = types.KeyboardButton("_____copyright_____")
    reply_markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5,  itembtn7, itembtn10, itembtn11)
    return reply_markup


# school button
def school_button():
    reply_markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=True,
        row_width=2,
        resize_keyboard=True
    )
    item1 = types.KeyboardButton("🏣 School 🏣")
    item2 = types.KeyboardButton("🏫 Technikum 🏫")
    item3 = types.KeyboardButton("🏛 University 🏛")
    item4 = types.KeyboardButton("🏪 Mohirdev School 🏪")
    item5 = types.KeyboardButton("🏢 Training center 🏢")
    reply_markup.add(item1, item2, item3, item4, item5)
    return reply_markup


# charackter button
def character_button():
    reply_markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=True,
        row_width=2,
        resize_keyboard=True
    )
    item1 = types.KeyboardButton("🛸 Interests 🛸")
    item2 = types.KeyboardButton("🎮 Hobbies 🎮")

    reply_markup.add(item1, item2)
    return reply_markup


# contact button
def contact_button():
    reply_markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=True,
        row_width=2,
        resize_keyboard=True
    )
    item1 = types.KeyboardButton("📞 Phone Number 📞")
    item2 = types.KeyboardButton("📬 My Email 📬")
    item3 = types.KeyboardButton("📨 My Telegram 📨")
    item4 = types.KeyboardButton("📱 My Instagram 📱")
    item5 = types.KeyboardButton("🌎 My Facebook 🌎")
    item6 = types.KeyboardButton("📝 My Twitter 📝")
    item7 = types.KeyboardButton("🖥 My Linkedin 🖥")
    item8 = types.KeyboardButton("🐱 My Github 🐱")
    reply_markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
    return reply_markup



@bot.message_handler(commands=['start'])
def start_message(message):
        getname = str(message.from_user.first_name)
        bot.reply_to(message, f"😊 Assalomu alaykum! {getname} \n 👤 Diyorbek Jabborovning shaxsiy telegram botiga xush kelibsiz. \n"
                              f"🤖 Bu bot yordamida Diyorbek Jabborov haqida ko'proq ma'lumot bilib olishingiz mumkin!", reply_markup=start_button_markup())



@bot.message_handler(func=lambda m: True)
def echo_message(message):
    if message.text == "👨🏻‍💻 About Me 👨🏻‍💻":
        text = "Assalomu alaykum! 🙂\n" \
               "                     \n"\
               "🧑🏻‍💼Mening ismim Diyorbek Jabborov\n" \
               "                     \n" \
               " 🏛Men O'zbekiston Milliy universiteti talabasiman.\n" \
               "                     \n" \
               "📗Amali matematika fakulteti\n" \
               "📘Axborot tizimlari va texnalogiyalar yo'nalishi \n" \
               "                     \n" \
               "⏰Hozir 2-kurs talabasiman \n" \
               "                     \n" \
               "🏡Qashqadaryo viloyati Kitob tumanida tug'ilganman\n" \
               "                     \n" \
               "⌛️2002-yil 1-iyulda\n" \
               "                     \n" \
               "👨🏻‍💻Men O'zbekiston Respublikasi Innovatsion rivojlanish vazirligida Hardware va Software dasturchi bo'lib faoliyat olib boraman.\n" \
               "                     \n" \
               "😅Men haqimda shu bot orqali bilib olishingiz mumkin\n" \
               "                     \n" \
               "🤲🏻E'tiboringiz uchun rahmat!\n"

               # "👉Green Card haqida umumiy malumot bilan tanishish uchun pastdagi knopkani boshing👇 <a href='https://telegra.ph/Green-Card-haqida-malumot-10-03'>.</a>"
        # bot.send_message(message.from_user.id, text, parse_mode='HTML', reply_markup=order_markups())
        bot.send_message(message.from_user.id, text)
    elif message.text == "📃 My CV 📃":
        text = "mening cv malumot pdf shaklda"
        bot.send_message(message.from_user.id, text)
    elif message.text == "🏛 Education 🏛":
        text = "🏫Ushbu bo'limda siz men ta'lim olgan joylar haqida ma'lumot olishingiz mumkin,\n" \
               "Iltimos sizni qiziqtirgan tugmani tanlang: \n" \
               "👇🏻👇🏻👇🏻👇🏻"
        msg2 = bot.send_message(message.from_user.id, text, reply_markup=school_button())
        bot.register_next_step_handler(msg2, all_education)
    elif message.text == "💻 Work 💻":
        text = "🏢Mening ish joyim \n" \
                "              \n" \
                "💵Oldin men Freelancer bo'lib ishlaganman\n" \
                "                     \n" \
                "👨‍💼Hozirda men Innavatsion rivojlanish vazirligida amaliyotchi bo'lib ishlayman"
        ping = open("photo/Innovatsiay_photo.jpg", 'rb')
        bot.send_photo(message.from_user.id, ping, text)

    elif message.text == "🤵🏻 My Skills 🤵🏻":
        text = "🧠Mening dasturlash bo'yicha bilimlarim\n" \
                "        \n" \
                "🤖Suniy intellekt: \n" \
                "   🔢Numpy \n" \
                "   🐼Pandas \n" \
                "    \n" \
                "🛠Backend: \n" \
                "           \n" \
                "   🐍Python\n" \
                "   🥷🏻Django \n" \
                "   🦸🏻‍♂️Django Rest Framwork \n" \
                "   🌶Flask \n" \
                "   🤖Telegram bot \n" \
                "      \n" \
                "✨Frontend: \n" \
                "            \n" \
                "   🔹Html \n" \
                "   🔸Css \n" \
                "           \n" \
                "📦Database: \n" \
                "        \n" \
                "   🐘PostgreSQL \n" \
                "   ✒️SQLite \n" \
                "   🐬MySQL \n" \
                "🏆Qo'shimcha imkoniyatlar: \n" \
                "       \n" \
                "   🌎Git-dan foydalanish \n" \
                "   🐉Linux operatsion tizimida ishalsh \n" \
                "   🕹Tarmoq admistratorligi \n" \
                "        \n" \
                "💻Men ko'p hollarda Linuxda ishlayman \n" \
                "          \n" \
                "🧠E'tiboringiz uchun rahmat! "

        bot.send_message(message.from_user.id, text)

    elif message.text == "🥷🏻 My Character 🥷🏻":
        text = "👨‍💼Mening xarakterim"
        msg4 = bot.send_message(message.from_user.id, text, reply_markup=character_button())
        bot.register_next_step_handler(msg4, all_character)

    elif message.text == "mening servisim":
        text = "servisim haqida"
        bot.send_message(message.from_user.id, text)

    elif message.text == "☎ Contact Me ☎":
        text =  "📥Bu yerda mening 📱ijtimoiy tarmoqdagi akkauntlarimni ko'rishingiz mumkin. \n" \
                "🔻Buning uchun pastdagi tugmalardan foydalaning: \n" \
                "👇🏻👇🏻👇🏻👇🏻"
        msg5 = bot.send_message(message.from_user.id, text, reply_markup=contact_button())
        bot.register_next_step_handler(msg5, all_contact)
    elif message.text == "_____copyright_____":
        text =  "________________2️⃣0️⃣2️⃣3️⃣________________ \n" \
                "        \n" \
                "| 👤Men Diyorbek Jabborov                  \n" \
                "| ❗ Barcha huquqlar ximoyalangan.          \n" \
                "| ✅Bu botdagi barcha ma'lumotlar to'gri   \n" \
                "            \n" \
                "_________________________________________"
        bot.send_message(message.from_user.id, text)


def all_education(message):
    if message.text == "🏣 School 🏣":
        text = "🏫 Mening maktabim\n" \
               "                  \n" \
               "🏢 Qashqadaryo viloyati, Kitob Tumani, Sevaz shaharchasida joylashgan 45-maktabda ta'lim olganman.\n" \
               "                   \n" \
               "⏳ 2009-2020 yillar"
        ping = open("photo/45-maktab.jpg", 'rb')
        bot.send_photo(message.from_user.id, ping, text, reply_markup=start_button_markup())
        # bot.send_message(message.from_user.id, text, reply_markup=start_button_markup())

    elif message.text == "🏫 Technikum 🏫":
        text1 = "🏛Mening texnikum\n" \
                "                \n" \
                "🏢Men maktabni tamomlaganimdan so'ng Toshkent axborot texnalogiyalar texnikumiga o'qishga kirdim.\n" \
                "                        \n" \
                "👨🏻‍🎓Men u yerdan Kompyuter Injenering kasbini o'rgandim.\n" \
                "                       \n" \
                "⏳2020-2021 yillar"
        ping = open("photo/tatt.jpg", 'rb')
        bot.send_photo(message.from_user.id, ping, text1, reply_markup=start_button_markup())
        # bot.send_message(message.from_user.id, text1, reply_markup=start_button_markup())
    elif message.text == "🏛 University 🏛":
        text2 = "🏛Mening Universitetim\n" \
                "               \n" \
                "🏢Mirzo Ulug'bek nomidagi O'zbekiston Milliy Universiteti\n" \
                "👨🏻‍🎓Amaliy matematika fakulteti\n" \
                "         \n" \
                "⏳2021 - (2025)"
        ping = open("photo/milliy_universiteti.jpg", 'rb')
        bot.send_photo(message.from_user.id, ping, text2, reply_markup=start_button_markup())
        # bot.send_message(message.from_user.id, text2, reply_markup=start_button_markup())

    elif message.text == "🏪 Mohirdev School 🏪":
        text5 = "👤Menga Juda katta foydasi tekkan MohirDev o'quv markazi \n" \
                "        \n" \
                "🏪Bu o'quv markaz tufayli dasturlashga kirib kelganimdan so'ng juda katta foyda oldim. " \
                "🤖Hozirgi vaqtda ham DataScince va suniy intellekt darlarida o'qiyman. \n " \
                "       \n" \
                "🤲🏻MohirDev jamoasiga rahmat \n" \
                "⌛️2021 - 2023 (hozirgi vaqt)"
        ping = open("photo/mohirdev.jpg", 'rb')
        bot.send_photo(message.from_user.id, ping, text5, reply_markup=start_button_markup())


    elif message.text == "🏢 Training center 🏢":
        text3 = "🏦Mening o'quv markazim \n" \
                "                     \n" \
                "💻Men dasturlashni o'rgatadigan TechSchool o'quv markazni " \
                "Web dasturlash yo'nalishi tamomlaganman.\n" \
                "     \n" \
                "🧑🏻‍💼Hozirda men Hardware va Software mutaxasis bo'lib faoliyat yuritaman\n" \
                "             \n" \
                "🖥Kelajakda Suniy intellekt mutaxasisi bo'lmoqchiamn. Hozirda Suniy intellektni o'rganyapman\n" \
                "⏳2021(02) - 2021(09)"
        ping = open("photo/tech_school.jpg", 'rb')
        bot.send_photo(message.from_user.id, ping, text3, reply_markup=start_button_markup())
        # bot.send_message(message.from_user.id, text3, reply_markup=start_button_markup())


def all_character(message):
    if message.text == "🛸 Interests 🛸":
        text =  "🏆Mening qiziqishlarim: \n" \
                "       \n" \
                "🧠Neyron tarmoqlar \n" \
                "🤖Robototexnika sohasi \n" \
                "🌌Kosmonavtika \n" \
                "📊Data Scince \n" \
                "🚘Eng so'ngi turdagi mashinalar \n" \
                "🏗Dizayn (SolidWorks) \n" \
                "🏢Baland binolar \n" \
                "🧗🏻‍♂️Tog'lar \n" \
                "📚Kitob o'qish(fantastika) \n" \
                "🕹Gamerlik (ModernWarships, Dota, CSGO)\n" \
                "👽Kino ko'rish (fantastika, dasturlashga, xakerlikka oid) \n" \
                "      \n" \
                "🙂 E'tiboringiz uchun rahmat 🙂"
        bot.send_message(message.from_user.id, text, reply_markup=start_button_markup())

    elif message.text == "🎮 Hobbies 🎮":
        text1 = "🥳Mening sevimli mashg'ulotlarim: \n" \
               "       \n" \
                "👨🏻‍💻Har doim yangilik yaratish \n" \
                "🧑🏻‍💼O'z ustimda tinmasdan ishlash va yangi narsalar o'rganish \n" \
                "⛷Adrenalin beradigan mashg'ulotlar \n" \
                "🚵🏻‍♀️Sovuqda velosiped haydash \n" \
                "🎸Qo'shiq aytish, gitara chalish (asosan Konsta)  \n" \
                "📚O'zni rivojlantirishga yordam beradigan kitoblar o'qish \n" \
                "🔭Kosmosdagi jismlar haqida qiziqarli maqolalar o'qish (ko'proq qora tuynik haqida) \n" \
                "🏙Dunyo bo'ylab sayohat (tabiat bag'rida sokin joyda kofe ichib kod yozish) \n" \
                "     \n" \
                "😇Rahmat🙂"

        bot.send_message(message.from_user.id, text1, reply_markup=start_button_markup())


def all_contact(message):
    if message.text == "📞 Phone Number 📞":
        text =  "📱Mening shaxsiy telfon nomerim: \n" \
                "      📞 +998912168087"
        bot.send_message(message.from_user.id, text, reply_markup=start_button_markup())
    elif message.text == "📬 My Email 📬":
        text1 = "📩Mening elektron pochta manzilim: \n" \
                "      💌 diyorbekdjabborov2002@gmail.com"
        bot.send_message(message.from_user.id, text1, reply_markup=start_button_markup())
    elif message.text == "📨 My Telegram 📨":
        text2 = "📥Mening telegram manzilim: \n" \
                "      📤 @djabborov_diyorbek"
        bot.send_message(message.from_user.id, text2, reply_markup=start_button_markup())
    elif message.text == "📱 My Instagram 📱":
        text3 = "📲Mening instagram manzilim: \n" \
                "     💤 www.instagram.com/diyorbek_djabborov"
        bot.send_message(message.from_user.id, text3, reply_markup=start_button_markup())
    elif message.text == "🌎 My Facebook 🌎":
        text4 = "🌎Mening Facebook manzilim: \n" \
                "       🪐 https://www.facebook.com/djabborovdiyorbek"
        bot.send_message(message.from_user.id, text4, reply_markup=start_button_markup())
    elif message.text == "📝 My Twitter 📝":
        text4 = "📖Mening twitter manzilim: \n" \
                "      📝@diyordjabborov"
        bot.send_message(message.from_user.id, text4, reply_markup=start_button_markup())
    elif message.text == "🖥 My Linkedin 🖥":
        text4 = "💻Mening Linkedin manzilim: \n" \
                "      🖥 https://www.linkedin.com/in/diyorbek-jabboroov-91a000265"
        bot.send_message(message.from_user.id, text4, reply_markup=start_button_markup())
    elif message.text == "🐱 My Github 🐱":
        text5 = "💻Mening github manzilim: \n" \
                "      🖥 https://github.com/Diyorbek-Jabborov"
        bot.send_message(message.from_user.id, text5, reply_markup=start_button_markup())



bot.polling(none_stop=True)

