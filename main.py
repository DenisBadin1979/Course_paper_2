from src.utils import user_interaction

# hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies("Дрессировщик")


if __name__ == "__main__":
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    user_interaction(search_query)
