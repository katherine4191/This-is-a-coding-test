'''testcase 생성하기'''
import random

def create_input(min, max, N):
    input_list = random.sample(range(min,max), N)
    print(N)
    print(input_list)