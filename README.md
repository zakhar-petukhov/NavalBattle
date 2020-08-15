# Тестовое задание по поиску кораблей
На вход подается файл, состоящий из n строк, по n символов в каждой. Символ "-" - значит, 
что в этой клетке нет корабля, символ "#" - означает, что в этой клетке находится корабль или 
часть корабля. Кораблем считается непрерывная последовательность символов "#" по вертикали или 
горизонтали. Корабли не должны соприкасаться. 
Длина и ширина игрового поля не может быть больше 1000. На вход могут 
подаваться и некорректные данные - нужно добавить обработку ошибок.


### Гайд по разветыванию
1) файл с кораблями должен иметь название ships.txt
2) создаем докер образ docker build -t application .
3) запускаем контейнер и сразу после его остановки он удаляется 
```docker run -v $PWD:/app -i -t application  python /app/main.py --rm ```
Это нам позволяет при подсчете кораблей на новой карте не пересобирать образ,  а просто менять файл в нашем контейнере