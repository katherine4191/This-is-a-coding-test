INF = int(1e9)

n, e = int(input()), int(input())
dist = [[INF] * (n + 1) for _ in range(n + 1)]

for node in range(1, n + 1): # diagonal 대각행렬
    dist[node][node] = 0

for _ in range(e): # 각 간선에 대한 정보 초기화
    a, b, cost = map(int, input().split())
    dist[a][b] = cost

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

print()
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if dist[a][b] == INF:
            print("INFINITY", end = " ")
        else:
            print(dist[a][b], end = " ")
    print()

'''
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
'''