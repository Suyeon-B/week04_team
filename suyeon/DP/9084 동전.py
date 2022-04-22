import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

# 테스트 케이스의 개수 T(1 ≤ T ≤ 10)
t = int(input().strip())
# 동전의 가지 수 N(1 ≤ N ≤ 20)
n = int(input().strip())
coins = [0] + map(int, input().strip().split())
# N가지 동전으로 만들어야 할 금액 M(1 ≤ M ≤ 10000)
m = int(input().strip())

# 동전의 누적 가치를 담아줄 배열
value_sofar = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        # 물건의 무게와 가치 (w, v)
        v = coins[i]
        if j < m: # 현재 허용된 가치보다 넣으려는 동전의 가치가 더 크다면
           value_sofar[i][j] = value_sofar[i-1][j] # 넣지 않는다. (직전 무게와 동일)
        else: # 현재 허용된 가치 안에 드는 가치라면
            # 1. 현재 넣을 동전의 가치만큼 빼고, 동전을 넣는다
            # 2. 동전을 넣지 말고 이전 금액 그대로 가지고 간다.
            # 위 둘 중 가치가 큰걸 선택한다.
            value_sofar[i][j] = max(value_sofar[i-1][j-m]+v, value_sofar[i-1][j]) 

print(value_sofar[n][m])

"""
3 테스트 케이스의 개수 T(1 ≤ T ≤ 10)
2 동전의 가지 수 N(1 ≤ N ≤ 20)
1 2 동전의 가치
1000 만들어야 할 금액
3
1 5 10
100
2
5 7
22
"""