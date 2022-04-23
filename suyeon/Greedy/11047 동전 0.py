import sys
sys.stdin = open("Greedy/input.txt",'r')
input = sys.stdin.readline

n, k = map(int, input().strip().split())
coins = []
for i in range(n):
    coins.append(int(input().strip()))

cnt = 0
for i in range(n-1, 0, -1):
    if coins[i]<=k:
        cnt += (k // coins[i])
        k %= coins[i]
if coins[0]<=k:
    cnt += (k // coins[0])
    k %= coins[0]

print(cnt)