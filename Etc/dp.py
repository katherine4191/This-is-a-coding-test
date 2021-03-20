'''
Q. 1칸 또는 2칸을 이동할 수 있을 때, 입력으로 들어온 경로에 대해서
왼쪽 끝부터 오른쪽 끝으로 도달할 수 있는 모든 경우의 수를 구하는 문제!
'''

N = int(input())
DP =  [0 for _ in range(N)]
arr = list(map(int, input()))

# 맨 처음과 끝은 무조건 1, 0은 연속으로 나오지 않는다.
if arr[1] == 0 and arr[2] == 1:
   DP[1], DP[2] = 0, 1
elif arr[1] == 1 and arr[2] == 0:
   DP[1], DP[2] = 1, 0
else:
   DP[1], DP[2] = 1, 2

for j in range(3, N):
   if arr[j] == 0:
      DP[j] = 0
      continue
   DP[j] = DP[j-1] + DP[j-2]

print(DP[N-1])

'''
3
111     >> 2
4
1101    >> 1
5
11111   >> 5
3
101     >> 1
'''