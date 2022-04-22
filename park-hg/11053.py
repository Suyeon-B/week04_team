import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1]*N
for i in range(N-1):
    for j in range(i+1):
        if A[j] < A[i+1]:
            dp[i+1] = max(dp[i+1], dp[j]+1)

print(max(dp))