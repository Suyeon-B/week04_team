import sys
sys.stdin = open('input.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    l = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    l.sort(key=lambda x: x[0])
    cnt = 0
    s = N+1
    for _, b in l:
        if b < s:
            cnt += 1
            s = b

    print(cnt)