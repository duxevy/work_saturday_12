def even_digits_generator():
    for i in range(100):
        if i % 2 == 0:
            yield str(i)
        else:
            yield "Нечётное"

def even_digits_generator_1():
    return (str(i) if i % 3 == 0 else "Число" for i in range(100))

a = even_digits_generator_1()
for i in a:
    print(i)

# print(even_digits_generators_1())

# a = map(lambda x: x**2, (1, 2, 3, 4, 5))
# b = filter(lambda x: x < 3, (1, 2, 3, 4, 5))



# print(list(b))
# filter()