from random import randint


def new_login():
    login = 'amatveev_' + str(randint(100, 999)) + '@yandex.ru'
    return login
