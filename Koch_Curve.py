#Koch_Curve
import turtle
turtle.pensize(2)
turtle.pensize(2)
turtle.pencolor('navy')
turtle.penup()
turtle.goto(-300,100)
turtle.pendown()

# 抽象步驟: 如果是0階，只往前走；如果是一階，就需要前進、轉向、前進、轉向、前進、轉向、前進，
# 共有的是前進，階數控制的是次數，所以邊界是0階，只需前行。

def koch_line(n=1, len=120):
    if n==0:
        turtle.fd(len)
    else:
        for i in [0, 60 , -120, 60]:
            turtle .left(i)
            koch_line(n-1, len/3)

def input_argm():
    # n1=int(input("選擇你要的科克雪花階段數: "))
    # len1=int(input("設定你要的基本長度(70-140): "))
    n2=5
    len2=1000
    koch_line(n2, len2)

input_argm()

turtle.hideturtle()
turtle.done()
