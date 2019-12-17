#从索引位置为1的位置开始，设置为缓存值，与左侧的所有数据进行比较
def insert_sort(list):
    list_len = len(list)
    for i in range(1,list_len):
        tempValue = list[i]
        position = i
        while position>0 and list[position-1]>tempValue:
            list[position] = list[position-1]
            position = position-1
        list[position] = tempValue
            

list = [2,4,1,6,8,3]
insert_sort(list)
print(list)
  



