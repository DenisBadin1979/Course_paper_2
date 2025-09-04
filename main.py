# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.job_search import HeadHunterAPI
from src.json_work import JsonFile
from src.utils import user_interaction
from src.work__vacantion import Work_vacantion

# hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
# hh_vacancies = hh_api.get_vacancies("Дрессировщик")



if __name__ == "__main__":
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    user_interaction(search_query)

