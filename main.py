def sum(a: int, b: int) -> int:
    return a + b


sum2 = lambda a, b: a + b

names = ["ala", "kasia", "kris", "tom"]

names_modified = map(
    lambda name: f'Lady {name}' if name[-1] == 'a' else f'Sir {name}', names)

print(list(names_modified))

male_names = filter(lambda name: name[-1] != "a", names)

print(list(male_names))

some_integers = [1, 2, 3, 4, 5, 6, 100, 102, 999, 203, 2020, 2021, 2022]
even_more_integers = [234, -34, 234, 121, 33, 6754]

odd_integers = filter(lambda number: number % 2 != 0, some_integers)

print(list(odd_integers))


def greet_user(greeter_function, name):
    return greeter_function(name)


print(greet_user(lambda name: f'Hello {name}', 'kris'))


def double(values):
    return map(lambda number: number * 2, values)


print(list(double(some_integers)))
print(list(double(even_more_integers)))


def factorial(value: int) -> int:
    if value == 0:
        return 1
    else:
        return value * factorial(value - 1)


print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(6))
print(factorial(7))
print(factorial(8))
print(factorial(9))
print(factorial(10))


def recursive_loop(n, limit):
    print(n)

    if n == limit:
        return n

    else:
        return recursive_loop(n + 1, limit)


recursive_loop(0, 10)
