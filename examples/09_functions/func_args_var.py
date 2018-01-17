def sum_arg(a, *args):
    print(a, args)
    return a + sum(args)


def sum_arg(*args):
    print(args)
    return sum(args)


def sum_arg(a, **kwargs):
    print(a, kwargs)
    return a + sum(kwargs.values())
