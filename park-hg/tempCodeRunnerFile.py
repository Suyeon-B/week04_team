import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))[::-1]

plugged = []
ans = 0
while A:
    a = A.pop()
    if a in plugged:
        continue

    if len(plugged) < N:
        plugged.append(a)
        
    else:
        flag = True
        for b in A:
            if b in plugged:
                plugged.remove(b)
                plugged.append(a)
                ans += 1
                flag = False
                break
        if flag:
            plugged.pop()
            plugged.append(a)
            ans += 1
            

    print(A, a, plugged, ans)
print(A)  
print(ans)
