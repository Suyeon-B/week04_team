import sys
sys.stdin = open('input.txt')

N = int(sys.stdin.readline())
l = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
l.sort(key=lambda x: (x[1], x[0]))

cnt = 0
e = 0
for i in range(N):
    start, end = l[i]
    if e <= start:
        cnt += 1
        e = end

print(cnt)
