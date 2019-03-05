'''
동적계획법: 불필요한 계산을 줄이고, 효율적으로 최적해를 찾기
프로그래머스 - [정수 삼각형]
'''
def solution(triangle):
    triangle.reverse()
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            triangle[i][j] = max(triangle[i][j] + triangle[i-1][j],triangle[i][j] + triangle[i-1][j+1])
    return triangle[-1][-1]
