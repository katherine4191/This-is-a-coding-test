N = int(input())
home = []
arr_cnt = [0 for _ in range(N+1)]

for i in range(N):
    home.append(list(map(int, input())))
print(home)

def ispossible(x, y, size): 
    # size 크기만큼 배치가 가능한지
    for i in range(size):
        for j in range(size):
            nx, ny = x + i, y + j
            if nx >= N or ny >= N or home[nx][ny] == 0:
                return False
    return True

for k in range(1, N+1):
    for i in range(N):
        for j in range(N):
            if ispossible(i, j, k):
                arr_cnt[k] += 1

print("total: {0}".format(sum(arr_cnt)))
for i in range(1, N+1):
    if arr_cnt[i] != 0:
        print("size[{0}]: {1}".format(i, arr_cnt[i]))

'''
4
1110
1110
0110
0000
>> total: 11
   size[1]: 8
   size[2]: 3
3
000
000
000
>> total: 0
2
11
11
>> total: 5
   size[1]: 4
   size[2]: 1
'''