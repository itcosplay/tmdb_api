# tmdb_api
Набор скриптов для работы с информацией о фильмах.  
Все данные собираются c помощью API [www.themoviedb.org](https://www.themoviedb.org/).



## hello_api_TMDB
С помощью этого скрипта можно проверить работоспособность вашего токена.  
Если токен рабочий, напечатает в консоль название фильма "Пила 2".

![test_token](https://raw.githubusercontent.com/itcosplay/images/main/test_tmdb_token.png)  
Запустить скрипт:
```
python hello_api_TMDB.py
```


## make_own_db.py
Формирует в папке со скриптами файл `MyFilmDB.json` с информацией 1000 фильмах, взятой с [www.themoviedb.org](https://www.themoviedb.org/).  
К основной информации относятся название фильма, жанр, бюджет, краткое описание, дата выхода и т.д.  
По мере завершения работы скрипта в консоль будет напечатано соответвующее предупреждение.

![make_own_db](https://raw.githubusercontent.com/itcosplay/images/main/make_own_db.png)  
Запустить скрипт:
```
python make_own_db.py
```



## find_similar
Печатает в консоль список фильмов (максимум восемь) которые похожи на фильм, который запросил пользователь.  
Похожесть определяется исходя из следующих параметров:
- принадлежность к какой либо коллекции фильмов
- жанр
- оригинальный язык фильма
- бюджет фильма

По чем большим параметрам фильмы будут похожи, тем выше фильм отбразится при сортировке фильмов.
Максимально похожий фильм будет напечатан первым, далее по убыванию.
Запустить скрипт:
```
python find_similar.py film_title
```

## search_in_db
Ищет фильм по названию или части названия.
Если название фильма совпадает, или часть названия, введенного пользователем, есть в одном из названий фильмов, то все совпадения будут выведенны в консоль.
Поиск осуществляется 


