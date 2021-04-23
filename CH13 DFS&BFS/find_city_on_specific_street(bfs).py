# p340 특정 거리의 도시 찾기
from collections import deque

n, m, k, x = map(int, input().split()) # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
graph = [[] for _ in range(n+1)] # graph [0]이 아니고 []임!!
dist = [-1]*(n+1); dist[x] = 0 # 모든 도시 최단 거리 초기화 및 출발 도시 거리 0 설정

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

# 너비 우선 탐색 수행
dq = deque([x])
while dq:
    now = dq.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next in graph[now]:
        # 아직 방문하지 않은 도시일 때, 최단 거리를 갱신
        if dist[next] == -1:
            dist[next] = dist[now] + 1
            dq.append(next)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if dist[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)