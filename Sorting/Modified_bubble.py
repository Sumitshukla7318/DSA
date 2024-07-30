import time
def bubble(data_list):
    for r in range(1,len(data_list)):
        flag=False
        for i in range(len(data_list)-r):
            if data_list[i]>data_list[i+1]:
                data_list[i],data_list[i+1]=data_list[i+1],data_list[i]
                flag=True
        if not flag:
            break
    return data_list

l=[3,2,1,4,5]
print(l)
print(time.time())
print(bubble(l))
print(time.time())
