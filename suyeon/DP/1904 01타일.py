# 점화식이 피보나치 수열과 같았던 문제!
import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

n = int(input().strip())

F = [1, 2] + [0] * (n-2)
def get_fibonacci(n):
    if n == 1 or n == 2:
        print(F[n-1]%15746)
    else:
        for i in range(2, n):
            F[i] = (F[i-1]%15746 + F[i-2]%15746)%15746 # 모듈러의 성질
        print(F[n-1]%15746)

get_fibonacci(n)