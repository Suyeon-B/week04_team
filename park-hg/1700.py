import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

plugged = []
ans = 0
while A:
    a = A.pop(0)
    if a in plugged:
        continue

    if len(plugged) < N:
        plugged.append(a)
        
    else:
        max_index = -1
        max_p = 0
        flag = True
        for p in plugged:
            if p not in A:
                plugged.remove(p)
                plugged.append(a)
                ans += 1
                flag = False
                break
            else:
                cur_index = A.index(p)
                if cur_index > max_index:
                    max_index = cur_index
                    max_p = p

        if flag:
            plugged.remove(max_p)
            plugged.append(a)
            ans += 1


        

    print(A, a, plugged, ans)
print(A)  
print(ans)
