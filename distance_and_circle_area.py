import math

def distance(x1, y1, x2, y2):
    dx=x2-x1
    dy=y2-y1
    dsquared=dx**2+dy**2
    result=math.sqrt(dsquared)
    # print(result)
    return result

def area(r):
    area1=r*2*math.pi
    # print(area1)
    return area1

def circle_area(xc,yc,xp,yp):
    print (area(distance(xc,yc,xp,yp)))
    #return area(distance(xc,yc,xp,yp))

#distance(1,2,4,6)
#area(5)
circle_area(1,2,4,6)