def fib(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = a+b, a


while True:
    max = int(input('Enter max fibonacci value: '))
    print(list(fib(max)))