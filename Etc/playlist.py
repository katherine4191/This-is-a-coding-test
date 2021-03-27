'''
주어진 총 시간 안에 최대로 들어갈 수 있는 시간의 개수와 그 시작 위치를 구하는 문제
제한 조건
- 총 시간 00:00:01 ~ 99:59:59
- 시간    00:00 ~ 59:59
'''
start_idx, max_cnt = 1, 0
N, str_total = map(str, input().split())
N = int(N)
total_hour = list(map(int, str_total.split(":")))

class Time:
    def __init__(self, hours, mins, seconds):
        self.h = int(hours)
        self.m = int(mins)
        self.s = int(seconds)

    def __add__(self, other):
        h = self.h + other.h
        m = self.m + other.m
        s = self.s + other.s

        if s >= 60: # second가 먼저였어야 하는데..! 실수했다..
            s -= 60;    m += 1
        if m >= 60:
            m -= 60;    h += 1
        
        return Time([h,m,s])

playlist = []
for i in range(N):
    minute, second = map(int, input().split())
    playlist.append([0, minute, second])


def getCnt(idx):
    cnt = 0
    # if 더한 시간이 총합을 넘지 않을 때
    # else 넘거나 같을 때
    #   같은 건지, 조금의 시간이라도 재생?먹을 수 있는지! 확인 후 cnt 결정

    return cnt


for idx in range(N):
    cnt = getCnt(i)
    if cnt > max_cnt:
        max_cnt, start_idx = cnt, idx

print(start_idx, max_cnt)

'''
5 00:05:48
09:20
02:22
03:26
00:24
2 2
# start_idx, max_cnt
'''