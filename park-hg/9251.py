import sys
sys.stdin = open('input.txt')

A = sys.stdin.readline().rstrip()
B = sys.stdin.readline().rstrip()

dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]

for i in range(len(A)):
    for j in range(len(B)):
        dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j] + (A[i] == B[j]))

print(dp[-1][-1])
