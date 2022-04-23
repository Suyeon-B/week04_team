import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    coins = [0] +list(map(int, sys.stdin.readline().split()))
    target = int(sys.stdin.readline())
    
    dp = [[0]*(target+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(target+1):
            k = j
            while k >= 0:
                dp[i+1][j] += dp[i][k]
                k -= coins[i+1]
            
    print(dp[-1][-1])
