def fib(n):
    n1, n2 = 0, 1

    while(n2 < n):
        n1, n2 = n2, n1+n2
        yield n2


for i in fib(20):
    print(i)

