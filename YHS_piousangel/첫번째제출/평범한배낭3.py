import sys
sys.stdin = open('sample.txt')
input = sys.stdin.readline


N, target = map(int, input().split())


bucket_list = []
w_total = 0 #무게합
v_total = 0 #가치합
for i in range(N):
    A, B = map(int, input().split())  #A, B 는 물건의 무게, 가치

    bucket_list.append([A,B])
    w_total += A
    v_total += B
    
super_value = 1000001
print(w_total)
print(v_total)

# print(bucket_list[ : -1])

def check_bag(bucket_list, w_total, v_total, target, idx) :
    global super_value

    if w_total > target :
        return

    if w_total == target :
        super_value = max(super_value, v_total)
        return

    check_bag(bucket_list[:-idx], w_total - bucket_list[-idx][0], v_total - bucket_list[-idx][0], target, idx+1)

    
for i in range(N-1):
    check_bag(bucket_list, w_total, v_total, target, i+1)
    print(super_value)