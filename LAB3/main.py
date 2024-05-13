from collections import deque


def is_valid_move(x, y):
    # Проверяет, что ход находится в пределах доски.
    return 0 <= x < 8 and 0 <= y < 8


def min_moves(start, end):
    # Находит минимальное число ходов для коня.
    # Преобразование начальной и конечной позиций в координаты на доске.
    start_x, start_y = ord(start[0]) - ord('A'), int(start[1]) - 1
    end_x, end_y = ord(end[0]) - ord('A'), int(end[1]) - 1

    # Возможные ходы коня.
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]

    # Массив для отслеживания посещенных позиций на доске.
    visited = [[False] * 8 for _ in range(8)]
    # Инициализация очереди для BFS.
    # Каждый элемент очереди - кортеж из (x, y) координаты и количества шагов до этой позиции.
    queue = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True

    # BFS для поиска минимального числа шагов.
    while queue:
        cur_x, cur_y, steps = queue.popleft()
        # Если текущая позиция совпадает с конечной, возвращаем количество шагов.
        if cur_x == end_x and cur_y == end_y:
            return steps
        # Проверяем возможные ходы коня.
        for dx, dy in moves:
            new_x, new_y = cur_x + dx, cur_y + dy
            # Если новая позиция в пределах доски и не посещалась ранее, добавляем ее в очередь.
            if is_valid_move(new_x, new_y) and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y, steps + 1))

    # Если достижимая позиция недостижима, возвращаем -1.
    return -1


# Получаем ввод от пользователя для начальной и конечной позиций.
start_pos = input("Введите начальную позицию (например, A5): ").upper()
end_pos = input("Введите конечную позицию (например, C2): ").upper()

# Проверяем и выводим результат.
if len(start_pos) == 2 and len(end_pos) == 2 \
        and start_pos[0] in 'ABCDEFGH' and end_pos[0] in 'ABCDEFGH' \
        and start_pos[1].isdigit() and end_pos[1].isdigit():
    print("Минимальное число ходов:", min_moves(start_pos, end_pos))
else:
    print("Пожалуйста, введите корректные позиции в формате, например, A5 или C2.")
