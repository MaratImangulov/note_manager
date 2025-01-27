import datetime # Импортируем библиотеку
today = datetime.datetime.now()  # Вводим сегоднешнее число
print('Текущая дата: ',datetime.datetime.now().date()) # Выводим дату пользователю
while True:  # цикл проверяющий правильность ввода даты пользователем
    dadline = input('Введите дату дедлайла(в формате дд-мм-гггг): ') # ввод даты пользователем
    try:
        dadline = datetime.datetime.strptime(dadline, '%d-%m-%Y')
        break
    except ValueError:
        print('Неправильный формат даты')
day_difference = dadline - today  # находим разницу между дедлайном и сегодняшнем днем
day_difference = day_difference.days # выводим только дни
if day_difference < 0 :  # проверяем истек ли дедлайн
    if day_difference < -4:  # Эти условия нужны для правильности сообщения
        print('Внимание! Дедлайн истёк ', abs(day_difference), ' дней назад')
    else:
        if day_difference == -1:
            print('Внимание! Дедлайн истёк вчера ')
        else:
            print('Внимание! Дедлайн истёк ', abs(day_difference), ' дня назад')

else:
    if day_difference == 0:  # проверяем сегодня ли дедлайн
        print('Дедлайн сегодня!')
    else:
        print('До дедлайна: ',day_difference, ' Дней')
