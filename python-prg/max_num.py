def largest_num(l):
    max=l[0]
    for i in range(1,len(l)):
        if(max<l[i]):
            max=l[i]
    print(max)



l=list(map(int, input().split()))
largest_num(l)
