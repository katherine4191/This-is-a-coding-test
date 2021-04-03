'''testcase 생성하기'''
import random

def create_input(min, max, N, overlap = True):
    if overlap == False:
        # ramdom한 정수를 중복되지 않게 sampling
        input_list = random.sample(range(min,max), N)
    else:
        # ramdom한 정수를 중복 허용
        input_list = [random.randint(min,max) for _ in range(N)]
        # random.suffle(_list) 데이터의 순서를 무작위로 만들어줌

    print(N);    print(input_list)

def get_input(min, max, N, overlap = True):
    if overlap == False:
        # ramdom한 정수를 중복되지 않게 sampling
        input_list = random.sample(range(min,max), N)
    else:
        # ramdom한 정수를 중복 허용
        input_list = [random.randint(min,max) for _ in range(N)]
        # random.suffle(_list) 데이터의 순서를 무작위로 만들어줌
    return input_list