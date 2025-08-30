# Создание экземпляра класса для работы с API сайтов с вакансиями
from src.job_search import HeadHunterAPI
from src.json_work import Json_file
from src.utils import user_interaction
from src.work__vacantion import Work_vacantion

hh_api = HeadHunterAPI()

# Получение вакансий с hh.ru в формате JSON
hh_vacancies = hh_api.get_vacancies("Python")

# Пример работы контструктора класса с одной вакансией
vacancy = Work_vacantion(
    "Разработчик",
    50000,
    "Описание вакансии например разработка",
    "Требования: можно без опыта главное что бы диплом от курсов SkyPro",
    "http://test.com",
)

# Сохранение информации о вакансиях в файл
json_saver = Json_file()
json_saver.add_json(vacancy)
json_saver.delete_json()


if __name__ == "__main__":
    platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    user_interaction()
