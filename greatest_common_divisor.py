def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

x=int(input('enter a number: '))
y=int(input('enter a number: '))

print(x%y)
print(gcd(x,y))