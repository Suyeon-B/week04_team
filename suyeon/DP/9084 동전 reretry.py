# 1차원 배열 사용 ver.
import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

# 테스트 케이스의 개수 T(1 ≤ T ≤ 10)
t = int(input().strip())

def get_num_coins():
    # 동전의 가지 수 N(1 ≤ N ≤ 20)
    n = int(input().strip())
    coins = list(map(int, input().strip().split()))

    # 만들어야 할 금액 M(1 ≤ M ≤ 10000)
    m = int(input().strip())

    # dp table
    dp = [0 for _ in range(m+1)]
    dp[0] = 1

    for coin in coins:
        for j in range(coin, m+1): 
            # 동전의 가치보다 기준 가치가 작다면 동전을 넣을지 말지 고민할 필요도 없으므로,
            # 동전의 크기부터 시작해서 채워준다.
            dp[j] += dp[j-coin] # dp[j] = j원을 만들기 위해 필요한 동전의 수

    print(dp[m])

def main():
    for i in range(t):
        get_num_coins()

main()