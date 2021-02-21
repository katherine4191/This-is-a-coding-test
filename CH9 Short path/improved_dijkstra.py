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
    pass

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