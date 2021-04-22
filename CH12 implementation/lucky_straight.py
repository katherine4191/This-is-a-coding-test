string = input()
n = len(string)

def getSum(string):
    total = int(string[0])
    for i in range(1, len(string)):
        total += int(string[i])
    return total

left = getSum(string[0:int(n/2)])
right = getSum(string[int(n/2):])

if(left == right):
    print("LUCKY")
else: 
    print("READY")
