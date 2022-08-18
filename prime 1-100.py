for n in range(1,101):
    for k in range(2,n):
        if(n%k==0):
            break
    else:
        print(n)