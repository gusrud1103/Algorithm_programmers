'''
정렬
프로그래머스 - [K번째수]
문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42748
'''

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        tmp = array[commands[i][0]-1:commands[i][1]]
        tmp.sort()
        answer.append(tmp[(commands[i][2]-1)])
    return answer
