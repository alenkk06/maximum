for n in range(1200000,10**8):
    x=str(n)
    if (n%273==0) and (x[0]=='1' and x[-7]=='2' and x[-4]=='3' and x[-3]=='6' and x[-1]=='1'):
        print(n,n/273)
