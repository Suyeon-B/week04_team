# 이분탐색
import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

def find_idx(list, k):
    l, r = 0, len(list)-1
    while l<r:
        m = l+(r-l)//2
        if list[m] < k:
            l = m+1
        else:
            r = m
    return l

def LIS():
    n = int(input().strip())
    A = list(map(int, input().strip().split()))
    cnt = 0

    lis = [A[0]] + [1e9]*(n-1)

    for i in range(1, n):
        idx = find_idx(lis, A[i])
        lis[idx] = A[i]
    
    for i in range(n):
        if lis[i] != 1e9:
            cnt+=1
    
    print(cnt)

LIS()