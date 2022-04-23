import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

n = int(input().strip())
F = [0, 1] + [0] * (n-1)
def get_fibonacci(n):
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    print(F[n])

get_fibonacci(n)