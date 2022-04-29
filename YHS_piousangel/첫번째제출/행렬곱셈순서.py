n = int(input())

n_list = []

for i in range(n):
    a, b = map(int, input())


import sys
input = sys.stdin.readline
n = int(input())
s = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * n for i in range(n)]
for i in range(1, n):   #   M1~M5 만약 6까지라고 하면 1,2,3,4,5
    for j in range(0, n - i):  # 0~4 , 0~3, 0~2 0~1., 0~0 열
        x = j + i  #전체 길이
        dp[j][x] = 2 ** 32  #최소구할꺼니까 일딴 엄청 크게 잡아놓고
        for k in range(j, x):   # 0부터 x-1까지 중 하나 잘라서 더하려고
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k + 1][x] + s[j][0] * s[k][1] * s[x][1])
print(dp[0][n - 1])

 
정답)
    A   B   C   D   E
A   0   105 240 567 364
B       0   189 528 294
C           0   297 252
D               0   198
E                   0
 

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
dp =[[0 for _ in range(N)] for _ in range(N)] 


for i in range(1, N): #몇 번째 대각선?
    for j in range(0, N-i): #대각선에서 몇 번째 열?
    
        if i == 1: #차이가 1밖에 나지 않는 칸
            dp[j][j+i] = matrix[j][0] * matrix[j][1] * matrix[j+i][1]
            continue
        
        dp[j][j+i] = 2**32 #최댓값을 미리 넣어줌
        for k in range(j, j+i): 
            dp[j][j+i] = min(dp[j][j+i], 
                             dp[j][k] + dp[k+1][j+i] + matrix[j][0] * matrix[k][1] * matrix[j+i][1])
                
    
print(dp[0][N-1]) #맨 오른쪽 위


import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
DP = [[0]*N for _ in range(N)]

# 분할된 그룹의 크기를 1부터 N-1까지 돎
for size in range(1, N):
    # 크기 size인 그룹의 모든 경우의 수 돎
    for start in range(N - size):
        end = start + size
        
        # 어떤 그룹의 최소 곱셈 횟수는 분할한 두 그룹의 최소 곱셈 횟수 + 각 그룹의 곱셈 다 끝나고 남은 행렬끼리의 곱셈 횟수
        result = float("inf")
        for cut in range(start, end):
            result = min(result, DP[start][cut] + DP[cut+1][end] +
                        matrix[start][0]*matrix[cut][1]*matrix[end][1])
        DP[start][end] = result

print(DP[0][-1])
