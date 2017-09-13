from turtle import Turtle
from random import randint

### laura ###
laura = Turtle()

laura.color("red")
laura.shape("turtle")

laura.penup()
laura.goto(-160, 100)
laura.pendown()


### satoshi ###
satoshi = Turtle()

satoshi.color("red")
satoshi.shape("turtle")

satoshi.penup()
satoshi.goto(-160, 70)
satoshi.pendown()


### kame ###
kame = Turtle()

kame.color("red")
kame.shape("turtle")

kame.penup()
kame.goto(-160, 40)
kame.pendown()


### tsuru ###
tsuru = Turtle()

tsuru.color("red")
tsuru.shape("turtle")

tsuru.penup()
tsuru.goto(-160, 10)
tsuru.pendown()


for movement in range(100):
    laura.forward(randint(1,5))
    satoshi.forward(randint(1,5))
    kame.forward(randint(1,5))
    tsuru.forward(randint(1,5))
