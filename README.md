### Описание:
---
В данном тестовом приложении реализовано REST API, позволяющее создавать, получать и фильтровать объекты с помощью отправки JSON.
Проект выполнен на базе Django и Django Rest Framework.
   
#### Замечания:
---
В проекте использована база данных **Sqlite3**, которая поставляется вместе с Django.

#### Инструкция:
---
В файле ***requirements.txt*** указаны все необходимые бибилотеки для работы приложения.
Для установки библиотек воспользуйтесь командой:
```sh
pip install -r requirements.txt
```
Для запуска приложения необходимо перейти в каталог проекта, где находится файл manage.py, и выполнить следующую команду:
```sh
python manage.py runserver
```
Далее представлен перечень **curl** команд для выполнения тестового сценария(протестированы в коммандной строке Windows 10):
1. Создание объетков:
    ```sh
    curl -H "Content-Type: application/json" -X POST "http://127.0.0.1:8000/api/products/" / -d "{"""products""": [{"""title""": """title_value""", """description""": """description_value""", """parameters""": {"""param""": """param_value"""}},{"""title""": """title_value2""", """description""": """description_value2""", """parameters""": {"""param2""": """param_value2"""}}]}"
    ```
2. Вывод всей коллекции из базы:
    ```sh
    curl "http://127.0.0.1:8000/api/products/"
    ```
3. Вывод объектов, отфильтрованных по:
    *ids:*
    ```sh
       curl -H "Content-Type: application/json" -X GET "http://127.0.0.1:8000/api/products/" -d "{"""ids""":["""1""","""20"""]}"
    ```
    *titles:*
    ```sh
       curl -H "Content-Type: application/json" -X GET "http://127.0.0.1:8000/api/products/" -d "{"""titles""":["""title1""","""title2"""]}"
    ```
    *parameters:*
    ```sh
       curl -H "Content-Type: application/json" -X GET "http://127.0.0.1:8000/api/products/" -d "{"""parameters""": {"""param1""": """param1""", """param2""": """param2"""}}"
    ```