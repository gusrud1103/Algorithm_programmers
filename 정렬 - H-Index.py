'''
정렬
프로그래머스 - [H-Index]
문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42747
'''

def solution(citations):
    citations.sort()
    answer = 0
    for i in range(0,max(citations)):
        cnt=0
        for j in citations:
            if i <= j:
                cnt+=1

        if cnt >= i:
            answer = i
        else:
            return answer
