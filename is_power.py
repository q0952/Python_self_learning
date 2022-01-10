def is_power(a,b):
    if a%b==0:
        if a==b:
            return True
        else: 
            return is_power(a/b, b)
    return False

x=int(input('enter a number for a: '))
y=int(input('enter a number for b: '))

print(is_power(x,y))