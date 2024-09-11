class HeroDiedError(Exception):
    pass


class GameOverError(Exception):
    pass


try:
    raise HeroDiedError('Рядовой Райан')
except HeroDiedError as exc:
    print(f'Поймано исключение {exc}')
    raise GameOverError('Миссия провалена')