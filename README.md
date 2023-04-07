# StringHolder

## Установка Catch2
```
cd third-party
git clone git@github.com:catchorg/Catch2.git
cd Catch2

cmake -Bbuild -H. -DBUILD_TESTING=OFF
sudo cmake --build build/ --target install
```
---
## Документация
StringHolder - это хранитель строковых типов данных либо std::string либо std::string_view.
<br>
Изначально идея была реализовывать через шаблон, но было предложено реализовать чистым классом.
Собственно это накладывает определённые сложности с методами доступа к данным. Из-за нехватки времени в связи сложившихся в моей жизни печальных обстоятельств, пришлось operator [] сделать немного кривоватым. В целом методы data() и operator [] оба кривоваты и используют следующий <a href="https://devblogs.microsoft.com/oldnewthing/20191106-00/?p=103066">хак</a>. Шаблонный класс решал бы эту проблему, но что есть то есть.<br>
В целом для модификации данных есть метод update(), который отлично подходит для обновления.<br>
Доставания по одному символу в случае std::string_view внутри экземпляра StringHolder'а достаточно неудобное.
### Сборка проекта
```
cd build; cmake ..; make
```
* Бинарные файлы лежат в папке bin/
<br>
* Запуск интеграционных тестов из корневой папки проекта

```
make integrate
```

---
### Методы StringHolder

* ```size_t size()``` - возвращает размер хранимых строковых данных.
* ```bool empty()``` - возвращает true если хранимые строковые данные пусты.
* ```resultData data()``` - возвращает внутренний класс resultData который потом можно сконвертировать неявно к char* или const char* соответсвенно.
* ```resultData operator[] (size_t)``` - ситуация как и с data. Требует прямого вызова метода operator const char&(), так как иначе разрешить не получается. Пришлось сделать explicit.
* ```operator std::string_view ()``` - позволяет передавать StringHolder туда где ожидается std::string_view.
* ```std::string_view string_view()``` - возвращает std::string_view хранимых строковых данных.
* ```std::string string()``` - возвращает std::string или делает копию если объект конструировался на std::string_view.
* ```std::string releaseString()``` - возвращает std::string внутренних текстовых данных, если внутри находиться std::string переводит его в нулевое, но валидное состояние(механика move-семантики).
* ```void update(std::string)``` - обновляет внутрение строковые данные, используя std::string.
* ```void update(std::string_view)``` - обновляет внутрение строковые данные, используя std::string_view.