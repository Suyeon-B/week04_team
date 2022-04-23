import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

n = int(input().strip())
matrix = []
for i in range(n):
    matrix.append(tuple(map(int, input().strip().split())))

dp = [[1e9]*(n) for _ in range(n)]
for i in range(n):
    dp[i][i] = 0

"""
인덱스 순서는 행렬을 우상향으로 채워짐.
예를 들어 행렬이 4개 곱해질 때
(0, 1) -> (1, 2) -> (2, 3) -> (0, 2) -> (1, 3) -> (0, 3)
"""
for diag in range(n):
    for i in range(n-diag):
        j = i+diag
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], matrix[i][0] * matrix[k+1][0] * matrix[j][1] + dp[i][k] + dp[k+1][j])

        print(dp)
