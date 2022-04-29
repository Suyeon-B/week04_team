from sys import stdin
stdin = open("Greedy/input.txt",'r')
input = stdin.readline

n = int(input().strip())
lectures = []
for i in range(n):
    lectures.append(tuple(map(int, input().strip().split())))

sorted_by_start = sorted(lectures, key=lambda x: x[0]) # 이 부분도 필요함. (5, 5) -> (5, 6) -> (6, 6) 같은 경우도 있을 수 있음
sorted_by_end = sorted(sorted_by_start, key=lambda x: x[1])


cnt = 1
now = sorted_by_end[0][1]
for i in range(1, n):
    if now <= sorted_by_end[i][0]:
        cnt+=1
        now = sorted_by_end[i][1]
print(cnt)