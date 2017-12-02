import itertools

INPUT_FILE = 'input.tsv'

test_input = '''
5 1 9 5
7 5 3
2 4 6 8
'''

test_mod_input = '''
5 9 2 8
9 4 7 3
3 8 6 5
'''

def input_to_int(input):
    return [[int(cell) for cell in row] for row in input]

def get_test_input(s):
    input = s.split('\n')
    input_str = [row.split(' ') for row in input][1:-1]
    return input_to_int(input_str)

def get_input_from_tsv_file(path, sep='\t'):
    with open(path) as file:
        input = file.readlines()
    input_str = [row.rstrip().split(sep) for row in input]
    return input_to_int(input_str)

def get_checksum(input):
    #print(input)
    return sum([max(row) - min(row) for row in input])

def get_row_mod(row):
    combos = itertools.combinations(row, 2)
    for t in combos:
        mod = max(t) % min(t)
        if mod == 0:
            return int(max(t)/min(t))
    return 0

def get_mod_checksum(input):
    return sum([get_row_mod(row) for row in input])

assert get_checksum(get_test_input(test_input)) == 18
print(get_checksum(get_input_from_tsv_file(INPUT_FILE)))

assert get_mod_checksum(get_test_input(test_mod_input)) == 9
print(get_mod_checksum(get_input_from_tsv_file(INPUT_FILE)))