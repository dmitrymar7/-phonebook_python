
Объекты:
1. Список телефонных номеров
2. Записи телефонного номера

Операции:
1. Вывод телефонного справочника
2. Добавление записи
3. Удаление записи
4. Экспорт в файл
5. Импорт в файл
6. Поиск
7. Редактирование
8. Перенос записи из одного справочника в другой

1. model
    2 объекта: телефонный справочник, запись телефонного справочника
    объект запись (record) определяется тремя атрибутами: имя (name), телефон(telephone),

2. view - отображение для пользователя
    Меню для операций - 1, 2, 3, 6, 7, 8

3. controller - логика работы меню
    Меню для операций - 1, 2, 3, 6, 7, 8

4. main
 Запуск констроллера