# p315 4. 만들 수 없는 금액
# 가지고 있는 화폐들을 더해서 만들 수 없는 최소 금액
import os.path as os_pth
import sys
sys.path.append(os_pth.dirname(os_pth.abspath(os_pth.dirname(__file__))))
from function import *

'''
15
[3, 1, 7, 8, 3, 4, 6, 8, 1, 8, 6, 9, 1, 2, 7]
>> 75

15
[8, 9, 5, 4, 6, 8, 7, 3, 10, 5, 8, 4, 1, 6, 10]
>> 2

10
[1, 1, 5, 3, 5, 3, 5, 4, 4, 1]
>> 33

10
[1, 4, 3, 4, 2, 2, 5, 1, 2, 3]
>> 28
'''

# n = int(input())
# coins = list(map(int, input().split()))

n, coins = 5, [3, 2, 1, 1, 9]
coins.sort()

# 주어진 화폐들의 조합을 어떻게 만들어야 할지 몰라서 못 풀었다..
amount = 1
for coin in coins: # 1, 1, 2, 3, 9
    if amount < coin:
        break
    amount += coin

print(amount)

'''testcase 만들기'''
arr = get_input(1, 5, 10)
print(len(arr), arr)
