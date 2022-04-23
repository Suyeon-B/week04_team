import sys
from collections import deque
sys.stdin = open('input.txt')

N, M = map(int, sys.stdin.readline().split())
smalls = set(int(sys.stdin.readline()) for _ in range(M))


dx = [-1, 0, 1]
visited = [0]*(N+1)
for s in smalls:
    visited[s] = -1
que = deque([[1, 0, 0]])
visited[1] = 1
ans = -1
while que:
    print(que)
    v, x, cnt = que.popleft()
    if v == N:
        ans = cnt
        break
    for i in range(3):
        nx = x+dx[i]
        if 1 <= nx <= N-v and visited[v+nx]==0:
            que.append([v+nx, nx, cnt+1])
            visited[v+nx] = 1

print(ans)