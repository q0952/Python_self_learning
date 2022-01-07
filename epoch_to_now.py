import time

raw_time=time.time()

rest_seconds=int(raw_time%60)    #求餘秒數
minutes=int(raw_time//60)        #分數總計

rest_minutes=int(minutes%60)     #求餘分數
hours=int(minutes//60)           #時數總計

rest_hours=int(hours%24)        #求餘時數
days=int(hours//24)              #日數總計

rest_days=int(days%365)          #求餘日數
years=int(days//365)             #年數總計

print('紀元以來到現在一共經過了:')
print(years, end='年 ')
print(rest_days, end='天 ')
print(rest_hours, end='小時 ')
print(rest_minutes, end='分 又')
print(rest_seconds, end='秒')