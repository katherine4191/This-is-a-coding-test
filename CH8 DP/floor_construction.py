#n = int(input())
n = 345
div_num = 796796

table = [0 for _ in range(1001)] # 1 <= n <= 1000, table = [0] * 1001
table[1], table[2] = 1, 3

for i in range(3, n + 1):
    table[i] = table[i-1] + 2 * table[i-2]

print(table[n] % div_num)

import random
def create_input(min, max, N):
    input_list = random.sample(range(min,max), N)
    print(input_list)

#create_input(1, 1000, 10)
# input:  [760,    765,    378,    345,    4,  521,    741,    640,    464,    530]
# output: [536911, 448425, 551139, 336313, 11, 373121, 481185, 496871, 646635, 603879]
