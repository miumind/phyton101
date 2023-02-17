import turtle
tao=turtle.Pen()
tao.shape('turtle')
tao.speed(100)

tao.color('red')

tao.penup()
tao.goto(0,0)
tao.pendown()
for i in range(6):
    tao.begin_fill()
    tao.fd(100)
    tao.left(30)
    tao.circle(50,180)
    tao.left(30)
    tao.fd(100)
    tao.left(180)
    tao.color('Red','Pink')
    tao.end_fill()

tao.penup()
tao.goto(10,0)
tao.pendown()

tao.left(30)
for i in range(6):
    tao.begin_fill()
    tao.fd(80)
    tao.left(30)
    tao.circle(50,180)
    tao.left(30)
    tao.fd(80)
    tao.left(180)
    tao.color('Red','Pink')
    tao.end_fill()

tao.penup()
tao.goto(15,-25)
tao.pendown()
tao.begin_fill()
tao.circle(30)
tao.color('Yellow')
tao.end_fill()
