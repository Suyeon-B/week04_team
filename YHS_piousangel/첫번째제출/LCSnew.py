import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline

str1 = input().rstrip()     #첫번째 문자열
str2 = input().rstrip()     #두번째 문자열

# 지금 돌리고 있는 문자열이 같으면 cnt 올려주고
# 

dp = [ [0] * (len(str2)+1) for _ in range( (len(str1)+1) )]

# for d in dp:
#     print(d)
# print("====")
for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1              # 대각 +1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])   # max(왼쪽, 위쪽)

# for d in dp:
#     print(d)
print(dp[-1][-1])

