def largest_num(l):
    max=l[0]
    for i in range(1,len(l)):
        if(max>l[i]):
            max=l[i]
        print(max)
l=list(map(int, input().split()))
largest_num(l)
#with min()
def largest_num(l):
    min=l[0]
    for i in range(1,len(l)):
        if(min>l[i]):
            min=l[i]
        print(min)

l=list(map(int, input().split()))
largest_num(l)
