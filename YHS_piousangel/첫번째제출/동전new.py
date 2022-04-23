import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n = int(input())

for i in range(n):

    num = int(input())   #코인 개수
    coin_list = list(map(int, input().split()))  #코인 리스트
    total = int(input())   #총합

    dp = [0] * (total+1)
    dp[0] = 1


    for coin in coin_list :
        for i in range(total+1):
            if i >= coin :
                dp[i] += dp[i-coin]     #경우의 수를 더해주는 느낌

    print(dp[total])