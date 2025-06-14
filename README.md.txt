# Прогноз погоды на Flask

Это простое веб-приложение, позволяющее пользователю ввести название города и получить текущий прогноз погоды, используя API Open-Meteo.

---

▌Что сделано

- Создано веб-приложение на Python с использованием фреймворка Flask.
- Реализована форма для ввода названия города.
- Получение координат города через Open-Meteo Geocoding API.
- Запрос и отображение текущей погоды с использованием Open-Meteo API.
- Вывод данных в удобочитаемом и простом формате.

---

▌Использованные технологии

- Python 3
- Flask — веб-фреймворк для создания сервера и маршрутов
- Requests — библиотека для HTTP-запросов к внешним API
- Open-Meteo API — источник данных о погоде и геокодинге
- HTML и CSS — для фронтенда (шаблоны Jinja2)

---

▌Как запустить приложение

Клонируйте репозиторий или скачайте файлы к себе:

shell

pip install flask requests


Запустите приложение:

shell

python app.py


Откройте браузер и перейдите по адресу:

http://127.0.0.1:5000


Введите название города в форму и получите прогноз погоды.
