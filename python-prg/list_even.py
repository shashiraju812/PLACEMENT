def filter_even(l):
    result=[]
    for i in range(0,len(l)):
        if(l[i]%2==0):
            result.append(l[i])
    print(result)
l=list(map(int,input().split()))
filter_even(l)
