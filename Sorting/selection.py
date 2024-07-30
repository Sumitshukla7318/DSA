def selection_sort(data_list):
    for i in range(len(data_list)):
        index=i
        for j in range(i+1,len(data_list)):
            if data_list[j]<data_list[index]:
                index=j
        data_list[i],data_list[index]=data_list[index],data_list[i]
    print(data_list)
x=[1,5,4,3,2,1]
selection_sort(x)
print(x)
