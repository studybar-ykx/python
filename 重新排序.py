def partition(arr, left, right):
    key = 0
    while left < right:
        while left < right and arr[right] >= arr[key]:
            right -= 1
        while left < right and arr[left] <= arr[key]:
            left += 1
        (arr[left], arr[right]) = (arr[right], arr[left])
    (arr[left], arr[key]) = (arr[key], arr[left])
    return left
arr = [0,-8,2,-5,6,-9,1]
flag=0
for i in range(len(arr)):
    if arr[i]<0:
        flag+=1
partition(arr,0,len(arr)-1)
print("数列按序排列如下：")
del arr[flag]
print(arr)