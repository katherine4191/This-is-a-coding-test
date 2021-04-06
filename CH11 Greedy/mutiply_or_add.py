# p313 2. 곱하기 또는 더하기
import os.path as os_pth
import sys
sys.path.append(os_pth.dirname(os_pth.abspath(os_pth.dirname(__file__))))
from function import *

'''
02984
>> 576

10003387 
>> 672

10000620 
>> 14

10003446 
>> 384

10001082 
>> 32
'''

def operate(c_num, p_num):
    if c_num <= 1 or p_num <= 1:
        return c_num + p_num
    else:
        return c_num * p_num

#str_num = str(input())
str_num = '10001082'

answer = int(str_num[0])
for i in range(1, len(str_num)):
    answer = operate(int(str_num[i]), answer)

print(answer)

def solution(data):
    result = int(data[0]) # 첫 번째 문자를 숫자로 변경하여 대입
    for i in range(1, len(data)):
        # 두 수 중에서 하나라도 '0' or '1'인 경우, 곱하기보다 더하기
        num = int(data[i])
        if num <= 1 or result <= 1:
            result += num
        else:
            result *= num

# 더해야하는 경우에서 0은 인지를 하고 있었는데, 1은 인지하지 못하고 있었다..!
# create_input(10000000, 10005000, 10, True)