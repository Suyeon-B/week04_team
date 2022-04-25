import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

n, target = map(int, input().split())

coin_list = []
# dp = [0] * (target+1)
# dp[0] = 1
for i in range(n):
    coin_list.append(int(input()))

coin_list.sort(reverse = True)              # 큰 코인들이 작은 코인들의 배수이기 때문에 그리디 알고리즘을 적용할 수 있다.(무조건 큰것이 작은 걸로 나누어 떨어지기때문에 최소값을 구할 수 있는거죠)


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

