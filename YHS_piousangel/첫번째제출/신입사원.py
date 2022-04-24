import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    answer = 1
    num = int(input())  # 지원자수
    seoru_rank = 0
    interview_rank = 0

    for i in range(num):

        seoru, interview = map(int, input().split())
        print(seoru, interview)
        print(seoru_rank, interview_rank)
        if i == 0:
            seoru_rank = seoru
            interview_rank = interview
            continue
            
        if seoru_rank > seoru or interview_rank > interview :  #둘중 하나라도 작으면
            answer +=1
            
        if seoru_rank < seoru :
            seoru_rank = seoru
        if interview_rank < interview :
            interview_rank = interview
         
    print(answer)
