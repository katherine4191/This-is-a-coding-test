# p312 모험가 길드
import os.path as os_pth
import sys
sys.path.append(os_pth.dirname(os_pth.abspath(os_pth.dirname(__file__))))
from function import *

# n = int(input())
# adventurer = list(map(int, input().split()))
# answer: 여행을 떠날 수 있는 그룹의 최대 개수

n = 30
adventurer = [1, 4, 4, 1, 2, 1, 8, 2, 2, 8, 4, 6, 4, 3, 3, 9, 7, 2, 10, 4, 10, 10, 9, 4, 7, 9, 6, 1, 3, 10]
adventurer.sort(reverse=True) # fear가 큰 순서대로 정렬

'''
5
[2,3,1,2,2]
>> 2

15
[3, 5, 3, 4, 2, 5, 2, 5, 3, 3, 5, 3, 5, 2, 4]
>> 4

30
[1, 4, 4, 1, 2, 1, 8, 2, 2, 8, 4, 6, 4, 3, 3, 9, 7, 2, 10, 4, 10, 10, 9, 4, 7, 9, 6, 1, 3, 10]
>> 9
'''

cnt = 0
while(True):
    max_fear = adventurer[0]
    if len(adventurer) > max_fear: # 최대 fear보다 모험가의 수가 많을 때
        cnt += 1
        adventurer = adventurer[max_fear:] # 남은 모험가 업데이트
    else:
        if len(adventurer) == max_fear: # 최대 fear보다 모험가의 수가 같을 때
            cnt += 1
        # 최대 fear보다 모험가의 수가 작을 때
        break
print(cnt)

def solution(data):
    data.sort()
    result = 0 # 총 그룹의 수
    count = 0 # 현재 그룹에 포함된 모험가의 수

    for i in data: # fear가 낮은 것부터 하나씩 확인
        count += 1 # 현재 그룹에 해당 모험가를 포함시킴
        if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재 fear 이상일 때, 그룹 결성
            result += 1
            count = 0
    
    print(result) # 총 그룹의 수 출력

# create_input(1, 5, 20, True)
# create_input(1, 10, 30, True)
