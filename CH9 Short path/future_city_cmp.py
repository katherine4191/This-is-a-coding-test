from future_city_by_Floyd import Floyd_Warshall
from future_city_by_dijkstra import dijkstra

import heapq # 우선 순위 큐
import sys
import timeit
input = sys.stdin.readline # input의 개수가 많을 때
INF = int(1e9)

if __name__ == '__main__':
    # Dijkstra
    print("Dijkstra")
    start_time = timeit.default_timer()
    n, e = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append((b, 1))
        graph[b].append((a, 1)) # 양방향

    x, k = map(int, input().split()) # 1 -> k -> x
    answer = 0
    dist = dijkstra(n, 1, graph);    answer += dist[k]
    dist = dijkstra(n, k, graph);    answer += dist[x]

    if answer >= INF:
        answer = -1
    print(answer)
    end_time = timeit.default_timer()
    dijkstra_time = end_time - start_time

    # Floyd Warshall
    print("Floyd Warshall")
    start_time = timeit.default_timer()
    n, e = map(int, input().split())
    x, k = map(int, input().split()) # 1 -> k -> x

    dist = Floyd_Warshall(n, e)
    answer = dist[1][k] + dist[k][x]

    if answer >= INF:
        answer = -1
    print(answer)
    end_time = timeit.default_timer()
    Floyd_time = end_time - start_time

    print("dijkstra time: {0}, Floyd time: {1}".format(dijkstra_time, Floyd_time))

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
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
output 1: 3
'''