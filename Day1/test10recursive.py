def sum_2_nums(a,b):
    restul = a + b
    return restul

def sum_n_nums(a,b,*args):
    print(*args)
    print(args)
    x=sum_2_nums(a,b)
    for i in  args:
        x+=i
    print(x)


sum_n_nums(1,2,3,4)