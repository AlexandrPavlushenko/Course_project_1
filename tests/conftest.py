# -*- coding: utf-8 -*-

import pytest

import pandas as pd


@pytest.fixture
def sample_transactions():
    data = {
        "Номер карты": ["1234567812345678", "1234567812345678", "8765432187654321", "8765432187654321"],
        "Сумма платежа": [-1000, -2000, -1500, 3000],
    }
    return pd.DataFrame(data)
