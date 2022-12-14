Архитектура REST предполагает применение следующих методов или типов запросов HTTP для взаимодействия с сервером, где каждый тип запроса отвечает за определенное действие:

GET (получение данных)

POST (добавление данных)

PUT (изменение данных)

DELETE (удаление данных)

Кроме этих типов запросов HTTP поддерживает еще ряд, в частности:

OPTIONS

HEAD

PATCH

TRACE

В классе FastAPI для каждого из этих типов запросов определены одноименные методы:

get()

post()

put()

delete()

options()

head()

patch()

trace()


Api = метод общения между разными приложениями, оно представлено в виде JSON(словаря)

min_length: устанавливает минимальное количество символов в значении параметра

max_length: устанавливает максимальное количество символов в значении параметра

regex: устанавливает регулярное выражение, которому должно соответствовать значение параметра

lt: значение параметра должно быть меньше определенного значения

le: значение параметра должно быть меньше или равно определенному значению

gt: значение параметра должно быть больше определенного значения

ge: значение параметра должно быть больше или равно определенному значению

