import math

def mysqrt(a):
    x=a/2
    while True:
        y=(x+a/x)/2
        if y==x:
            return y
        x=y

def test_square_root(list_of_a):
    title1a="a"
    title1b="mysqrt(a)"
    title1c="math.sqrt(a)"
    title1d="diff"

    title2a="-"
    title2b="---------"
    title2c="------------"
    title2d="----"

    spacing1=" "
    spacing2=" "*3
    spacing3=""

    print(title1a, spacing1, title1b, spacing2, title1c, spacing3, title1d)
    print(title2a, spacing1, title2b, spacing2, title2c, spacing3, title2d)

    for a in list_of_a:
        col1=float(a)
        col2=mysqrt(a)
        col3=math.sqrt(a)
        col4=abs(mysqrt(a)-math.sqrt(a))

        print(col1, "{:<13f}".format(col2), "{:<13f}".format(col3), col4)

test_square_root(range(1,10))