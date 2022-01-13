def find(w, k, start_index=0):  #參數為單字、字符、跟可變動的起始位置
    index=start_index           #將變數index指定為可變動的起始位置start_index
    while index<len(w):         #當index值小於單字字符數，迴圈啟動
        if w[index]==k:         #如果單字裡有符合字符:
            print(index)        #輸出index值，讓操作者確認
            return index        #返回index值，讓python做後續運用
        index+=1                #作為迴圈的計數器，若>=len(w)則迴圈終止
    print(-1)                   #如果迴圈結束而沒有找到字符，輸出-1給操作者
    return -1                   #如果迴圈結束而沒有找到字符，返回-1給python

find('jamese', 'e', 0)

def count_by_for(w, k):         #將參數設為單字、關鍵字符
    count=0                     #初始化變數count，讓count的存在符合規範
    for i in w:                 #遍歷關鍵字w裡的每一個字符
        if i==k:                #只要有字符=關鍵字福
            count+=1            #變數count+1
    print(count)                #for迴圈結束時，輸出變數count終值

count_by_for('jameseee', 'e')   

def count_by_find(w, k):        #將參數設為單字、關鍵字符
    count=0                     #初始化變數count，讓count的存在符合規範
    index=0                     #初始化變數index，讓index的存在符合規範
    while index<len(w):         #當index值小於單字字符數，迴圈啟動
        if w[index]==k:         #當單字字符=關鍵字福
            count+=1            #變數count+1
        index+=1                #程式碼走完時變數index+1
    print(count)                #輸出變數count終值，讓操作者確認

count_by_find('jameseee', 'e')
