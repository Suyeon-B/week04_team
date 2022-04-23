# 맞긴 했는데 최적화 필요
import sys
sys.stdin = open("Greedy/input.txt",'r')
input = sys.stdin.readline

expression = input()
sum_candidate = []

result = 0
# '-', '+' 혼합되어 있는 경우
# '-' 있으면 다음 '-' 나올 때 까지 무조건 괄호쳐서 더해서 뺌
if '-' in expression:
    temp = expression.split('-')
    for i in range(len(temp)):
        if len(temp[i].split('+'))>1: # +가 들어있으면
            sum_candidate += list(map(int, temp[i].split('+')))
            if i!=0:
                result -= sum(sum_candidate)
            else:
                result += sum(sum_candidate)
            sum_candidate = []
        else:
            if i != 0:
                result -= int(temp[i])
            else:
                result += int(temp[i])
    
    print(result)
else: # '+'만 있으면 그냥 더해서 출력
    result = list(map(int, expression.split('+')))
    print(sum(result))
    exit(0)
