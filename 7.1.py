from turtle import * #подключение модуля

#goto() - координаты
#speed() - скорость
#penup() - подымаем перо
#pendown() - опускаем перо
#begin_fill() - начало заливки
#end_fill() - конец заливки
#color() - цвета

#--СОЛНЦЕ--#
def solnce():
    #begin_fill()
    speed(100)
    penup()
    goto(100, 140)
    pendown()
    begin_fill()
    color("yellow")
    for i in range(18):
        forward(100)
        left(100)
    end_fill()

#--ЗЕМЛЯ--#
def zemlya():
    speed(11)
    penup()
    goto(-200, -200)
    pendown()
    color('green', 'yellowgreen')
    begin_fill()
    for i in range(2):
        forward(425)
        left(90)
        forward(100)
        left(90)
    end_fill()

#--НЕБО--#
def nebesa():
    speed(11)
    penup()
    goto(-200, -200)
    pendown()
    color('skyblue')
    begin_fill()
    for i in range(2):
        forward(425)
        left(90)
        forward(400)
        left(90)
    end_fill()

#--1-ДОМ--#
def draw():
    penup()
    speed(5)
    goto(-200, 0)
    pendown()
    for i in range(4):
        begin_fill()
        color("red")
        forward(120)
        right(90)
    end_fill()
    begin_fill()
    color("orange")
    left(60)
    forward(120)
    right(120)
    forward(120)
    left(60)
    end_fill()

#--2-ДОМ--#
def draw2():
    penup()
    speed(5)
    goto(0, 0)
    pendown()
    for i in range(4):
        begin_fill()
        color("red")
        forward(120)
        right(90)
    end_fill()
    begin_fill()
    color("orange")
    left(60)
    forward(120)
    right(120)
    forward(120)
    end_fill()

nebesa()
solnce()
zemlya()
draw()
draw2()

#конец
hideturtle()
exitonclick()