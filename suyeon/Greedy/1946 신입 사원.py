# 시간 초과 코드
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
    sorted_by_inter = sorted(sorted_by_doc, key=lambda x: x[1])

    fail = 0
    for i in range(n):
        competitors_doc = sorted_by_doc[:i]
        idx = sorted_by_inter.index(sorted_by_doc[i])
        competitors_inter = sorted_by_inter[:idx]
        for j in range(len(competitors_doc)):
            if competitors_doc[j] in competitors_inter:
                fail+=1
                break
            

    print(n-fail)
