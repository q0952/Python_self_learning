import turtle
import math

def square(t, length):              #參數僅有烏龜與步長
    """繪製四邊形，t=烏龜，length=邊長，角度角數無法變更。"""
    for i in range(4):              #寫死的4次迴圈
        t.fd(length)                #呼叫烏龜行走單次迴圈步長
        t.lt(90)                    #呼叫烏龜行走單次角度

def polygon1(t, n, length):         #參數除了烏龜、步長，新增參數N邊數
    """繪製多邊形，t=烏龜，n=邊數，length=邊常。"""
    angle=360/n                     #用周長先計算出邊數，後方可以自動引用
    for i in range(n):              #將迴圈次數以參數N自動計算
        t.fd(length)                #呼叫烏龜行走單次迴圈步長
        t.lt(angle)                 #呼叫烏龜行走單次角度

def circle1(t, r):                  #N是一個常數會有計算上的問題而且隨著大小不適用
    """繪製圓形，t=烏龜，r=半徑，寫死邊數採用50繪製近似圓形的多邊形。"""
    circumference=2*math.pi*r       #圓周長=直徑*圓周率
    n=50                            #邊數=50，取近似圓形的多邊形
    length=circumference/n          #烏龜步長=圓周長/邊數
    polygon1(t, n, length)          #呼叫polygon函數繪製圖形

def circle2(t, r):                  #將N轉為自變數隨著調用的大小而自動調整
    """繪製圓形，t=烏龜，r=半徑，邊數=周長1/3近似值，為自適應變數。"""
    circumference=2*math.pi*r       #周長=直徑*圓周率
    n=int(circumference/3)+1        #邊數=取圓周長1/3近似值，自適應變數
    length=circumference/n          #烏龜步長=圓周長/邊數，自適應變數
    polygon1(t, n, length)          #呼叫polygon函數繪製圓形

def arc1(t, r, angle):
    """繪製弧形，t=烏龜，r=半徑，angle=弧形內角。"""
    arc_length=2*math.pi*r*angle/360    #圓弧周長=圓周*圓弧角度/全角
    n=int(arc_length/3)+1               #圓弧邊數=圓弧周長1/3近似值
    step_length=arc_length/n            #烏龜步長=圓弧周長/圓弧邊數
    step_angle=angle/n                  #烏龜轉折角度=圓弧角度/圓弧邊數
    for i in range(n):                  #轉折的次數帶入迴圈成為自適應變數
        t.fd(step_length)               #呼叫烏龜行走每次的弧形邊數步長
        t.lt(step_angle)                #呼叫烏龜每次的弧形角度

def polyline(t, n, length, angle):      #可以重複呼叫的函數，獨立出來方便簡化程式
    """泛化烏龜(繪製)行為，t=烏龜，n=邊數，length=烏龜步長，angle=烏龜轉折角度。"""
    for i in range(n):                  #調用for迴圈重複動作
        t.fd(length)                    #length=烏龜步長
        t.lt(angle)                     #angle=烏龜轉折角度

def polygon2(t, n, length):             #新polygon函數，後段套用polyline函數
    """繪製多邊形，t=烏龜，n=邊數，length=烏龜步長，angle=烏龜轉折角度。"""
    angle=360/n                         #烏龜轉折角度=周長/邊數
    polyline(t, n, length, angle)       #呼叫polyline函數將圖形畫出來

def arc2(t, r, angle):                  #新arc函數，後段套用polyline函數
    """繪製弧形，t=烏龜，r=半徑，angle=圓弧內角。"""
    arc_length=2*math.pi*r*angle/360    #用弧形占比計算弧形周長
    n=int(arc_length/3)+1               #將邊數定義為圓弧1/3近似值
    step_length=arc_length/n            #圓弧步長=圓弧周長/邊數
    step_angle=angle/n                  #用圓弧總角度/邊數計算圓弧每次轉折角度
    polyline(t, n, step_length, step_angle) #呼叫polyline函數將圖形畫出來

def circle3(t, r):
    arc2(t, r, 360)

def petal(t, r, angle):
    """繪製烏龜的葉子，t=烏龜，r=半徑(葉片大小)，angle=角度(葉片大小)。"""
    for i in range(2):
        arc2(t, r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360/n)

def move(t, length):
    """移動烏龜，但是不增加筆畫。"""
    t.pu()
    t.fd(length)
    t.pd()

bob=turtle.Turtle()
move(bob, -200)
flower(bob, n=7, r=100, angle=60)
move(bob, 200)
flower(bob, n=10, r=100, angle=60)
move(bob, 200)
flower(bob, n=20, r=100, angle=60)

bob.hideturtle()
# print(bob)
turtle.mainloop()