# DP로 풀어본 LIS
# 기준 값을 변경하며 최소한만 확인한다.
import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

def LIS():
    n = int(input().strip())
    A = list(map(int, input().strip().split()))

    dp = [1] * (n+1)
    for i in range(1, n):
        for j in range(0, i): 
            if A[i] > A[j]: # A[i] > A[j] 일 때 앞쪽만 확인해서 LIS를 갱신한다.
                dp[i] = max(dp[i], dp[j]+1)
    
    print(max(dp))

LIS()