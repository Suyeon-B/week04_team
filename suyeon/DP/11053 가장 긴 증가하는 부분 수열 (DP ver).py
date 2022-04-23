# DP ver
# 이 방법은 기준 값이 바뀌면 안 될 때의 case를 고려하지 못함
# 결국 O(n^2)번 돌아서 확인하는 코드로 retry함
import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

def LIS():
    n = int(input().strip())
    A = list(map(int, input().strip().split()))

    now = A[-1]
    dp = [0] * (n-1) + [1]
    for i in range(n-2, 0, -1):
        if A[i] < now:
            dp[i] = dp[i+1] + 1
        else:
            dp[i] = dp[i+1]
        now = A[i]
    if A[0] < now:
        dp[0] = dp[1] + 1
    else:
        dp[0] = dp[1]

    print(dp[0])

LIS()