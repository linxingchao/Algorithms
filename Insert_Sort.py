def insert_sort(list):
    list_len = len(list)
    for i in range(1,list_len):
        tempValue = list[i]
        j = i-1
        while j>=0:
            if(tempValue<list[j]):
                list[j+1]=list[j]
                list[j]=tempValue
            j=j-1

list = [2,4,1,6,8,4,3]
insert_sort(list)
for i in list:
    print(i)



