# Comics to VK

Данный скрипт при каждом запуске скачивает с [xkcd.com](https://xkcd.com/) случайный комиск с комментарием у публикует в ваш паблик ВКонтакте.

## Как установить

Python3 должен быть уже установлен в системе.  
Используя `pip` или  `pip3`  (если есть конфликт с python2) необходимо установить  зависимости:

```shell
pip install -r requirements.txt
```

Рекомендуется использовать виртуальное окружение для изоляции проекта.  
Подробности: [virtualenv/venv](https://docs.python.org/3/library/venv.html).

### Получение CLIENT_ID и  ACCESS_TOKEN для Vkontakte
Чтобы скрипт работал нужно зарегистрировать новое приложение. Регистрируем вот [здесь](https://vk.com/dev/products).
Платформу выбираем standalone-приложение.
С помощью этого шага мы получаем **ClIENT_ID**

После идем и получаем **ACCESS_TOKEN**. Вся подробная информация [здесь](https://vk.com/dev/access_token)

Сохраняем полученные данные в файл `.env`.

В файле  `.env` написать:

```
CLIENT_ID_VK=ВАШ_CLIENT_ID
ACCESS_TOKEN_VK=ВАШ_ACCESS_TOKEN
```
## Создание паблика и получение GROUP_ID

Далее вам необходимо создать паблик, если его еще нет, куда скрипт будет публиковать комиксы.

После создания группы следуем получить её **ID**.
Сделать это можно [здесь](http://regvk.com/id/).

Дописываем в `.env`:
GROUP_ID_VK=ВАШ_GROUP_ID

## Как запустить скрипт

```shell
python3 main.py
```

После завершения работы, скрипт "скажет", как прошла его работа, успешно или нет.

В случае успеха у вас в паблике должен появиться новый пост с комиксом и текстом.

## Цель проекта

Данные скрипты написаны только с образовательной целью. 