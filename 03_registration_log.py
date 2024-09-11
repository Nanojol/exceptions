# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
good_list = []
bad_list = []

file_name = 'registrations.txt'


def create_txt(file, list):
    if file == str(file):
        with open(file, 'w', encoding='utf8') as ttt:

            for lines in list:
                ttt.write(lines)
                ttt.write('\n')

    else:
        print('Используйте текстовый формат')


def name_check(name):
    if name == str(name):
        return True
    else:
        raise ValueError(f'NotNameError')


def mail_check(mail):
    if '@' in str(mail) and '.' in str(mail):
        return True
    else:
        raise ValueError(f'NotEmailError')


def age_check(age):
    if age == int(age) and 10 < int(age) < 99:
        return True
    else:
        raise ValueError(f'Поле возраст НЕ является числом от 10 до 99')


def check(line):
    if line != "":
        # print(line.split(' '))
        name, mail, age = line.split(' ')
        name = str(name)
        mail = str(mail)
        age = int(age)
        if name_check(name) and mail_check(mail) and age_check(age):
            return True
        else:
            return False
    else:
        # print('***********')
        raise ValueError(f'Незаполнены все три поля >{line}<')
        # return False


with open(file_name, 'r', encoding='utf8') as text:
    number = 0
    for line in text:
        number += 1
        line = line[:-1]
        # print(line)
        try:
            checking = check(line)
            print(checking, '-', number)
            good_list.append(line)
        except ValueError as exc:
            print(f'Error - {exc} | in stroke - {line} | number - {number}')
            bad_list.append(line)

create_txt('registrations_good.log', good_list)
create_txt('registrations_bad.log', bad_list)
