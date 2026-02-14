l=list(map(int ,input.split()))
search=int(input())
flag=0
low=0
high=len(1)-1
while(low<=high):
    mid=(low+high)//2
    if(l[mid]==search):
        flag=1
        print("i found the element",mid,"index")
        break
    elif(search>l[mid]):
        low=mid+1
    elif(search<l[mid]):
        high=mid-1
if(flag==0):
    print("i cannot found")
    
