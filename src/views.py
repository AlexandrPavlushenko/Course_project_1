# -*- coding: utf-8 -*-

import json

import pandas as pd

from src.logger import setting_logger

from src.utils import fetch_exchange_rates, fetch_stock_prices, read_xlsx_file, greeting, get_top_five_transactions, \
    filter_transactions_by_card, filter_transactions_by_date

logger = setting_logger("views")


def generator_json_data(df_transactions: pd.DataFrame, date_filter: str) -> str:
    """Функция формирует json ответ для главной страницы SkyBank"""
    logger.info("Функция начала свою работу.")
    greeting_ = greeting()
    filter_transactions_by_date_ = filter_transactions_by_date(df_transactions, date_filter)
    filter_transactions_by_card_ = filter_transactions_by_card(filter_transactions_by_date_)
    top_five_transactions = get_top_five_transactions(filter_transactions_by_date_)
    exchange_rates = fetch_exchange_rates()
    stock_prices = fetch_stock_prices()

    json_data = json.dumps(
        {"greeting": greeting_, "cards": filter_transactions_by_card_, "top_transactions": top_five_transactions,
         "currency_rates": exchange_rates, "stock_prices": stock_prices}, indent=4, ensure_ascii=False)
    logger.info("Функция успешно завершила свою работу.")
    return json_data


# path_to_file = "../data/operations.xlsx"
# df_transactions = read_xlsx_file(path_to_file)
# date_filter = "20.05.2018 14:30:00"
# print(generator_json_data(df_transactions, date_filter))


