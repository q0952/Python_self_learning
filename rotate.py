def rotate_letter(letter,n):            #轉動單一字符
    """
    Rotates a letter by n places. doesn't change other chars.
    
    letter: single-letter string
    n: int
    
    returns: single-letter string
    """

    if letter.isupper():                #調用方法檢查大小寫
        start=ord('A')                  #大寫的起始位置
    elif letter.islower():              #調用方法檢查大小寫
        start=ord('a')                  #小寫的起始位置
    else:
        return letter
    
    c=ord(letter)-start                 #將字符的數字減去起始位置，取得"數字"
    i=(c+n)%26+start                    #將字符與位移數取於除以26得到正確位數，再加上起始數字得到正確編碼"數字"
    return chr(i)                       #將正確數字轉化為解碼字符

def rotate_word(word,n):                #將單字字符一個個解碼再組合起來
    """
    Rotates a word by n places.

    word: string
    n: integer

    Returns: string
    """

    res=''                              #初始化res，此處的雙引號表明其為字串str
    for letter in word:                 #將字符一個個傳入轉動單一字符函數
        res+=rotate_letter(letter,n)    #將結果一個個加入倒res字串
    return res                          #返回值為完成字串

print(rotate_word('cheer',7))
print(rotate_word('melon',-10))
print(rotate_word('sleep',9))