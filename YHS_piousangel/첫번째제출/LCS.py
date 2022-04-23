import sys
from functools import lru_cache
sys.stdin = open('sample.txt')
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

str1_idx = len(str1)-1
str2_idx = len(str2)-1

cnt = 0

@lru_cache(None)
def chk_LCS(str1_idx, str2_idx):
    global cnt
    cnt += 1
    print(cnt, str1[:str1_idx+1], str2[:str2_idx+1])
    if str1_idx == 0 or str2_idx == 0:
        return 0

    if str1[str1_idx] == str2[str2_idx]:
        return max(chk_LCS(str1_idx-1, str2_idx), chk_LCS(str1_idx, str2_idx-1), chk_LCS(str1_idx-1, str2_idx-1) + 1)
    else :
        return max(chk_LCS(str1_idx-1, str2_idx), chk_LCS(str1_idx, str2_idx-1), chk_LCS(str1_idx-1, str2_idx-1))

print(chk_LCS(str1_idx, str2_idx))


# import sys
# sys.setrecursionlimit(10**7)
# sys.stdin = open('sample.txt')
# input = sys.stdin.readline

# str1 = input().rstrip()
# str2 = input().rstrip()

# def chk_LCS(str1, str2, total):

#     if len(str1) == 0 or len(str2) == 0:
#         return total

#     if str1[-1] == str2[-1]:
#         result = chk_LCS(str1[:-1], str2[:-1], total+1)
#     else :
#         result = max(chk_LCS(str1[:-1], str2, total), chk_LCS(str1, str2[:-1], total) )

#     return result

# answer = chk_LCS(str1, str2, 0)
# print(answer)