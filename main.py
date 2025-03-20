# Осуществить циклический сдвиг столбцов или строк
# (указывается отдельно) двумерного массива на n позиций.

def read_array(filename):
    with open(filename, "r") as file:
        content = file.read().strip()
        if not content:
            return []
        return list(map(int, content.split()))

def write_matrix(filename, matrix):
    with open(filename, "w") as file:
        file.write(' '.join(map(str, matrix)))

def cyclic_shift(matrix, n, setting):
    if not matrix or not matrix[0]:
        return

    if setting == 'r':
        n = n % len(matrix)
        return matrix[-n:] + matrix[:-n]
    elif setting == 'c':
        n = n % len(matrix[0])
        return [row[-n:] + row[:-n] for row in matrix]
        return
    else:
        print("Настройка должна быть r (rows) или c (columns)")


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nСдвиг строк вниз на 2:")
shifted_matrix = cyclic_shift(matrix, 2, 'r')
for row in shifted_matrix:
    print(row)

print("\nСдвиг столбцов вправо на 2:")
shifted_matrix = cyclic_shift(matrix, 2, 'c')
for row in shifted_matrix:
    print(row)
