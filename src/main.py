# -*- coding: utf-8 -*-

from typing import Any

from src.reports import spending_by_category
from src.services import transfers_to_individuals, transfers_to_phone
from src.utils import read_xlsx_file
from src.views import generator_json_data

sp = " " * 25
df_transactions = read_xlsx_file("../data/operations.xlsx")


def main() -> None:
    def action_1() -> None:
        print(generator_json_data(df_transactions, "31.12.2021 23:59:59"))
        return None

    def action_2() -> None:
        print(f"\n{sp}Выберите отчет :\n{sp}1. По переводам физ. лицам\n{sp}2. По переводам на мобильные номера")
        while True:
            user_input = input()
            if user_input == "1":
                print(transfers_to_individuals(df_transactions))
                break
            elif user_input == "2":
                print(transfers_to_phone(df_transactions))
                break
            else:
                continue

    def action_3() -> Any:
        while True:
            category = input("Введите категорию: ")
            if category in df_transactions["Категория"].values:
                data_dict = spending_by_category(df_transactions, category, "31.12.2021 23:59:59").to_dict("records")
                print(data_dict)
                break
            else:
                print("Категория отсутствует в списке")
                continue

    print("*" * 30 + " SKY BANK " + "*" * 30)
    print(" " * 9 + "Внимание!!! Для отчета используется дата: 31.12.2021")
    print(f"{sp}Выберите категорию:\n{sp}1. Главная страница\n{sp}2. Сервисы\n{sp}3. Отчеты")

    while True:
        user_input = input()
        if user_input == "1":
            action_1()
            break
        elif user_input == "2":
            action_2()
            break
        elif user_input == "3":
            action_3()
            break
        else:
            continue


if __name__ == "__main__":
    main()
