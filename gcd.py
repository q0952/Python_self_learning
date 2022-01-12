def gcd(a,b):
    if  b==0:
        return a
    else:
        gcd(b, a%b)
        return gcd(b, a%b)
x=72
y=60

print(x%y)
print(gcd(x,y))