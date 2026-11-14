import pytest

@pytest.fixture()
def operations():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2026-11-07"},
        {"id": 2, "state": "EXECUTED", "date": "2026-10-07"},
        {"id": 3, "state": "CANCELLED", "date": "2026-09-07"},
        {"id": 4, "state": "PENDING", "date": "2026-11-01"},
        {"id": 5, "state": "EXECUTED", "date": "2026-11-02"}
    ]