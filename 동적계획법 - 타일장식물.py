'''
동적계획법: 불필요한 계산을 줄이고, 효율적으로 최적해를 찾기
프로그래머스 - [타일 장식물]
문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42840
'''
def solution(N):
    dp = []
    dp.append(1)
    dp.append(1)
    for i in range(80-1):
        dp.append(dp[i] + dp[i+1])
    return (dp[N-1]+dp[N-1]+dp[N-2])*2
