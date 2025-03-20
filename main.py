# Осуществить циклический сдвиг столбцов или строк
# (указывается отдельно) двумерного массива на n позиций.

def read_array(filename):
    with open(filename, "r") as file:
        content = file.read().strip()
        if not content:
            return []
        return list(map(int, content.split()))

def write_array(filename, array):
    with open(filename, "w") as file:
        file.write(' '.join(map(str, array)))
