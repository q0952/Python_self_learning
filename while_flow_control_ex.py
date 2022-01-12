def a_to_z(w):          #設定為從頭讀取字符
    y=0                 #初始化參數y=0
    while y<len(w):     #當y小於字符長度迴圈啟動，當y>=0的時候迴圈終止
        letter=w[y]     #指定變數為引得字符
        print(letter)   #輸出字符
        y+=1            #賦予新值給y，每次回圈+1，loop

def z_to_a(w):          #設定為從尾讀取字符
    x=len(w)-1          #計算x的字符數
    while x>=0:         #當x>=0，迴圈啟動，當x<0迴圈終止
        letter=w[x]     #指定變數為引得字符
        print(letter)   #輸出字符
        x-=1            #賦予新值給x，每次迴圈-1，loop

word=input('>>> ')      #人機互動設定

a_to_z(word)            #調用從頭讀取字符
print()                 #輸出空白
z_to_a(word)            #調控從尾讀取字符
