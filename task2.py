def gen_fib(n):

    l = [1, 1]
    i = 0

    while(i < n):
        if i not in (0, 1):
            new_element = l[i - 1] + l[i - 2]
            l.append(new_element)        
        yield l[i]
        i += 1


n = 10
fib = gen_fib(n)

for f in fib:
    print(f)
