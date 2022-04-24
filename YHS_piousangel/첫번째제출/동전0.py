import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, target = map(int, input().split())

coin_list = []
# dp = [0] * (target+1)
# dp[0] = 1
for i in range(n):
    coin_list.append(int(input()))

coin_list.sort(reverse = True)


#항상 그 순간에 최선을 다하는 알고리즘

cnt = 0
for i in range(len(coin_list)):
    if target >= coin_list[i]:
        temp = target // coin_list[i]   #몫으로 
        target -= coin_list[i] * temp
        cnt += temp
        if target == 0 :
            break

print(cnt)

