# p316 5. 볼링공 고르기
# N개의 공의 무게가 각각 주어질 때, 
# 두 사람이 서로 무게가 다른 볼링공을 고르는 경우의 수를 구하기

# n, m = map(int, input().split())
# bowlings = list(map(int, input().split()))
'''
5 3
1 3 2 3 2

8 5
1 5 4 3 2 4 5 2

10 5
[1, 4, 3, 4, 2, 2, 5, 1, 2, 3]
>> 39

15 9
[3, 1, 7, 8, 3, 4, 6, 8, 1, 8, 6, 9, 1, 2, 7]
>> 96

15 10
[8, 9, 5, 4, 6, 8, 7, 3, 10, 5, 8, 4, 1, 6, 10]
>> 98
'''

n, m  = 15, 10
bowlings = [8, 9, 5, 4, 6, 8, 7, 3, 10, 5, 8, 4, 1, 6, 10]

def solution(data, n, m):
    # solution idea
    # 각 무게별로 볼링공이 몇 개가 있는지 담는 하나의 list 사용
    # 1부터 max num까지의 무게를 담을 수 있는 list 생성
    arr = [0] * (m + 1) # 문제에는 볼링공의 무게 1 ~ 10까지의 범위
    for x in data:
        arr[x] += 1
    
    answer = 0
    for i in range(1, m + 1):
        n -= arr[i] # A가 선택할 수 있는 무게의 개수 제외
        answer += arr[i] * n # B가 선택할 수 있는 무게의 개수 곱하기
    print(answer)

solution(bowlings, n, m)

bowlings.sort()
cnt = 0
for i in range(n-1):
    for j in range(i+1, n):
        if bowlings[i] == bowlings[j]:
            continue
        cnt += 1

print(cnt)



