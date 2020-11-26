### Описание:
---
*Микросервис для электронного магазина.*

В данном тестовом приложении реализовано REST API, позволяющее создавать, получать и фильтровать объекты с помощью отправки JSON.

Проект выполнен на базе Django и Django Rest Framework.

Модель имеет следующие поля:
 - Идентификатор(id)
 - Название(title)
 - Описание(description)
 - Параметры(parameters): словарь, где key - название параметра; value - занчение параметра

### Замечания:
---
В проекте использована база данных **Sqlite3**, которая поставляется вместе с Django.

### Инструкция:
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
    curl -H "Content-Type: application/json" -X POST "http://127.0.0.1:8000/api/products/" -d "{"""products""": [{"""title""": """value""", """description""": """value""", """parameters""": {"""parameter""": """value"""}},{"""title""": """value2""", """description""": """value2""", """parameters""": {"""parameter1""": """value1""", """parameter2""": """value2"""}}]}"
    ```
2. Вывод всей коллекции из базы:
    ```sh
    curl "http://127.0.0.1:8000/api/products/"
    ```
3. Вывод объектов, отфильтрованных по:

    *ids:*

    ```sh
       curl -H "Content-Type: application/json" -X GET "http://127.0.0.1:8000/api/products/" -d "{"""ids""":["""5""","""20""","""47"""]}"
    ```
    *titles:*
    ```sh
       curl -H "Content-Type: application/json" -X GET "http://127.0.0.1:8000/api/products/" -d "{"""titles""":["""title1""","""title2"""]}"
    ```
    *parameters:*
    ```sh
       curl -H "Content-Type: application/json" -X GET "http://127.0.0.1:8000/api/products/" -d "{"""parameters""": {"""parameter1""": """value1""", """parameter2""": """value2"""}}"
    ```