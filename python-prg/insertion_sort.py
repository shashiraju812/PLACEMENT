#insertion sort
l=list(map(int,input().split()))
for i in range(1,len(1)):
    circle=l[i]
    j=i-1
    while(j>=0 and l[j]<circle):
        l[j+1]=l[j]
        j=j-1
    l[j+1]=circle
print(l)
