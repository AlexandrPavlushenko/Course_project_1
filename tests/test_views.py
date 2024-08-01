from src.views import get_greeting

from freezegun import freeze_time


@freeze_time("2024-08-02 06:00:00")
def test_get_greeting():
    assert get_greeting() == "Доброе утро"
