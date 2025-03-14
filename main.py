
def read_array(filename):
    with open(filename, 'r') as file:
        content = file.read().strip()
        if not contetn:
            return []
        return list(map(int, content.split()))

def write_array(filename, array):
     with open(filename, 'w') as file:
         file.write(' '.join(array))

