import heapq # 우선 순위 큐
import sys
input = sys.stdin.readline # input의 개수가 많을 때
INF = int(1e9) # 무한을 의미하는 값

n, e = map(int, input().split()) # 노드의 개수, 간선의 개수
n_start = int(input())

graph = [[] for _ in range(n + 1)] # 각 노드의 연결 정보를 담고 있는 리스트
visited = [False] * (n + 1) # 방문한 적이 있는지 체크하는 리스트
dist = [INF] * (n + 1) # 최단 거리 테이블

for i in range(e):
    a, b, cost = map(int, input().split()) # cost = node a에서 b까지 드는 거리 비용
    graph[a].append((b, cost))

def dijkstra(n_start): 
    global dist
    que = []
    heapq.heappush(que, (0, n_start)) # 첫 번째 원소 기준으로 우선순위를 정함
    dist[n_start] = 0
    while que:
        distance, now = heapq.heappop(que)
        if dist[now] < distance: # 이미 처리되어 최단 거리로 갱신된 경우
            continue
        for b, cost in graph[now]:
            next_cost = distance + cost
            if next_cost < dist[b]: # 현재 노드를 거쳐서 b로 가는 거리가 짧은 경우
                dist[b] = next_cost
                heapq.heappush(que, (dist[b], b))

dijkstra(n_start)

answer = ''
for i in range(1, n + 1):
    if dist[i] == INF:
        answer += "infinite"
    else:
        answer += str(dist[i])
    answer += ", "
print(answer[:-2])

'''
input
# 노드의 개수, 간선의 개수
# 시작 노드 번호
# 간선 정보 a b cost (노드 a에서 노드 b로 갈 때 거리 비용 cost)
6 11
1
1 2 2 
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''