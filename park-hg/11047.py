import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
A = [int(sys.stdin.readline()) for _ in range(N)]
A.sort(reverse=True)

ans = 0
for a in A:
    ans += K//a
    K -= (K//a)*a
print(ans)