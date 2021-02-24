# ch 9. 미래 도시
# 방문 판매원 1번 회사 -> k번 회사 -> X번 회사
# 방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 구하시오

import heapq # 우선 순위 큐
import sys
input = sys.stdin.readline # input의 개수가 많을 때
INF = int(1e9) # 무한을 의미하는 값

def dijkstra(n_start, graph, dist):
    que = []
    heapq.heappush(que, (0, n_start))
    dist[n_start] = 0
    while que:
        dist_now, n_now = heapq.heappop(que)
        if dist[n_now] < dist_now:
            continue
        for b, cost in graph[n_now]:
            next_cost = dist[n_now] + cost
            if next_cost < dist[b]:
                dist[b] = next_cost
                heapq.heappush(que, (dist[b], b))

if __name__ == '__main__':
    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    dist = [INF] * (n + 1)

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append((b, 1))
        graph[b].append((a, 1)) # 양방향

    x, k = map(int, input().split()) # 1 -> k -> x
    answer = 0
    dijkstra(1, graph, dist)
    answer += dist[k]

    dist = [INF] * (n + 1)
    dijkstra(k, graph, dist)
    answer += dist[x]
    print(answer)

# 다익스트라로 안 되는 이유가 도대체 뭘까
# 1. x와 k의 순서
# 2. 입력으로 받은 간선의 정보는 단방향이 아니라 양방향임!

'''
input 1
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

input 2
4 2
1 3
2 4
3 4
'''