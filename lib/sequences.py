#!/usr/bin/env python3

def print_fibonacci(length):
    fib = []
    f1 = 0
    f2 = 1
    count = 2
    #special case for start of the list
    if length > 0:
        fib.append(0)
    if length > 1:
        fib.append(1)

    while count < length:
        count += 1
        added = f1+f2
        fib.append(added)
        f1 = f2
        f2 = added

    print(fib)
