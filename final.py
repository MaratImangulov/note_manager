# Ввод данных заметки
username = input('Введите ваше имя: ')
title1 = input('Введите название заголовка1: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки:  ')
created_date = input('Введите дату создания (дд:мм:гггг): ')
issue_date = input('Введите дату оканчания заметки (дд:мм:гггг): ')
# Доп названия заголовка
title2 = input('Введите название заголовка2: ')
title3 = input('Введите название заголовка3: ')
# Создание списка
note = [username, content, status, created_date, issue_date, [title1, title2, title3]]
# Вывод списка
print(note)