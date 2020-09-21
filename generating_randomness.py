def count_triads(string):
    triads = {'000': {0: 0, 1: 0}, '001': {0: 0, 1: 0}, '010': {0: 0, 1: 0}, '011': {0: 0, 1: 0},
              '100': {0: 0, 1: 0}, '101': {0: 0, 1: 0}, '110': {0: 0, 1: 0}, '111': {0: 0, 1: 0}}
    for i in range(len(string)-3):
        sliced = string[i:i+3]
        next_digit = string[i+3]
        triads[sliced][int(next_digit)] += 1
    return triads


def process_input(processed_string=''):
    string = input('Print a random string containing 0 or 1:\n\n')
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
        triads = count_triads(processed_string)
        print(triads)
        test_string = input('Please enter a test string containing 0 or 1:\n\n')
        payload = len(test_string) - 3
        predicted_string = test_string[:3]
        print('predicted_string', predicted_string)
        for i in range(payload):
            sliced = test_string[i:i+3]
            next_digit = 0 if triads[sliced][0] > triads[sliced][1] else 1
            predicted_string += str(next_digit)
        print('prediction:')
        print(predicted_string)
        vangued = 0
        for i in range(payload):
            if predicted_string[i] == test_string[i]:
                vangued += 1
        print(f'Computer guessed right {vangued} out of {payload} symbols ({round(vangued / payload * 100, 2)} %)')


process_input()
