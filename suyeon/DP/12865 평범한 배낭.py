# 누적합을 구하지 못했던 아래 방법 -> DP로 개선
# 물품의 수 100개
# 최대 100*100 의 2차원 배열 생성 후,
# 가치의 합 <= k일 때의 가치의 합을 배열에 저장
# max값을 출력
import sys, collections
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

# 물품의 수 N(1 ≤ N ≤ 100), 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)
n, k = map(int, input().strip().split())

# 물품의 수와 가치 dictionary
weight_val = collections.defaultdict(int)
weights = [0]*(n+1)
for i in range(1, n+1):
    weight, value = map(int, input().strip().split())
    weights[i] = weight
    weight_val[weight] = value



sum_values = [[0]*(n+1) for _ in range(n+1)]
results = []
for i in range(n+1):
    for j in range(n+1):
        if i == 0 and j > 0:
            if weights[j] <= k:
                results.append(weight_val[weights[j]])
            sum_values[i][j] = weight_val[weights[j]]
        elif i<j:
            if weights[i] + weights[j] <= k:
                results.append(weight_val[weights[i]] + weight_val[weights[j]])
                sum_values[i][j] = weight_val[weights[i]] + weight_val[weights[j]]

print(max(results))

"""
4 7
6 13
4 8
3 6
5 12
"""
