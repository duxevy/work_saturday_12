from src.generators import even_digits_generator, even_digits_generator_1

def test_even_digits_generator():
    gen = even_digits_generator()
    assert next(gen) == "0"
    assert next(gen) == "Нечётное"
    assert next(gen) == "2"
    assert next(gen) == "Нечётное"

def test_even_digits_generator_1():
    gen = even_digits_generator_1()
    assert next(gen) == "0"
    assert next(gen) == "Число"
    assert next(gen) == "Число"
    assert next(gen) == "3"