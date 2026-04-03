import copy

from src import app

ORIGINAL_ACTIVITIES = copy.deepcopy(app.activities)


def test_data(monkeypatch):
    """Reset the in-memory activities data before each test."""
    app.activities.clear()
    app.activities.update(copy.deepcopy(ORIGINAL_ACTIVITIES))
    yield
