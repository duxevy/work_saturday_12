import pytest
from src.masks import get_mask_card_number, get_mask_account

@pytest.mark.parametrize("card_number, expected", [
    ("1234 6789 1353 9383", "1234 67** **** 9383"),
    ("0000 0000 0000 0000", "0000 00** **** 0000"),
    ("1234678913539383", "1234 67** **** 9383"),
    ("abcdelkajsdlkjsa", "abcd el** **** kjsa"),
    ("", " ** **** ")
])
def test_get_mask_card_number(card_number, expected):
    actual = get_mask_card_number(card_number)
    assert actual == expected

def test_get_mask_card_number_int():
    card_number = 1234
    with pytest.raises(AttributeError):
        get_mask_card_number(card_number)

def test_get_mask_account():
    account_number = "123467891353938332"
    actual = get_mask_account(account_number)
    expected = "**8332"
    assert actual == expected