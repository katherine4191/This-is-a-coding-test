# n = int(input())
# adventurer = list(map(int, input().split()))
# answer: 여행을 떠날 수 있는 그룹의 최대 개수

n = 5
adventurer = [2,3,1,2,2]

adventurer.sort(reverse=True)

cnt = 0
# while(True):
#     max_fear = max(adventurer)
#     for idx in range(max_fear):
#         #adventurer
print(adventurer)