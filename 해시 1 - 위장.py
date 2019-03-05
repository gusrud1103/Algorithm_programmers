'''
해시 :  Key-value쌍으로 데이터를 저장하는 자료구조
프로그래머스 - [위장]
'''

from collections import Counter
from functools import reduce

def solution(clothes):
    kind_lst = [clothes[i][1] for i in range(len(clothes))]
    cnt_lst = list(Counter(kind_lst).values())
    # 부분집합
    cnt_lst = [a+1 for a in cnt_lst] # 공집합 때문에 +1 해줌
    cnt_lst = reduce(lambda x, y: x*y, cnt_lst) -1
    return cnt_lst
