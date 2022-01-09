def is_bigger1(x, y):
    return x<y

def is_bigger2(y, z):
    return y<z

def is_between(x, y, z):
    if is_bigger1(x,y) == is_bigger2(y,z):
        print(True)
        return True
    else:
        print(False)
        return False


is_between(3,6,7)
# print(is_bigger1(3, 4))
# print(is_bigger2(4, 5))