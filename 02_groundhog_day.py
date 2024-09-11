# -*- coding: utf-8 -*-
import random

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

ENLIGHTENMENT_CARMA_LEVEL = 777
day = 0
CARMA_LEVEL = 0


def bad_carma():
    dice = random.randint(1, 6)
    if dice == 1:
        raise BaseException("IamGodError")
    elif dice == 2:
        raise BaseException("DrunkError")
    elif dice == 3:
        raise BaseException("CarCrashError")
    elif dice == 4:
        raise BaseException("GluttonyError")
    elif dice == 5:
        raise BaseException("DepressionError")
    elif dice == 6:
        raise BaseException("SuicideError")


def check_bad_day():
    check = random.randint(1, 13)
    if check == 6:
        bad_carma()
        print("Bad day, sorry...")
    else:
        print("It's yours day!")
        return 2


def one_day(CARMA_LEVEL):

    print("*" * 10, 'Day - ', day, "*" * 10)
    carma = random.randint(1, 7)

    try:
        CARMA_LEVEL = CARMA_LEVEL + carma - check_bad_day()
    except BaseException as exc:
        print(f'Y A unlucky, yours bad carma is {exc}')


    return CARMA_LEVEL


while CARMA_LEVEL < ENLIGHTENMENT_CARMA_LEVEL:
    CARMA_LEVEL = one_day(CARMA_LEVEL)
    print(f'------------{CARMA_LEVEL} CARMA_LEVEL')
    day += 1
