import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

def dp1(total):                                # dp[1] = 1, dp[2] = 2, dp[3] = 2, dp[4] = 3, dp[5] = 3, dp[6] = 4 
    if idx == 0:
        return total//2 + 1                         # 짝수개 마다 1씩 증가하네요 n//2 +1

def dp2():


for i in range(n):
    num = int(input())

    n_list = list(map(int, input().split()))
    total = int(input())
    dp1(total)

    import sys


input = sys.stdin.readline

t = int(input())
for _ in range(t):                            #문제에서 주어진 횟수만큼 돌면서 
    n = int(input())                          #동전 개수
    coins = list(map(int, input().split()))   #코인 리스트
    m = int(input())                          # 총 합

    # memoization을 위한 리스트 선언
    d = [0] * (m + 1)                         # 0 ~ 총합 리스트 만들기
    d[0] = 1                                  # 0은 0이니까 한가지


    for coin in coins:
        for i in range(m + 1):
            # a_(i-k) 를 만드는 방법이 존재한다면 
            # 이전 경우의 수에 현재 동전으로 만들 수 있는 경우의 수를 더한다.
    
            if i >= coin:                  # 당연히 코인보다 i가 클 때로 걸어야죠
                d[i] += d[i - coin]




    print(d[m])