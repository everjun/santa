# Тайный Санта
Скрипт для проведения мероприятия тайной раздачи подарков.

## Требования к работе скрипта
### Технические:
python 3.6+

### Требования к файлам participants.json
В файле должны содержаться сведения об участниках мероприятия. Представляет собой словарь вида
```
{
    "Имя человека (должно быть уникально)" : {
        "email": "Электронная почта человека",
        "is_nonresident": "Нужно ли отправлять подарок этому человеку в другой город, значения: true или false",
        "address": "Адрес на случай, если предыдущее поле true",
        "blacklist": ["Список людей, которым этот человек по тем или иным причинам не может сделать подарок"]
    }
}
```
Пример файла найдете в participants.json.example. Файл с названием "participants.json" должен лежать в той же папке, 
что и скрипт

### Требования к файлам smtp.json
В файле должны содержаться сведения для подключения к электронной почте gmail с выключенными настройками безопасных 
приложений
```
{
  "host": "smtp.gmail.com",
  "port": "587",
  "user": "имя пользователя гугл",
  "password": "пароль от аккаунта"
}
```
Файл с названием "smtp.json" олжен лежать в той же папке, что и скрипт

## Запуск
После добавления настроек smtp и участников мероприятия, просто запустите скрипт командой
```
python main.py
```
С Новым Годом и с Рождеством! Приятного пользования!
