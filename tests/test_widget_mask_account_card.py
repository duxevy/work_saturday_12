import pytest
from src.widget import mask_account_card

@pytest.mark.parametrize("data, expected", [
    ("Счет 123467891353938332", "Счет **8332"),
    ("Visa 1234678913539383", "Visa 1234 67** **** 9383"),
    ("Visa Classic 1234678913539383", "Visa Classic 1234 67** **** 9383"),
    ("Mastercard 1234678913539383", "Mastercard 1234 67** **** 9383"),
    ("МИР 1234678913539383", "МИР 1234 67** **** 9383"),
    # ("", " ")
    ("Счёт 123467891353938332", "Счёт 1234 67** **** 8332"),
])
def test_mask_account_card(data, expected):
    actual = mask_account_card(data)
    assert actual == expected