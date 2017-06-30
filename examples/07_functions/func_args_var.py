def sum_arg(a, *args):
    print a, arg
    return a + sum(args)

def sum_arg(*args):
    print arg
    return sum(arg)

def sum_arg(a,**kwargs):
    print a, kwargs
    return a + sum(kwargs.values())


