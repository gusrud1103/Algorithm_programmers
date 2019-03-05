'''
탐욕법: 부분적인 최적해가 전체적인 최적해가 되는 마법!
프로그래머스 - [조이스틱]
문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42860
'''
def solution(name):
    alpha = list('abcdefghijklmnopqrstuvwxyz'.upper())
    dic = {i: j for i ,j in zip(alpha,[ord(i)-65 if ord(i)-65 <=13 else 91 - ord(i) for i in alpha])}
    name = list(name)
    answer1 = 0
    answer2 = 0
    cnt = 1
    if name[0]=='A':
        for i in range(len(name)):
            if name[i] != 'A':
                break
            cnt +=1

        answer1 = cnt
        answer2 = cnt
        name = name[i:]
    print(name)
    for i in range(len(name)):
        if all(b == 'A' for b in name[i:]):
            break

        if i == 0:
            answer1+=dic[name[i]]
        else:
            answer1+=(1+dic[name[i]])

    name2 = [name[0]]
    name2.extend([name[i] for i in range(len(name)-1,0,-1)])
    for i in range(len(name2)):
        if all(b == 'A' for b in name2[i:]):
            break
        if i == 0:
            answer2+=dic[name2[i]]
        else:
            answer2+=(1+dic[name2[i]])

    return(min(answer1,answer2))
