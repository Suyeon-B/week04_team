N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
# 곱셈의 최소 횟수 행렬
dp = [[0]*N for _ in range(N)]

for diagonal in range(1, N):  # dp[i][i]는 자기 자신의 행렬이기 때문에 값이 0
    for i in range(0, N-diagonal):  # 대각선의 우측 한 칸씩 이동
        j = i + diagonal  # 현재 대각선에서 몇 번째 원소인지
        # 차이가 1밖에 나지 않는 칸
        if diagonal == 1:
            dp[i][j] = matrix[i][0] * matrix[j][0] * matrix[j][1]
            continue

        dp[i][j] = float('inf')
        # 각 부분행렬의 곱셈 횟수 + 두 행렬의 곱셈 횟수
        for k in range(i, j):  # k값으로 최적분할 찾기
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + matrix[i][0] * matrix[k][1] * matrix[j][1])

print(dp[0][N-1])
# from sys import stdin
# stdin = open("DP/input.txt",'r')
# input = stdin.readline

# n = int(input().strip())
# matrix = []
# for i in range(n):
#     matrix.append(tuple(map(int, input().strip().split())))

# dp = [[float('inf')]*(n) for _ in range(n)]
# for i in range(n):
#     dp[i][i] = 0

# """
# 인덱스 순서는 행렬을 우상향으로 채워짐.
# 예를 들어 행렬이 4개 곱해질 때
# (0, 1) -> (1, 2) -> (2, 3) -> (0, 2) -> (1, 3) -> (0, 3)
# """
# for diag in range(n):
#     for i in range(n-diag):
#         j = i+diag
#         for k in range(i, j):
#             dp[i][j] = min(dp[i][j], matrix[i][0] * matrix[k+1][0] * matrix[j][1] + dp[i][k] + dp[k+1][j])

# print(dp[0][-1])
