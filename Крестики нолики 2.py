primum_iecit = 1

def primum():
    global primum_iecit
    if primum_iecit == 1:
        name_ = "X"
        return name_
    else:
        name_ = "O"
        return name_


matrix = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]


def electio():
    global primum_iecit
    global matrix
    if primum_iecit == 1:
        cellula_x = input(f"Игрок {primum()} выбирает клетку по оси X - ")
        cellula_y = input(f"Игрок {primum()} выбирает клетку по оси Y - ")
        index_x = int(cellula_x) - 1
        index_y = int(cellula_y) - 1
        if index_x > 3 or index_y > 3:
            print ("Отказ, клетка вне поля")
            electio()
        elif matrix[index_x][index_y] != 'X' and matrix[index_x][index_y] != 'O':
            matrix[index_y].pop(index_x)
            matrix[index_y].insert(index_x, "X")
            primum_iecit += 1
        else:
            print("Отказ, клетка занята")
            electio ()

    else:
        cellula_x = input(f"Игрок {primum()} выбирает клетку по оси X - ")
        cellula_y = input(f"Игрок {primum()} выбирает клетку по оси Y - ")
        index_x = int(cellula_x) - 1
        index_y = int(cellula_y) - 1
        if index_x > 3 or index_y > 3:
            print ("Отказ, клетка вне поля")
            electio()
        elif matrix[index_x][index_y] != 'X' and matrix[index_x][index_y] != 'O':
            matrix[index_y].pop(index_x)
            matrix[index_y].insert(index_x, "O")
            primum_iecit -= 1
        else:
            print("Отказ, клетка занята")
            electio()


def theatrum_operationum ():
    print("        X")
    print("      1 2 3")
    print(f"    1 {matrix[0][0]} {matrix[0][1]} {matrix[0][2]}")
    print(f" Y  2 {matrix[1][0]} {matrix[1][1]} {matrix[1][2]}")
    print(f"    3 {matrix[2][0]} {matrix[2][1]} {matrix[2][2]}")

theatrum_operationum ()
def game():
    global primum_iecit
    electio()
    theatrum_operationum()
    if (matrix [0][0] is matrix [0][1] and matrix[0][0] is matrix[0][2] and matrix [0][0] != " ") or \
            (matrix [0][0] is matrix [1][0] and matrix[0][0] is matrix[2][0] and matrix [0][0] != " ") or \
            (matrix [0][0] is matrix [1][1] and matrix[0][0] is matrix[2][2] and matrix [0][0] != " ") or \
            (matrix [0][2] is matrix [1][1] and matrix[0][2] is matrix[2][0] and matrix [0][2] != " ") or \
            (matrix [2][0] is matrix [2][1] and matrix[2][0] is matrix[2][2] and matrix [2][0] != " ") or \
            (matrix [0][2] is matrix [1][2] and matrix[0][2] is matrix[2][2] and matrix [0][2] != " ") or \
            (matrix [0][1] is matrix [1][1] and matrix[0][1] is matrix[2][1] and matrix [0][1] != " ") or \
            (matrix [1][0] is matrix [1][1] and matrix[1][0] is matrix[1][2] and matrix [1][0] != " "):
                if primum_iecit == 1:
                    primum_iecit += 1
                    print (f"Игра окончена. Победил игрок {primum()}")
                else:
                    primum_iecit -= 1
                    print (f"Игра окончена. Победил игрок {primum()}")
    else:
        print("Продолжаем")
        return game ()



game ()
