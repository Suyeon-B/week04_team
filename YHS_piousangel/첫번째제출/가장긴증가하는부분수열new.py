import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

n_list = list(map(int, input().split()))
arr = [1 for _ in range(n)]                #각 인덱스 일때 부분증가수열의 길이를 디폴트값으로 1으로 잡고


for i in range(len(n_list)):          # n_list 를 차례대로 돌면서
    for j in range(i):                # 기존 n_list[i] 와 0 ~ i-1 인덱스를 돌면서 
        if n_list[i] > n_list[j]:     # 전 인덱스중 하나 값보다 클 때 이 값보다 작은 모든 idx 에서 출발해서 완성되어있던 부분수열길이들을 경쟁시켜 최대 길이를 완성시킨다~
            arr[i] = max(arr[i], arr[j]+1)

print(arr)
print(max(arr))