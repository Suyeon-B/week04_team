import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

arr = [[0] * (K+1) for _ in range(N+1)]

bag = [[0,0]]
for i in range(N):
    a, b = map(int, input().split())
    bag.append([a,b])

for i in range(1, len(arr)):          #개수
    for j in range(1, len(arr[0])):   #최대합

        weight = bag[i][0]
        value = bag[i][1]

        if j < weight :
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = max(arr[i-1][j- weight] + value, arr[i-1][j] + 0)

print(arr[N][K])