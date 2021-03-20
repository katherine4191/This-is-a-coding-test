'''
입력으로 주어진 시간들 중 공통된 시간을 찾아 출력하는 문제!
08:00 ~ 09:00, 00:30 ~ 00:45처럼 앞자리가 0이 나오는 것에 유의해야한다!
00:00..ㅠㅜ
'''
N = int(input())
start_time, end_time = [], []
   
for i in range(N):
   str_time = input().split()
   if(str_time[0][0]=="0"): # HH: 02:xx
      if(str_time[0][1]=="0"): # HH: 00:xx
         start_time.append(int(str_time[0][3:]))
      else:
         start_time.append(int(str_time[0][1:2] + str_time[0][3:]))
   else:
      start_time.append(int(str_time[0][0:2] + str_time[0][3:]))

   if(str_time[2][0]=="0"):
      if(str_time[2][1]=="0"): # HH: 00:xx
         end_time.append(int(str_time[2][3:]))
      else:
         end_time.append(int(str_time[2][1:2] + str_time[2][3:]))
   else:
      end_time.append(int(str_time[2][0:2] + str_time[2][3:]))

# print(start_time, end_time)
start, end = max(start_time), min(end_time)

if start > end:
   print("-1") 
else:
   st_zero, e_zero = "", ""
   if start < 100:
      st_zero = "00"
   elif start < 1000:
      st_zero = "0"
   
   if end < 100:
      e_zero = "00"
   elif end < 1000:
      e_zero = "0"
      
   start_ans, end_ans = st_zero + str(start), e_zero + str(end)
   print(start_ans[0:2]+":"+start_ans[2:]+" ~ "+end_ans[0:2]+":"+end_ans[2:])

'''
3
12:00 ~ 23:59
11:00 ~ 18:00
14:00 ~ 20:00   >> 14:00 ~ 18:00
2
05:30 ~ 11:30
00:30 ~ 08:00   >> 05:30 ~ 08:00
'''