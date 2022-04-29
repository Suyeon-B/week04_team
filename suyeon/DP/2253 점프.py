# 반례 존재
import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

n, m = map(int, input().strip().split())
s_rocks = [int(input().strip()) for _ in range(m)]
# s_rocks = map(int, input().strip().split()) TC 돌리기용
# dp[i] = i번째 돌에서 할 수 있는 점프 시작 숫자
dp = [0] * n

# 만약 idx = 1에 돌이 있으면 -1 출력
if 1 in s_rocks:
    print(-1)
    exit(0)

now = jump = cnt = 0
while now < n:
    jump += 1
    now += jump
    if now-1 < n:
        dp[now] = jump
        cnt += 1
    else:
        break

    while True:
        if jump == 0: # 점프 수를 다 줄여도 작은 돌이면 점프 불가능
            print(-1)
            exit(0)
        if now-1 in s_rocks: # 도착한 지점이 작은 돌이면
            # dp, cnt깂을 초기화해주고
            dp[now] = 0
            cnt -= 1
            # 작은 돌 위가 아닐 때 까지 점프 수를 줄여본다.
            now -= 1 
            jump -= 1
            dp[now] = jump
            cnt+=1
        else: # 도착한 지점이 큰 돌일 때
            break 
print(cnt+1)