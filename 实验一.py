import time
import numpy
def insertion_sort(arr):
    #插入排序
    # 第一层for表示循环插入的遍数
    for i in range(1, len(arr)):
        # 设置当前需要插入的元素
        current = arr[i]
        # 与当前元素比较的比较元素
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            # 当比较元素大于当前元素则把比较元素后移
            temp=arr[pre_index]
            arr[pre_index + 1] = temp
            # 往前选择下一个比较元素
            pre_index -= 1
        # 当比较元素小于当前元素，则将当前元素插入在 其后面
        arr[pre_index + 1] = current
    return arr
def quicksort(arr):
  if len(arr) < 2:
    # 基线条件：为空或只包含一个元素的数组是“有序”的
    return arr
  else:
    # 递归条件
    pivot = arr[0]
    # 由所有小于基准值的元素组成的子数组
    less = [i for i in arr[1:] if i <= pivot]
    # 由所有大于基准值的元素组成的子数组
    greater = [i for i in arr[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)
def bubble_sort(arr):
    #冒泡排序
    # 第一层for表示循环的遍数
    for i in range(len(arr) - 1):
        # 第二层for表示具体比较哪两个元素
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                # 如果前面的大于后面的，则交换这两个元素的位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
arr1=input('请输入：')
arr1 = [int(c) for c in arr1]
start = time.clock()
print(insertion_sort(arr1))
end1 = time.clock()
print('插入排序时间为%s毫秒'%(end1-start))
print(quicksort(arr1))
end2 = time.clock()
print('快速排序时间为%s毫秒'%(end2-end1))
print(bubble_sort(arr1))
end3 = time.clock()
print('冒泡排序时间为%s毫秒'%(end3-end2))