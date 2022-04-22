num = int(input())

arr = [0] * 1000000
arr[0] = 0
arr[1] = 1
arr[2] = 2

n = 1
while n <= num :                             # 00, 1, 11 11도 1+1,

    arr[n+2] = arr[n]%15746 + arr[n+1]%15746
    n += 1

print(arr[num]%15746)

# arr[3] = 3
# arr[4] = 5
# arr[5] = 8

