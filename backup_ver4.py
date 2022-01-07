import os
import time

# 1.需要備份的文件與目錄將被指定在一個列表中。
# 例如在 Windows 下:
# source=['"C:\\My Documents"', 'C:\\Code']
# 又例如在 Mac OS X 與 Linux 下:
# source=['/Users/swa/notes']
# 在這裡要注意到我們必須在字符串中使用雙引號
# 用以括起其中包含空格的名稱。
source = ['"C:\\file00168"']

# 2. 備份文件必須存儲在一個主備份目錄中
# 例如在Windows 下:
# target_dir='E:\\Backup'
#又例如在 Mac OS X 與 Linux 下:
# target_dir='/Users/swa/backup'
target_dir = 'C:\\Backup3'

#如果目標目錄還不存在，則進行創建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 3. 備份文件將打包壓縮成zip文件
# 4. 將當前日期作為主備份目錄下的子目錄名稱
today=target_dir+os.sep+time.strftime('%Y%m%d')
# 將當前時間作為zip文件的文件名稱
now=time.strftime('%H%M%S')

# 添加一條來自用戶的註釋以創建zip文件的文件名稱
comment=input('Enter a comment --> ')
# 檢查是否有評論輸入
if len(comment)==0:
    target=today+os.sep+now+'.zip'
else:
    target=today+os.sep+now+'_'+\
        comment.replace(' ', '_')+'.zip'

# 如果子目錄尚不存在則創建一個
if not os.path.exists(today):
    os.mkdir(today)
    print('Successful created directory', today)

# 5. 我們使用zip命令將文件打包成zip格式
zip_command="zip -r {0} {1}".format(target,' '.join(source))

# 執行備份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command)==0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
