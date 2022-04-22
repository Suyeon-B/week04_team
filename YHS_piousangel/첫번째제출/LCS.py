import sys
sys.setrecursionlimit(10**7)
sys.stdin = open('sample.txt')
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

# print(str1[:-1])
# print(str2[:-1])
# char_box = [0] * 100

def chk_LCS(str1, str2, total):

    if len(str1) == 0 or len(str2) == 0:
        return total

    if str1[-1] == str2[-1]:
        result = chk_LCS(str1[:-1], str2[:-1], total+1)
    else :
        result = max(chk_LCS(str1[:-1], str2, total), chk_LCS(str1, str2[:-1], total) )

    return result

answer = chk_LCS(str1, str2, 0)
print(answer)

