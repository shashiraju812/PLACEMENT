def cal(num):
    sum=0
    while(num!=0):
        r=num%10
        square=r*r
        sum+=square
        num=num//10
    print(sum)

num=int(input())
cal(num)
