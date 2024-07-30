def insertion_sort(data_list):
    for i in range(1,len(data_list)):
        temp=data_list[i]
        j=i-1
        while j>=0 and temp < data_list[j]:
            data_list[j+1]=data_list[j]
            j-=1
        data_list[j+1]=temp

l=[5,4,3,2,1]
insertion_sort(l)
print(l)
        
