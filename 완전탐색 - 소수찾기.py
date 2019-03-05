'''
완전탐색: 가능한 모든 상황을 조사
프로그래머스 - [소수 찾기]
'''
from itertools import permutations
def is_prime_not_bad(n: int) -> bool:
    if n < 2:
        return False 
    if n is 2:
        return True
    if n % 2 is 0:
        return False
    l = round(n ** 0.5) + 1
    for i in range(3, l, 2):
        if n % i is 0:
            return False
    return True

def solution(numbers):
    lst = list(numbers)
    per = list(set([int(''.join(i)) for j in range(1,len(lst)+1) for i in permutations(lst, j)]))
    return len([i for i in per if is_prime_not_bad(i) == True])
