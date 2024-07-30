def quick_sort(list1):
    if len(list1)==0:
        return list1
    pivot=list1[0]
    lesser=[i for i in list1[1:] if i<=pivot]
    gretor=[i for i in list1[1:] if i>pivot]
    return quick_sort(lesser)+[pivot]+quick_sort(gretor)
l=[5,4,3,2,1]
print(quick_sort(l))
    
