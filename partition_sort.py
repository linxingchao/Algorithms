
class SortArray(object):

    def __init__(self, array):
        self.array = array

    #O(NlogN)
    def quickSort(self,leftIndex,rightIndex):
        if(len(self.array)<1 or (leftIndex>=rightIndex)):
            return;
        pivot_postition = self.partion(leftIndex,rightIndex)
        self.quickSort(leftIndex,pivot_postition-1)
        self.quickSort(pivot_postition+1,rightIndex)

    #将数组最后一个元素作为轴元素
    def partion(self,leftIndex,rightIndex):
        #以数组最后一个元素作为州
        povit_position = rightIndex
        #轴数据
        povit_value = self.array[povit_position]

        rightIndex -= 1

        while True:
            #如果左侧数据小于或等于轴数据，跳到下一个索引
            while(self.array[leftIndex]<povit_value):
                leftIndex+=1
            #如果右侧数据大于轴数据，跳到前一个索引
            while(self.array[rightIndex]>povit_value):
                rightIndex-=1
            #如果左侧索引大于或等于右侧索引，终止
            if (leftIndex>=rightIndex):
                break;
            else:
                #如果左侧大于轴数据，右侧小于轴数据，交换两侧的数据
                self.array[leftIndex],self.array[rightIndex] = self.array[rightIndex],self.array[leftIndex]
        #将左侧值和轴值交换
        self.array[leftIndex],self.array[povit_position] = self.array[povit_position],self.array[leftIndex]

        return leftIndex
    def quickSelect(self,kth_low_value,leftindex,rightIndex):
        if(len(self.array)<1 or (leftindex>=rightIndex)):
            return
        povit_index = self.partion(leftindex,rightIndex)
        if(povit_index>kth_low_value):
            self.quickSelect(kth_low_value,leftindex,povit_index-1)
        elif(povit_index<kth_low_value):
            self.quickSelect(kth_low_value,povit_index+1,rightIndex)
        elif(povit_index == kth_low_value):
            return self.array[povit_index]

list2 = [0, 50, 20, 10, 60, 30]
array1 = SortArray(list2)
value = array1.quickSelect(1,0,len(array1)-1)
print(value)

<<<<<<< HEAD
def quicksort2(array):
    if(len(array)<2):
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i<=pivot]
        greater = [i for i in  array[1:] if i>pivot]

        return quicksort2(less) + [pivot] + quicksort2(greater)


list = [0,5,2,1,6,3]
length = len(list)
array = SortArray(list)
array.quickSort(0,length-1)
print(array.array)
print(list)
=======
                


            
>>>>>>> 5ad5da7461620947c193ed64844a814554e67f0e
