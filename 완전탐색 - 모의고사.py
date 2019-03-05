'''
완전탐색: 가능한 모든 상황을 조사
프로그래머스 - [모의고사]
문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42840
'''
import math
def solution(answers):
    a = [1,2,3,4,5]*math.ceil(len(answers)/5)
    b = [2,1,2,3,2,4,2,5]*math.ceil(len(answers)/8)
    c = [3,3,1,1,2,2,4,4,5,5]*math.ceil(len(answers)/10)
    li = []
    li.append(len([0 for i, j in zip(a[:len(answers)],answers) if i == j]))
    li.append(len([0 for i, j in zip(b[:len(answers)],answers) if i == j]))
    li.append(len([0 for i, j in zip(c[:len(answers)],answers) if i == j]))
    return [i+1 for i, j in enumerate(li) if j == max(li)]
