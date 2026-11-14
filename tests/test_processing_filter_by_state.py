from src.processing import filter_by_state

def test_filter_by_state(operations):
    expected = [
        {"id": 1, "state": "EXECUTED", "date": "2026-11-07"},
        {"id": 2, "state": "EXECUTED", "date": "2026-10-07"},
        {"id": 5, "state": "EXECUTED", "date": "2026-11-02"}
    ]
    actual = filter_by_state(operations, state_value="EXECUTED")
    assert actual == expected