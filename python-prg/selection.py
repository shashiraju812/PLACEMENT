l=list(map(int,input().split()))
for i in range(0,len(l)):
    min=i
    for j in range(i+1,len(l)):
        if(l[min]<l[j]):
            min=j
        l[i],l[min]=l[min],l[i]
print(l)
