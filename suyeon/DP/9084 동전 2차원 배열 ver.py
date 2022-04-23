import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

# 테스트 케이스의 개수 T(1 ≤ T ≤ 10)
t = int(input().strip())

def get_num_coins():
    # 동전의 가지 수 N(1 ≤ N ≤ 20)
    n = int(input().strip())
    coins = list(map(int, input().split()))
    # N가지 동전으로 만들어야 할 금액 M(1 ≤ M ≤ 10000)
    m = int(input().strip())

    # 동전의 누적 가치를 담아줄 배열
    dp = [[0]*(m+1) for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(m+1):
            if i==0: # 참조할 테이블이 없을 때
                dp[i][j] += dp[i][j-coins[i]]
            elif j<coins[i]: # 동전 크기가 기준 가치보다 클 때는 넣지 않는다.
                dp[i][j] = dp[i-1][j]
            else: # 참조할 테이블이 있고, 동전이 기준 가치보다 작거나 같을 때
                if dp[i][j-coins[i]] == dp[i-1][j-coins[i]]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-coins[i]]
                else: 
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]

    print(dp[n-1][m])

def main():
    for i in range(t):
        get_num_coins()

main()