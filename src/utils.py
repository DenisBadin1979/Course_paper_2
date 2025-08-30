import json
from typing import Any


def user_interaction() -> Any:

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")
    file_name = input("Введите где находится список вакансий: ")

    with open(file_name, "r", encoding="utf-8") as file:
        vacancies_list = json.load(file)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    return top_vacancies


def filter_vacancies(vacancies_list: list, filter_words: list) -> list:
    """Функция фильтрации вакансий по ключевому слову в описании вакансии"""
    new_list = []
    for v in vacancies_list:
        description = v.get("description_vac", "").lower()
        # Проверяем, содержит ли описание хотя бы одно из ключевых слов
        if any(word.lower() in description for word in filter_words):
            new_list.append(v)
    return new_list


def sort_vacancies(vacancies: list) -> list:
    """Функция сортировки вакансий по заработной плате"""
    return sorted(vacancies, key=lambda x: x.get("pay_vac"))


def get_top_vacancies(vacancies: list, top_n: int) -> list:
    """Функция отбора вакансий в количестве"""
    return vacancies[:top_n]


def get_vacancies_by_salary(vacancies: list, salary_range: str) -> list:
    """Функция получает вакансии в пределах указанного диапазона зарплат"""
    new_list = []
    try:
        split_str = salary_range.split("-")
        min_salary = int(split_str[0].strip())
        max_salary = int(split_str[-1].strip()) if len(split_str) > 1 else min_salary

        for v in vacancies:
            pay = v.get("pay_vac", 0)
            if min_salary <= pay <= max_salary:
                new_list.append(v)
    except (ValueError, IndexError):
        raise ValueError("Некорректный формат диапазона зарплат")

    return new_list
