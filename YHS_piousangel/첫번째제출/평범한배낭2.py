import sys
from collections import deque
sys.stdin = open('sample.txt')
input = sys.stdin.readline


N, total = map(int, input().split())

visited = [0]* 10001

bucket_list = []

for i in range(N):
    a, b = map(int, input().split())

    bucket_list.append([a,b])


def bfs(bucket_list, total, visited) :
    global answer
    q = deque()

    for i in range(len(bucket_list)):
        if bucket_list[i] <= total :
            visited[total - bucket_list[i][0]] = True
            q.append()


    while q :

answer = 0
bfs(n_list, total, visited)