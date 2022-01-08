#Koch_snowflake
import turtle

def koch(n, len):
    '''n=科克階數，len=基礎長度'''
    if n==0:
        turtle.fd(len)
    else:
        for i in [0, 60, -120, 60]:
            turtle.left(i)
            koch(n-1, len/3)

level=3
length=500
spin_degree=120

def main():
    turtle.penup()
    turtle.goto(-100, 100)
    turtle.pensize(2)
    turtle.color('green')
    turtle.pendown()

    koch(level, length)
    turtle.rt(spin_degree)
    koch(level, length)
    turtle.rt(spin_degree)
    koch(level, length)
    turtle.rt(spin_degree)
    
    turtle.hideturtle()
    turtle.done()

main()