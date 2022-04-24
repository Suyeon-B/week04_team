import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

sdol_list = []
arr = [i for i in range(N+1)] #한칸뛰기로 갈수있음으로 갈수있는 경우의 수 0
jump_boundary = [i for i in range(1,N+1)] #점프 바운더리 (1~19) 최종적으로 19칸더뛸수있지않나?

print(arr)


# for i in range(M):
#     sdol_list.append(int(input()))

jump_idx = 1

for i in range(2, N):  #첫번째 칸부터 작은 경우의 수로 갱신해줘야 해요

    for j in (1, i+1):  # 점프 범위 

        arr[i] = min(jump_boundary[j]+j, jump_boundary[i])

print(arr)



import sys
N, M = map(int, sys.stdin.readline().split())
dp = [[float('inf')] * (int((2 * N)** 0.5) + 2) for _ in range(N + 1)] 
dp[1][0] = 0

stone_set = set()
for _ in range(M):
    stone_set.add(int(sys.stdin.readline()))
for i in range(2, N + 1):
    if i in stone_set:
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))


from sys import stdin

N, stone_n = map(int, stdin.readline().split())

stone = set()
for _ in range(stone_n):
    stone.add(int(stdin.readline().rstrip()))


int((2*N)^0.5)의 의미 
-> 불필요한 연산을 막기 위한 연산
등차수열의 합 공식 = k(2a+(k-1)d) / 2
(이 문제에서 a(첫 번째 수) =1, d(공차) =1 )
따라서 마지막에 있는 돌까지 가장 빠르게 갈 수 있는 돌들의 수의 합 N
= k(k+1)/2
k = (2N-k)^0.5 <= 2N^0.5

dp  = [[10001]* (int((2*N)**0.5)+2)  for _ in range(N+1)]

dp[1][0] = 0
for i in range(2, N+1):
    if i in stone:
        continue
    for v in range(1,int((2*i)**0.5)+1):
        dp[i][v] = min(dp[i-v][v-1],dp[i-v][v],dp[i-v][v+1]) +1


ans = min(dp[N])
if ans == 10001:
    print(-1)
else:
    print(ans)