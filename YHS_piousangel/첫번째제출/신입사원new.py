import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    answer = 1
    num = int(input())  # 지원자수

    temp_rank = []
    

    for i in range(num):

        seoru, interview = map(int, input().split())
        temp_rank.append([seoru,interview])

    temp_rank.sort(key = lambda x : (x[0]))       # 걍 하나라도 작은걸로 정렬하고
    seoru_rank = num
    interview_rank = num
    # print(temp_rank)
    cnt = 0

    for i in range(len(temp_rank)):
        # print(seoru_rank, interview_rank)

        if temp_rank[i][0] < seoru_rank or temp_rank[i][1] < interview_rank :           # 다 되는 걸로 최신화 시켰으니 둘중 하나라도 작으면 랭크 최신화
            seoru_rank = temp_rank[i][0]
            interview_rank = temp_rank[i][1]
            cnt += 1
            continue
        
        # flag = False
        for j in range(0, len(temp_rank)):
            if temp_rank[i][0] > seoru_rank and temp_rank[i][1] > interview_rank :     # 이중에 없다? 그럼 전체 돌면서 확인
                # flag = True
                break
        else:
            seoru_rank = temp_rank[i][0]
            interview_rank = temp_rank[i][1]
            cnt += 1
    print(cnt)

  


    # print(answer)
