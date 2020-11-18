def insertion_sort2(arr):
    for i in range(1, len(arr)):
        tem = arr[i]
        left = 0
        right = i - 1
        count = 0
        while left <= right:
            count += 1
            mid = (left + right) // 2
            if arr[i] < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i - 1, left - 1, -1):
            arr[j + 1] = arr[j]
        # 插入元素
        if left != i:
            arr[left] = tem
            print(arr)
    return arr

arr = input('请输入：')
arr = [int(c) for c in arr]
insertion_sort2(arr)