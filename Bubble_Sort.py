def bubble_sort(list):
    if(len(list)<1):
        return;
    list_len = len(list)-1;
    isSorted = False;
    while not isSorted:
        for i in range(list_len):
            isSorted = True
            if(list[i]>=list[i+1]):
                isSorted = False
                list[i],list[i+1] = list[i+1],list[i];
        list_len = list_len-1


list = [7,3,7,4,8,2,9,3,7]
bubble_sort(list)
print(list);