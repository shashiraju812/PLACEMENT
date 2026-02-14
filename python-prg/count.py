def count_vowels(s):
    count=0
    for i in s:
        if( i in"aeiouAEIOU"):
            count+=1
        print(count)
s=input()
count_vowels(s)
