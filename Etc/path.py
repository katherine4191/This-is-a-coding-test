'''
Q. 도시 간에 방향 정보가 주어진다(양방향에 해당). 
이 도시들 간에 하나라도 연결되어있는 네트워크를 건설하고자 할 때 최소 비용을 구는 문제
'''
N = int(input())
g_key, city = 0, {}
graph = [[int(1e5) for _ in range(N)] for _ in range(N)]

for i in range(N):
    a, b, cost = input().split()
    if a not in city:
        city[a] = g_key; g_key += 1
    if b not in city:
        city[b] = g_key; g_key += 1
    
    graph[a][b], graph[b][a] = cost, cost

N = len(city.keys())
dist = [[int(1e5) for _ in range(N)] for _ in range(N)]
for k in range(N):
    for a in range(N):
        for b in range(N):
            dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

print(dist)
# 여기서는 beijing, seoul, tokyo, hawaii 이렇게 순서로 네트워크를 구축할 때 12 최소 비용

'''
6
seoul beijing 3
beijing hawaii 10
seoul tokyo 4
seoul hawaii 6
tokyo hawaii 5
beijing tokyo 5
>> 12

3
seoul busan 10
busan daegu 7
daegu busan 2
>> 12
'''