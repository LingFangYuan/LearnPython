from turtle import *

def drawStar(x, y):
    pu()  # 提起画笔
    goto(x, y) # 移动画笔到指定坐标
    pd()  # 放下画笔
    seth(0) # 改变方向
    
    for i in range(5):
        fd(40)
        rt(144)
        
hideturtle()
for x in range(0, 250, 50):
    drawStar(x, 0)
    
done()