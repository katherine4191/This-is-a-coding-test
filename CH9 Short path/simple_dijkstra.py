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

''' 
get_shortest_node_idx: 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드의 번호를 반환하는 함수
'''
def get_shortest_node_idx():
    min_dist = INF
    idx = 0
    for i in range(1, n + 1):
        if dist[i] < min_dist and not visited[i]:
            min_dist = dist[i]
            idx = i
    return idx

def dijkstra(n_start): 
    '''시작 노드에 대한 처리'''
    dist[n_start] = 0
    visited[n_start] = True
    for b, cost in graph[n_start]: # 시작 노드와 연결된 간선 확인 및 거리 갱신
        dist[b] = cost

    '''다음 노드에 대한 처리'''
    for i in range(n-1):
        n_now = get_shortest_node_idx() # 현재 방문할 노드의 번호
        print("n_now", n_now)
        visited[n_now] = True
        for b, cost in graph[n_now]: # 현재 노드와 연결된 간선 확인 및 거리 갱신
            next_cost = dist[n_now] + cost # 최단 거리 + 다음에 연결된 노드로 갈 때 드는 거리 비용
            dist[b] = min(next_cost, dist[b]) # 현재 노드를 거쳐서 이동하는 거리가 더 짧다면 다음 노드의 dist가 갱신됨

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