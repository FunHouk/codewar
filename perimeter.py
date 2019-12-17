def perimeter(n):
    #Fibonacci sequence
    a=[]
    a.append(1)
    a.append(1)
    for i in range(2,n+1):
        a.append(a[i-1]+a[i-2])
    #
    return int(4*sum(a))
