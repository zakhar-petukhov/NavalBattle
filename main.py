class ErrorMap(Exception):
    pass


def validators(arr):
    count_horizontal_lines = len(arr)
    count_vertical_lines = len(arr[0].replace('\n', ''))

    for index in range(len(arr)):
        count_symbols = len(arr[index].replace('\n', ''))

        if count_symbols != count_horizontal_lines and count_symbols < 1000 and len(
                arr) != count_vertical_lines:
            raise ErrorMap('Карта должна быть квадратом и меньше 1000 символов по горизонтале!')


def search_ships():
    with open('ships.txt') as file:
        all_lines = file.readlines()
        validators(all_lines)
        arr = tuple(map(tuple, all_lines))  # карта с кораблями

    n = len(arr)  # длина строк и столбцов
    ship_counter = 0  # счетчик кораблей

    prev_check = False  # если последняя клетка была частью корабля
    prev_row = -1

    ship_coords = []

    for i in range(n):
        for j in range(n):

            if prev_check and arr[i][j] == '.':
                prev_check = False
                prev_row = -1

            elif arr[i][j] == '#':
                ship_coords.append([i, j])

                if [i - 1, j] in ship_coords:
                    ship_counter -= 1

                if prev_check and prev_row == i:
                    continue

                ship_counter += 1
                prev_check = True
                prev_row = i

    return f"Всего {ship_counter} кораблей."


print(search_ships())
