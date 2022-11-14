from random import choice
from time import sleep
from turtle import *

from freegames import floor, square, vector


pattern = []
guesses = []
"""распложение плиток и их цвета."""
tiles = {
    vector(0, 0): ('red', 'dark red'),
    vector(0, -200): ('blue', 'dark blue'),
    vector(-200, 0): ('green', 'dark green'),
    vector(-200, -200): ('yellow', 'khaki'),
    vector(-400, 0): ('#8100A8','#9562FE'),
    vector(-400, -200): ('#FF00CA','#FF2BF0')
}


def grid():
    """разрисовка сетки плиток."""
    square(0, 0, 200, 'dark red')
    square(0, -200, 200, 'dark blue')
    square(-200, 0, 200, 'dark green')
    square(-200, -200, 200, 'khaki')
    square(-400, 0, 200, '#9562FE')
    square(-400, -200, 200, '#FF2BF0')
    update()


def flash(tile):
    """свечение плитки в сетке"""
    glow, dark = tiles[tile]#свечение плиток изначальное
    square(tile.x, tile.y, 200, glow)#параметры  плитки до нажатия
    update()#обновление
    sleep(0.1)#время мигания
    square(tile.x, tile.y, 200, dark)# параметры плитки после нажатия
    update()
    sleep(0.1)# время между переходом мигания плиток


def grow():
    """выбор шаблонов и мигающих плиток."""
    tile = choice(list(tiles))#выбоор плиток из списка (выше)
    pattern.append(tile)#добавление шаблона

    for tile in pattern:
        flash(tile)

    print('нужное колличество нажатий:', len(pattern))#подсчет кол-ва и ответов "миганий" шаблона
    guesses.clear()#уберание "догадок" после нажатие


def tap(x, y):
    """реагирование на касание экрана."""
    onscreenclick(None)# отсутствие экранного клика
    x = floor(x, 200)#пределы размера квадрата при мигании(длина)
    y = floor(y, 200)#пределы размера квадрата при мигании ширина)
    tile = vector(x, y)#
    index = len(guesses)#подсчет кол-ва и ответов "миганий" догадок

    if tile != pattern[index]:#в случае несовпадения
        exit()#

    guesses.append(tile)#добравление догаддок
    flash(tile)#свечение догадки плитки при нажатии
    if len(guesses) == len(pattern):#сравнение ответов шаблона и догадок
        grow()

    onscreenclick(tap)#высвечивание экранного клика на экран


def start(x, y):
    """начало игры."""
    grow()
    onscreenclick(tap)#старт при нажатии на любую плитку


setup(800, 400,400,400)#размеры всплывающего окна и его расположение на мониторе
hideturtle()#скрытие курсора черепахи(сделание черепахи невидимой)
tracer(False)#выключение анимации черепахи
grid()
onscreenclick(start)
done()
