#simple pong game in python


import turtle  #this modules let you do some basic graphics and its great getting started with games
import winsound

vn = turtle.Screen()
vn.title("pong with vignesh")
vn.bgcolor('black')
vn.setup(width=800, height=600)
vn.tracer(0)          #its actually stop the window from updating

#score

score_a = 0
score_b = 0


#paddle A

paddle_a = turtle.Turtle()   #creating a class 
paddle_a.speed(0)            #speed of animation as max speed
paddle_a.shape('square')
paddle_a.color('red')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)





#paddle B

paddle_b = turtle.Turtle()   #creating a object
paddle_b.speed(0)            #speed of animation as max speed
paddle_b.shape('square')
paddle_b.color('red')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#Ball

ball = turtle.Turtle()   #creating a object 
ball.speed(0)            #speed of animation as max speed
ball.shape('circle')
ball.color('green')
ball.penup()
ball.goto(0,0)
ball.dx = 1     #ball moves by 2pixels
ball.dy = -1    

#player score card
card = turtle.Turtle()
card.speed(0)
card.color('white')
card.penup()
card.hideturtle()
card.goto(0, 260)
card.write('Player A: 0  Player B: 0', align='center',font=('Courier',12, 'normal'))


#function

def paddle_a_up():
    y = paddle_a.ycor()      #ycor- its return the ycordinates
    y +=20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()     
    y -=20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()      
    y +=20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()     
    y -=20
    paddle_b.sety(y)

#keyboard binding
vn.listen()
vn.onkeypress(paddle_a_up, "s")
vn.onkeypress(paddle_a_down, "x")
vn.onkeypress(paddle_b_up, "Up")
vn.onkeypress(paddle_b_down, "Down")

#main game loop

while True:
    vn.update()


    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border checking

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        card.clear()
        card.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center',font=('Courier',12, 'normal'))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        card.clear()
        card.write('Player A: {}  Player B: {}'.format(score_a, score_b), align='center',font=('Courier',12, 'normal'))



    #paddle and ball collision
        
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor() -40): 
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor() -40): 
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
    

    