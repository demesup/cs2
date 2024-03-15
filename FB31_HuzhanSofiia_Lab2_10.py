# Дан текст. Визначте, скільки в ньому слів, що складаються з 1, 2, ..., N букв.

text = """У всякого своя доля
І свій шлях широкий,
Той мурує, той руйнує,
Той неситим оком
За край світа зазирає,
Чи нема країни,
Щоб загарбать і з собою
Взять у домовину.
Той тузами обирає
Свата в його хаті,
А той нишком у куточку
Гострить ніж на брата.
А той, тихий та тверезий,
Богобоязливий,
Як кішечка підкрадеться,
Вижде нещасливий
У тебе час та й запустить
Пазурі в печінки, —
І не благай: не вимолять
Ні діти, ні жінка.
А той, щедрий та розкошний,
Все храми мурує;
Та отечество так любить,
Так за ним бідкує,
Так із його, сердешного,
Кров, як воду, точить!..
А братія мовчить собі,
Витріщивши очі!
Як ягнята. «Нехай, — каже, —
Може, так і треба».
Так і треба! бо немає
Господа на небі!
А ви в ярмі падаєте
Та якогось Раю
На тім світі благаєте?
Немає! немає!
Шкода й праці, схаменіться.
Усі на сім світі —
І царята, і старчата —
Адамові діти.
І той... і той... А що ж то я?
Ось що, добрі люди:
Я гуляю, бенкетую
В неділю і в будень.
А вам нудно! жалкуєте!
Єй-богу, не чую.
І не кричіть! Я свою п’ю,
А не кров людськую!
"""

symbols_to_replace = [',', '-', '.', '«', '—', '!', '\n', '?', '(', ')', ':', ';']
for symbol in symbols_to_replace:
    text = text.replace(symbol, ' ')

newText = text.split(" ")
count = {}
for word in newText:
    index = len(word)
    if index == 0:
        continue
    if index in count:
        count[index] += 1
    else:
        count[index] = 1

for l in sorted(count.items()):
    print(l)