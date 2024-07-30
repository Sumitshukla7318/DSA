'''
l=[1,3,5,2,4]
print(l)
for i in range(len(l)):
    for j in range(i,len(l)):
        if l[i]>l[j]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)
            
'''
'''
l=[1,2,5,3,4]
print(l)
for i in range(len(l)):
    min=l[i]
    index=i
    for j in range(i,len(l)):
        if l[j]<min:
            min=l[j]
            index=j
    temp=l[i]
    l[i]=l[index]
    l[index]=temp

print(l)
'''    
            
