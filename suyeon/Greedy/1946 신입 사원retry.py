# 시간 초과 해결
# 서류는 이미 정렬순이니, 면접 점수가 기준값보다 작은 값만 골라 count 해주면 된다.
from sys import stdin
stdin = open("Greedy/input.txt",'r')
input = stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    applicants = []
    for i in range(n):
        applicants.append(tuple(map(int, input().strip().split())))

    # 서류 기준 sort
    sorted_by_doc = sorted(applicants, key=lambda x: x[0])

    cnt = 1
    now = sorted_by_doc[0][1]
    for i in range(1, n):
        if sorted_by_doc[i][1] < now:
            cnt+=1
            now = sorted_by_doc[i][1]

    print(cnt)
