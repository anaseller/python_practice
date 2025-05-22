# Метод count()

Метод `str.count(substring, start, end)` используется для подсчёта количества вхождений подстроки `substring` в строке.

### Синтаксис:

`str.count(substring, start=0, end=len(str))`

    `substring – подстрока, количество вхождений которой нужно найти.
    `start` (необязательный) – индекс начала поиска (по умолчанию 0).
    `end` (необязательный) – индекс конца поиска (по умолчанию – конец строки).

🔹 Важно: `str.count()` чувствителен к регистру.
```
text = "Python python PyThOn"
print(text.count("python"))  # Вывод: 1
```

### Примеры:
#### 1. Подсчёт всех вхождений:
```
text = "hello world, hello again"
count_hello = text.count("hello")
print(count_hello)  # Вывод: 2
```
#### 2. Подсчёт в определённом диапазоне:
```
text = "banana banana banana"
count_ban = text.count("ban", 7, 20)  # Ищем с 7-го по 19-й символ
print(count_ban)  # Вывод: 1
```
#### 3. Поиск частичного совпадения:

Метод ищет непересекающиеся вхождения, поэтому, например, в строке "aaa" слово "aa" будет найдено 1 раз, а не 2:
```
print("aaa".count("aa"))  # Вывод: 1
```

