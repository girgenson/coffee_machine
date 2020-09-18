def count_triads(string):
    triads = {'000': {0: 0, 1: 0}, '001': {0: 0, 1: 0}, '010': {0: 0, 1: 0}, '011': {0: 0, 1: 0},
              '100': {0: 0, 1: 0}, '101': {0: 0, 1: 0}, '110': {0: 0, 1: 0}, '111': {0: 0, 1: 0}}
    for i in range(len(string)-3):
        sliced = string[i:i+3]
        next_digit = string[i+3]
        triads[sliced][int(next_digit)] += 1
    for i, j in triads.items():
        print(f'{i}: {j[0]},{j[1]}')


def process_input(processed_string=''):
    string = input('Print a random string containing 0 or 1:\n')
    for i in string:
        if i in ('0', '1'):
            processed_string += i
    print(processed_string)
    len_str = len(processed_string)
    if len_str < 100:
        print(f'Current data length is {len_str}, {100 - len_str} symbols left')
        process_input(processed_string)
    else:
        print('Final data string:\n' + processed_string + '\n')
        count_triads(processed_string)


process_input()
