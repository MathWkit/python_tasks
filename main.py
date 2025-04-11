
# Осуществить циклический сдвиг столбцов или строк
# (указывается отдельно) двумерного массива на n позиций.

def read_array(filename):
    with open(filename, "r") as file:

import os

def read_array(filename):
    with open(filename, 'r') as file:

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

def write_array(filename, array):
     with open(filename, 'w') as file:
         file.write(' '.join(map(str, array)))

def array_to_progression(array):
    n = len(array)
    if n <= 2:
        return array

    min_changes = n
    best_array = array[:]

    for i in range(n):
        for j in range(i + 1, n):
            a1 = array[i]
            a2 = array[j]

            if (a2 - a1) % (j - i) != 0:
                continue

            d = (a2 - a1) / (j - i)
            changes = 0

            for k in range(n):
                expected_element = a1 + (k - i) * d
                if array[k] != expected_element:
                    changes += 1

            if changes < min_changes:
                min_changes = changes
                best_array = [int(a1 + (k - i) * d) for k in range(n)]

    print("Количество изменений: " + str(min_changes))
    return best_array

files = {
    "arr1.txt": "1.08 2 3 4.7 5",
    "arr2.txt": "-1 -2 -30 -4 -5",
    "arr3.txt": "",
    "arr4.txt": "1 16 4 10 7 11 1 -2",
    "arr5.txt": "51afuhafh 38 10 38 4 52",
    "arr6.txt": "1 2",
}

for filename, content in files.items():
    with open(filename, "w") as file:
        file.write(content)

for filename in files.keys():
    try:
        array = read_array(filename)
    except ValueError:
        print("Неверные входные данные\n")
        continue

    print(f"Исходный массив из {filename}: {array}")

    progression = array_to_progression(array)

    print(f"Преобразованный массив: {progression}\n")
    output_filename = "output_" + filename
    write_array(output_filename, progression)
