# 每一次遍历，将未排序数据中的最小值放在正确的位置
def selection_sort(list):
    nonsort_minValue_index = 0
    list_len = len(list)

    for i in range(list_len):
        minValueIndex=i
        for j in range(i+1,list_len):
            if(list[minValueIndex]>list[j]):
                minValueIndex = j
        if(minValueIndex!=i):
            list[i],list[minValueIndex] = list[minValueIndex],list[i]


def findSmallValue(arr):
    minValue = arr[0]
    minIndex = 0
    for i in range(1,len(arr)):
        if minValue > arr[i]:
            minValue = arr[i]
            minIndex = i
    return minIndex

def selection_sorts(arr:[]):
    new_array = []
    for i in range(len(arr)):
        index = findSmallValue(arr)
        new_array.append(arr.pop(index))
    return new_array


list = [3,4,2,1,9,6,8,9,2,2]
selection_sort(list)
print(list)

list2 = [3,4,6,1,8,0,2,7]
array = selection_sorts(list2)
print(array)

