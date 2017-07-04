
def recur_sum_of_digits(args):
    print(args)
    if not args:
        return 0
    return args[0] + recur_sum_of_digits(args[1:])


recur_sum_of_digits([0,1,2,3])

