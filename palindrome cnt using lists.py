def palindrome(n,data):

    def digits(i):
        d=0
        while i:
            r=i%10
            i=i//10
            d=d*10+r
        return d
    c=0          
    for i in data:
        if i==digits(i):
            c+=1
    return c
n=int(input())
data=list(map(int,input().split()))
r=palindrome(n,data)
print(r)


