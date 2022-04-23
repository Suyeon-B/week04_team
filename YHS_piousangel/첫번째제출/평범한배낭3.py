import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline


N, target = map(int, input().split())


bucket_list = []
w_total = 0 #무게합
v_total = 0 #가치합
for i in range(N):
    A, B = map(int, input().split())  #A, B 는 물건의 무게, 가치

    bucket_list.append([A,B])
    w_total += A
    v_total += B
    
super_value = 1000001
print(w_total)
print(v_total)



import sys

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))


#냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] #무게
        value = stuff[i][1]  #가치
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else:
            knapsack[i][j] = max(knapsack[i - 1][j - weight] + value, knapsack[i - 1][j] + 0)
            # A, B, C, D 배낭의 가치와 무게가 있을 때, 만약 D가 Sack안에 원래 있었는지 원래 없었는지로 구분해 들어간다
            # 원래 Sack 안에 있었다면 n-1할때, n무게를 빼주면서 가치를 더해주고 없었다면 그냥 n-1만 해주면 된다.
            #NS(n,w) = 최대치로max(NS(n-1, w-w[n])+val[n] , NS(n-1,w)+0)

print(knapsack[N][K])