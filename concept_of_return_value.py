from turtle import done


def compare(x, y):
    if x>y:
        return print("1 ,x is bigger")
    elif x<y:
        return print("-1, y is bigger")
    else:
        return print("0, they are equal")

def input_num():
    x=int(input('Enter a number for the value of x: '))
    y=int(input('Enter a number for the value of y: '))
    compare(x, y)

input_num()

