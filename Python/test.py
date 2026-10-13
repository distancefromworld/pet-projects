from turtle import *
tracer(0)
screensize(3000, 3000)
k = 20
left(90)

for i in range(8):
    for r in range(4):
        forward(5*k)
        right(30)
        forward(6*k)
        right(150)
    right(60)

pu()
for x in range(-60, 60):
    for y in range(-60, 60):
        goto(x*k, y*k)
        dot(5)
done()
