import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
stone_list = []

for _ in range(M):
    stone = int(input().rstrip())
    if stone not in stone_list:
        stone_list.append(stone)
        
arr = [[10001]* (int((2*N)**0.5)+2) for _ in range(N+1)] 

arr[1][0] = 0

for i in range(2, N+1):
    if i in stone_list:
        continue
    for k in range(1, int((2*i)**0.5)+1): # 1부터 갈수있는 최대 거리까지 다 돌면서 min값을 구해준다.
        arr[i][k] = min(arr[i-k][k-1], arr[i-k][k], arr[i-k][k+1]) + 1    #k-1, k, k+1 에 1을 더해야해(전에거에서 뛰어와야하잖아)

answer = min(arr[N])
if answer == 10001:
    print("-1")
else:
    print(answer)



