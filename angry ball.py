import turtle
import math

def turnleft():
    p.left(5)

def turnright():
    p.right(5)


def fire():
    x = p.xcor()
    y = p.ycor()

    velocity = 50
    angle = p.heading()
    vx = velocity * math.cos(angle * 3.14 / 180.0)   
    vy = velocity * math.sin(angle * 3.14 / 180.0)
    c = ['red','purple','blue','green']
    
#현재위치 = 속도 + 이전위치
    while vx >= 0 :
        p.pensize(width = '10')
        
        if p.ycor() < 0:
            vy *= (-0.8)
            vx *= 0.8
            
        x += vx 
        y += vy
        
        vy -= 10     
       
        
       
       # 그 다음 수평속도는 그대로 나둔 상태에서 수직속도는 한번 더 줄인다.
# 이값을 적용하여 x,y의 좌표를 다시 구하고 다시 시작한다.
        
        p.goto(x,y)
    
p = turtle.Pen()
p.shape('turtle')

screen = p.getscreen()
screen.onkeypress(turnleft, 'Left')
screen.onkeypress(turnright, 'Right')
screen.onkeypress(fire, 'space')

p.goto(+300,0)
p.goto(-300,0)
p.goto(-300,300)
p.goto(-300,0)
screen.listen()
