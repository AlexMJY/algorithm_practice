n = int(input())
array = list(map(int, input().split()))
array.sort()
print(array[0], array[-1])
# print(min(array), max(array))