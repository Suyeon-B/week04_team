import sys
sys.stdin = open('input.txt')

l = list(sys.stdin.readline().split('-'))

ans = sum(list(map(int, l[0].split('+'))))

for x in l[1:]:
    ans -= sum(list(map(int, x.split('+'))))

print(ans)