

def multiply(a):
    def result(b):
        return a*b
    return result


by_10 = multiply(10)
print(by_10)
print(by_10(4))
print(by_10(5))

by_5 = multiply(5)
print(by_5)
print(by_5(100))
