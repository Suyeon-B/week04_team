from functools import lru_cache
import sys

sys.stdin = open('input.txt')

N = int(sys.stdin.readline())

def matmul(A, B):
    C = [[0]*2 for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += (A[i][k]*B[k][j])%15746

    return C

memo = {}
def rec(A, n):
    if n == 1:
        return A

    if n in memo:
        return memo[n]

    if n%2 == 0:
        memo[n] = matmul(rec(A, n//2), rec(A, n//2))
        return memo[n]

    if n%2 == 1:
        memo[n] = matmul(matmul(rec(A, n//2), rec(A, n//2)), A)
        return memo[n]


F = [[1, 1], [1, 0]]

F = rec(F, N)

print(F[0][0]%15746)