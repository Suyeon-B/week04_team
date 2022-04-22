import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline


N, total = map(int, input().split())


bucket_list = []

for i in range(N):
    A, B = map(int, input().split())  #A, B 는 물건의 무게, 가치

    bucket_list.append((A,B))

super_value = 1000001

def check_bag(bucket_list, total) :
    global super_value

    i_sum = 0   #물건무게 합
    t_sum = 0   #물건가치 합

    for t_list in bucket_list :
        i_sum += t_list[0]            #물건무게의 합
        t_sum += t_list[1]            #물건가치의 합

    if i_sum == total :
        super_value = max(super_value, t_sum)
    
    check_bag

check_bag(bucket_list, total)