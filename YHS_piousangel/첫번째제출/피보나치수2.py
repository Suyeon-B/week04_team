num = int(input())

arr = [0] * 92
arr[0] = 0
arr[1] = 1

n = 0
while True:
    if n == 90:
        break
    arr[n+2] = arr[n] + arr[n+1]
    n += 1

print(arr[num])