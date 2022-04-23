import sys
sys.stdin = open("DP/input.txt",'r')
input = sys.stdin.readline

X = input().strip()
Y = input().strip()


LCS = [[0]*(len(Y)+1) for _ in range(len(X)+1)]
for i in range(1, len(X)+1):
    for j in range(1, len(Y)+1):
        if X[i-1] == Y[j-1]: # if xi = xj
            LCS[i][j] = LCS[i-1][j-1]+1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1]) # if xi != xj

print(LCS[len(X)][len(Y)])