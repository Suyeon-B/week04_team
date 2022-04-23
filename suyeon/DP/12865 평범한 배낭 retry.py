# Backtracking으로도 풀어보기
import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

# 물품의 수 N(1 ≤ N ≤ 100), 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)
n, k = map(int, input().strip().split())

# 물건의 무게와 가치를 담아둘 배열
juniggeo = [(0, 0)]
for i in range(n):
    w, v = map(int, input().strip().split())
    juniggeo.append((w, v))

# 물건의 누적 가치를 담아줄 배열
value_sofar = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        # 물건의 무게와 가치 (w, v)
        w, v = juniggeo[i][0], juniggeo[i][1]
        if j < w: # 현재 허용된 무게보다 넣으려는 물건의 무게가 더 무겁다면
           value_sofar[i][j] = value_sofar[i-1][j] # 넣지 않는다. (직전 무게와 동일)
        else: # 현재 허용된 무게 안에 드는 무게라면
            # 1. 현재 넣을 물건 무게만큼 배낭에서 빼고, 현재 물건을 넣는다.
            # 2. 현재 물건을 넣지 말고 이전 배낭 그대로 가지고 간다.
            # 위 둘 중 가치가 큰걸 선택한다.
            value_sofar[i][j] = max(value_sofar[i-1][j-w]+v, value_sofar[i-1][j]) 

print(value_sofar[n][k])


"""
4 7
6 13
4 8
3 6
5 12
"""