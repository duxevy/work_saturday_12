def foobar(a: int, b: str) -> tuple[int, int]:
    """
    Мок функция, которая умножает a на 10 и прибавляет int(b)
    Args:
        a: любое число
        b: строка (числовая, но проверки нет)

    Returns:
        Кортеж чисел
    """
    x = a * 10 + int(b)
    return x, a
