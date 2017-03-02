def fib(n):
    a,b=1,1
    fs=[]
    for i in range(n-1):
        a,b=b,a+b
        fs.append(a)
    return fs

s=fib(50)
print s
