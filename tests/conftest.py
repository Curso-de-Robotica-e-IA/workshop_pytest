import pytest


@pytest.fixture
def patch_time_sleep(monkeypatch):
    monkeypatch.setattr("time.sleep", lambda x: None)
