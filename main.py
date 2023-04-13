#Ссылка на бота - https://t.me/KurskProkhorovBattleBot

import telebot
from telebot import types

bot = telebot.TeleBot(".")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'👋 Привет, {message.from_user.first_name}!')
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Начать", callback_data='start') 
    markup.add(button1)
    bot.send_message(message.chat.id, text='Сейчас я расскажу про Курскую битву', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'start':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='start')
        button2 = types.InlineKeyboardButton(">>", callback_data='1') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/start.jpg', 'rb'), 'Среди сражений Второй мировой войны на разных фронтах можно отметить самое главное – Курскую битву или “Сражение на Курской дуге”. Ее даты – 5 июля – 23 августа. Битва закончилась освобождением нескольких крупных городов – Орла, Белгорода и Харькова.', reply_markup=markup)
    elif call.data == '1':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='start') 
        button2 = types.InlineKeyboardButton(">>", callback_data='2') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/1.jpg', 'rb'), 'Зимой-весной 1943 года сражения на Восточном фронте шли с переменным успехом. Несмотря на ряд успешных наступательных операций, в марте 1943 года вермахт смог одержать победу в сражении, которое вошло в историю под названием “Третья битва за Харьков”.', reply_markup=markup)
    elif call.data == '2':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='1') 
        button2 = types.InlineKeyboardButton(">>", callback_data='3') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/2.jpg', 'rb'), 'Немцы вернули себе контроль над частью территории и добились появления на фронте выступа 200 километров в ширину и 150 километров в глубину. Он получил название “Курская дуга”.', reply_markup=markup)
    elif call.data == '3':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='2') 
        button2 = types.InlineKeyboardButton(">>", callback_data='4') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/3.jpg', 'rb'), 'Для наступления немцы выделили свыше 400 танков и самоходных орудий новых типов – “Тигр”, “Пантера” и “Фердинанд”. Всего они задействовали 10 тыс. орудий, 2000 самолетов, 2700 единиц бронетехники и почти 1 млн солдат.Советское командование имело превосходство в живой силе (1,3 млн солдат), танках (от 3.5 до 5 тыс.) и орудиях (от 20 до 27 тыс.).', reply_markup=markup)
    elif call.data == '4':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='3') 
        button2 = types.InlineKeyboardButton(">>", callback_data='5') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/4.jpg', 'rb'), 'Войска были распределены по трем фронтам: Центральный под командованием Рокоссовского. Воронежский под командованием Ватутина. Степной под командованием Конева.', reply_markup=markup)
    elif call.data == '5':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='4') 
        button2 = types.InlineKeyboardButton(">>", callback_data='6') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/5.jpg', 'rb'), 'Информация о немецком наступлении стала известна советской и даже британской разведке уже в апреле 1943 года. Это помогло при подготовке войск и на первом этапе, оборонительном, который длился с 5 по 23 июля 1943 года. В частности, 12 июля произошло самое крупное танковое сражение в мировой истории – на поле под Прохоровкой. 17-23 июля произошло контрнаступление Степного и Воронежского фронтов и немцы были отброшены на исходные позиции.', reply_markup=markup)
    elif call.data == '6':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='5') 
        button2 = types.InlineKeyboardButton(">>", callback_data='7') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/6.jpg', 'rb'), 'В наступательных действиях июля-августа принимали участие не только перечисленные выше три фронта, но и еще два: Брянский и Западный (командующие – генералы Попов и Соколовский). Наступательные операции продолжались с 12 июля по 23 августа. Они получили кодовые названия “Кутузов” и “Румянцев”. В ходе первой был освобожден город Орел, а в ходе второй – Белгород и Харьков (к 23 августа).', reply_markup=markup)
    elif call.data == '7':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='6') 
        button2 = types.InlineKeyboardButton(">>", callback_data='8') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/7.jpg', 'rb'), 'После поражения в битве на Курской дуге немецкое командование осталось без средств для проведения стратегических наступательных операций. Потери сторон до сих пор вызывают массу вопросов, так как различаются методики подсчетов и источниковая база. По советским данным, немцы потеряли около 500 тыс. солдат. Потери Красной армии составила 250 тыс. безвозвратных и 600 тыс. санитарных.', reply_markup=markup)
    elif call.data == '8':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='7') 
        button2 = types.InlineKeyboardButton("Погнали!🚀", callback_data='9') 
        markup.add(button1, button2)
        bot.send_message(call.message.chat.id, 'Окей, давай теперь изучим Танковое сражение под Прохоровкой', reply_markup=markup)
    elif call.data == '9':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='8') 
        button2 = types.InlineKeyboardButton(">>", callback_data='10') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/9.jpg', 'rb'), '12 июля 1943 г. на южном фасе Курской дуги в районе станции Прохоровка произошло одно из крупнейших в военной истории сражений с применением бронетанковых сил. С обеих сторон в сражении было задействовано до 1,2 тыс. танков и самоходно-артиллерийских установок.', reply_markup=markup)
    elif call.data == '10':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='9') 
        button2 = types.InlineKeyboardButton(">>", callback_data='11') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/10.jpg', 'rb'), 'С 5 июля по 23 августа 1943 г. проходили бои за Курскую дугу, в ходе которых германские войска попытались окружить советские части и перейти в наступление. Для выполнения этой задачи они решили воспользоваться плацдармом у железнодорожной станции Прохоровка. Это было единственное удобное место для прохода танков, которым в боях под Курском придавалось большое значение. Поэтому противник бросил сюда тяжёлые танки «Тигр» и самоходные орудия  «Фердинанд». На защиту плацдарма было направлено несколько танковых армий и корпусов.', reply_markup=markup)
    elif call.data == '11':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='10') 
        button2 = types.InlineKeyboardButton(">>", callback_data='12') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/11.jpg', 'rb'), '12 июля в 8 ч. 30 мин. соединениями 5-й гвардейской танковой армии под командованием генерал-лейтенанта П. А. Ротмистрова и 5-й гвардейской армии под командованием генерал-лейтенанта А. С. Жадова после пятнадцатиминутной артиллерийской подготовки и при поддержке авиации был нанесён контрудар. Наиболее трудное встречное танковое сражение пришлось на долю 18-го и 29-го танковых корпусов, вступивших в противостояние со 2-м танковым корпусом СС на 6-километровом участке фронта между хутором Сторожевое и Псёлом, в двух километрах юго-западнее Прохоровки.', reply_markup=markup)
    elif call.data == '12':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='11') 
        button2 = types.InlineKeyboardButton(">>", callback_data='13') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/12.jpg', 'rb'), '«… С зияющими пробоинами, с сорванными гусеницами и башнями среди ржи горели сотни танков. Боеприпасы взрывались, тысячи искр летели во все стороны. Башни с грохотом падали на землю. Бой шёл на земле и в воздухе, с высоты падали горящие самолеты и взрывались. Экипажи подбитых танков, покидая горящие машины, продолжали схватку в рукопашную, орудуя автоматами, гранатами и ножами. Это было неподдающееся воображению месиво огня, металла и людских тел. Все горело вокруг, и, наверное, так художникам следует изображать ад» — вспоминал очевидец сражения.', reply_markup=markup)
    elif call.data == '13':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='12') 
        button2 = types.InlineKeyboardButton(">>", callback_data='14') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/13.jpg', 'rb'), 'Бои за плацдарм продолжались до 14 июля.\nНи одной из сторон не удалось достичь целей поставленных на 12 июля: немцам не удалось захватить Прохоровку, прорвать оборону советских войск и выйти на оперативный простор, а советским войскам не удалось окружить группировку противника.', reply_markup=markup)
    elif call.data == '14':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='13') 
        button2 = types.InlineKeyboardButton(">>", callback_data='15') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/14.jpg', 'rb'), 'Оценки боевых потерь в сражении под Прохоровкой в различных источниках сильно отличаются. Но в основном эти цифры варьируются в пределах 300-400 танков. Потери советских войск за эти два дня составили более 300 танков (по некоторым зарубежным данным до 400). Немецкие войска в этом двухдневном сражении потеряли, по разным источникам, 320-400 танков.', reply_markup=markup)
    elif call.data == '15':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='14') 
        button2 = types.InlineKeyboardButton(">>", callback_data='16') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/15.jpg', 'rb'), 'В сложившейся ситуации германское командование приняло вынужденное решение об отходе на южном фасе Курской дуги и с 16 по 24 июля отвело войска на исходные позиции.', reply_markup=markup)
    elif call.data == '16':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='15') 
        button2 = types.InlineKeyboardButton(">>", callback_data='17') 
        markup.add(button1, button2)
        bot.send_photo(call.message.chat.id, open('pic/16.jpg', 'rb'), 'В память о погибших под Прохоровкой 3 мая 1995 г. к 50-летию Победы в Великой Отечественной войне в Прохоровке был открыт Храм Святых Апостолов Петра и Павла. На мраморных плитах его стен высечены имена 7 тыс. погибших здесь воинов.', reply_markup=markup)
    elif call.data == '17':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("<<", callback_data='16') 
        button2 = types.InlineKeyboardButton("Ну что, поехали!▶️", callback_data='18') 
        markup.add(button1, button2)
        bot.send_message(call.message.chat.id, 'А ты молодец!🏆\nДавай теперь пройдём небольшой тестик😃', reply_markup=markup)

    elif call.data == '18':
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("1️⃣", callback_data='18True') 
        button2 = types.InlineKeyboardButton("2️⃣", callback_data='18False') 
        markup.add(button1, button2)
        bot.send_message(call.message.chat.id, 'В каких датах проходили бои за Курскую дугу?\n\n1️⃣ С 5 июля по 23 августа 1943г.\n2️⃣ С 5 июня по 23 августа 1943г.', reply_markup=markup)
    elif call.data == '18True':
        bot.send_message(call.message.chat.id, 'Ты правильно ответил🏆')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("1️⃣", callback_data='19True') 
        button2 = types.InlineKeyboardButton("2️⃣", callback_data='19False') 
        markup.add(button1, button2)
        bot.send_message(call.message.chat.id, 'Чем закончилась Курская битва?\n\n1️⃣Битва закончилась освобождением – Орла, Белгорода, Харькова.\n2️⃣Битва закончилась освобождением – Белгорода, Харькова', reply_markup=markup)
    elif call.data == '18False':
        bot.send_message(call.message.chat.id, 'Ты неправильно ответил')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("1️⃣", callback_data='19True') 
        button2 = types.InlineKeyboardButton("2️⃣", callback_data='19False') 
        markup.add(button1, button2)
        bot.send_message(call.message.chat.id, 'Чем закончилась Курская битва?\n\n1️⃣Битва закончилась освобождением – Орла, Белгорода, Харькова.\n2️⃣Битва закончилась освобождением – Белгорода, Харькова', reply_markup=markup)
    elif call.data == '19True':
        bot.send_message(call.message.chat.id, 'Ты правильно ответил🏆')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("1️⃣", callback_data='20False') 
        button2 = types.InlineKeyboardButton("2️⃣", callback_data='20True') 
        markup.add(button1, button2)
        bot.send_message(call.message.chat.id, 'В наступательных действиях под кодовыми названиями “Кутузов” и “Румянцев” в ходе второй битвы был освобождён город:\n\n1️⃣Харьков\n2️⃣Белгород и Харьков', reply_markup=markup)
    elif call.data == '19False':
        bot.send_message(call.message.chat.id, 'Ты неправильно ответил')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("1️⃣", callback_data='20False') 
        button2 = types.InlineKeyboardButton("2️⃣", callback_data='20True') 
        markup.add(button1, button2)
        bot.send_message(call.message.chat.id, 'В наступательных действиях под кодовыми названиями “Кутузов” и “Румянцев” в ходе второй битвы был освобождён город:\n\n1️⃣Харьков\n2️⃣Белгород и Харьков', reply_markup=markup)
    elif call.data == '20True':
        bot.send_message(call.message.chat.id,  'Ты правильно ответил🏆')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("1️⃣", callback_data='21True') 
        button2 = types.InlineKeyboardButton("2️⃣", callback_data='21False') 
        markup.add(button1, button2)
        bot.send_message(call.message.chat.id, 'Оценки боевых потерь в сражении под Прохоровкой в различных источниках сильно отличаются. Но в основном эти цифры варьируются в пределах ? танков.\n\n1️⃣300-400\n2️⃣200-400', reply_markup=markup)
    elif call.data == '20False':
        bot.send_message(call.message.chat.id,  'Ты неправильно ответил')
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton("1️⃣", callback_data='21True') 
        button2 = types.InlineKeyboardButton("2️⃣", callback_data='21False') 
        markup.add(button1, button2)
        bot.send_message(call.message.chat.id, 'Оценки боевых потерь в сражении под Прохоровкой в различных источниках сильно отличаются. Но в основном эти цифры варьируются в пределах ? танков.\n\n1️⃣300-400\n2️⃣200-400', reply_markup=markup)
    elif call.data == '21True':
        bot.send_message(call.message.chat.id, 'Ты правильно ответил🏆')
        bot.send_message(call.message.chat.id, 'Спасибо за прохождение теста! Мы надеемся, что наш проект позволил Вам больше узнать о Курской битве и Прохоровского сражения!')
        bot.send_message(call.message.chat.id, 'А мы заканчиваем погружение в наш электронный музей Курской Битвы и Прохоровского сражения')
        bot.send_message(call.message.chat.id, 'А если ты хочешь снова окунуться в наш электронный музей, просто напиши команду /start')
    elif call.data == '21False':
        bot.send_message(call.message.chat.id, 'Ты неправильно ответил')
        bot.send_message(call.message.chat.id, 'Спасибо за прохождение теста! Мы надеемся, что наш проект позволил Вам больше узнать о Курской битве и Прохоровского сражения!')
        bot.send_message(call.message.chat.id, 'А мы заканчиваем погружение в наш электронный музей Курской Битвы и Прохоровского сражения')
        bot.send_message(call.message.chat.id, 'А если ты хочешь снова окунуться в наш электронный музей, просто напиши команду /start')



bot.polling(none_stop=True, interval=0)
