'''
우선순위 Y > O 및 입력으로 주어지는 장르 A, B, C, D, E의 값
Y: 보지 않은 작품, O: 보다 만 작품
출력: 장르, 장르 score, 가로 위치, 세로 위치
'''
class video:
    def __init__(self, g_key, g_score, x, y):
        self.g_key = g_key
        self.g_score = g_score
        self.x = x
        self.y = y

g = ["A", "B", "C", "D", "E"]
g_scores = list(map(float, input().split()))
dict_g = {}
for i in range(5):
    dict_g[g[i]] = g_scores[i]

N, M = map(int, input().split())

arr_info, arr_genre = [], []
for i in range(N):
    arr_info.append(list(map(str, input())))
for i in range(N):
    arr_genre.append(list(map(str, input())))

arr_Y, arr_O = [], []
for i in range(N):
    for j in range(M):
        if arr_info[i][j] == 'Y':
            g = arr_genre[i][j]
            arr_Y.append(video(g, dict_g[g], i, j))
        elif arr_info[i][j] == 'O':
            g = arr_genre[i][j]
            arr_O.append(video(g, dict_g[g], i, j))

arr_Y = sorted(arr_Y, key=lambda v: v.g_score, reverse=True)
arr_O = sorted(arr_O, key=lambda v: v.g_score, reverse=True)

for video in arr_Y:
    print("{0} {1} {2} {3}".format(video.g_key, video.g_score, video.x, video.y))
for video in arr_O:
    print("{0} {1} {2} {3}".format(video.g_key, video.g_score, video.x, video.y))
'''
4.0 3.0 2.0 4.3 5.0
2 3
WYO
YYO
ABC
CDE
>> D 4.3 1 1
   B 3.0 0 1
   C 2.0 1 0
   E 5.0 1 2
   C 2.0 0 2
'''
