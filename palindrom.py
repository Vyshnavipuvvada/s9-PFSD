i=1
for i in range(200):
    n=i
    sum=0
    while(i>0):
        r=i%10
        sum=sum*10+r
        i=i//10
    if(n==sum):
        print(sum)
