def function(*args, **kwargs):
    suma = 0
    for a in args:
        if type(a) == int or type(a) == float:
            suma += a

    for a in kwargs.values():
        if type(a) == int or type(a) == float:
            suma += a

    return suma


def input_func():
    n = input("number: ")
    try:
        my_int = int(n)
        return my_int
    except ValueError:
        return 0


def sum_all(n):
    if n == 0:
        return 0
    return n + sum_all(n - 1)


def sum_odd(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return sum_odd(n - 1)
    return n + sum_odd(n - 1)


def sum_even(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + sum_even(n - 1)
    return sum_even(n - 1)


print(function(1, 5, -3, 'abc', [12, 56, 'cad']))
print(function())
print(function(2, 4, 'abc', param_1=1.2))
print(input_func())
print(input_func())

print(sum_all(10))
print(sum_odd(10))
print(sum_even(10))

