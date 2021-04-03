# p314 문자열 뒤집기
import os.path as os_pth
import sys
sys.path.append(os_pth.dirname(os_pth.abspath(os_pth.dirname(__file__))))
from function import *

'''
0101010 >> 3

0110101000 >> 3
1101000011 >> 2
0011010001 >> 3
0101000000 >> 2
0111000111 >> 2

00100000001001000111 >> 4
10100000011111010111 >> 4
00111110011011101111 >> 4
01010010010010001010 >> 7
10000110011111110100 >> 4
'''

def get_minCnt(str_num):
    cnt = [0, 0]
    for idx in range(1, len(str_num)):
        p_num, c_num = int(str_num[idx-1]), int(str_num[idx])
        if p_num != c_num: # 연속되지 않을 때
            cnt[p_num] += 1
    l_num = int(str_num[-1]) # 끝에 연속된 구간의 숫자
    cnt[l_num] += 1
    return min(cnt)

#str_num = str(input()) # 0과 1로만 이루어진 문자열
arr = ['0101010']
# arr = ['0110101000', '1101000011', '0011010001', '0101000000', '0111000111']
# arr = ['00100000001001000111','10100000011111010111','00111110011011101111','01010010010010001010','10000110011111110100']
for str_num in arr:
    print(str_num + ",", get_minCnt(str_num))

# 전체 문자열에서 0의 연속된 구간의 개수를 구한다, 1의 연속된 구간의 개수를 구한다.
# 개수가 많은 것의 연속된 구간의 count를 계산한다.

''' <testcase 생성하기> '''
def create_testcase():
    arr = get_input(0, 1, 20, True)
    string = ""
    for num in arr:
        string = string + str(num)
    return string

# for _ in range(5):
#     print(create_testcase(), end = ",")

def solution(data):
    count0 = 0 # 전부 0으로 바꾸는 경우
    count1 = 0 # 전부 1로 바꾸는 경우

    # 첫 번째 원소에 대해서 처리
    if data[0] == '1':
        count0 += 1
    else:
        count1 += 1

    # 두 번째 원소부터 모든 원소를 확인하며
    for i in range(len(data) - 1):
        if data[i] != data[i + 1]: # 연속되지 않을 때
            # 다음 수에서 1로 바뀌는 경우
            if data[i + 1] == '1':
                count0 += 1
            # 다음 수에서 0으로 바뀌는 경우
            else:
                count1 += 1

    print(min(count0, count1))