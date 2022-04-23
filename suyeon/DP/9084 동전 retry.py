# 1차원 배열 사용 ver.
import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

# 테스트 케이스의 개수 T(1 ≤ T ≤ 10)
t = int(input().strip())
for i in range(t):
    # 동전의 가지 수 N(1 ≤ N ≤ 20)
    n = int(input().strip())
    coins = list(map(int, input().strip().split()))
    # N가지 동전으로 만들어야 할 금액 M(1 ≤ M ≤ 10000)
    m = int(input().strip())

    # 동전의 누적 가치를 담아줄 배열
    dp = [0] * (m+1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, m+1):
            dp[i] += dp[i - coin]
    
    print(dp[m])