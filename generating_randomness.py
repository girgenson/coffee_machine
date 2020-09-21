import inspect


def count_triads(string):
    triads = {'000': {0: 0, 1: 0}, '001': {0: 0, 1: 0}, '010': {0: 0, 1: 0}, '011': {0: 0, 1: 0},
              '100': {0: 0, 1: 0}, '101': {0: 0, 1: 0}, '110': {0: 0, 1: 0}, '111': {0: 0, 1: 0}}
    for i in range(len(string)-3):
        sliced = string[i:i+3]
        next_digit = string[i+3]
        triads[sliced][int(next_digit)] += 1
    return triads


def process_string(string: str) -> str:
    processed_string = ''
    for i in string:
        if i in ('0', '1'):
            processed_string += i
    return processed_string


def process_input(string=''):
    print('Please give AI some data to learn...')
    string = process_string(string)
    len_str = len(string)
    if len_str < 100:
        print(f'The current data length is {len_str}, {100 - len_str} symbols left')
        string += input('Print a random string containing 0 or 1:\n\n')
        if len(string) < 100:
            process_input(string)
        else:
            start_the_game(string)
    else:
        start_the_game(string)


def start_the_game(string):
    triads = count_triads(string)
    print(inspect.cleandoc(f"""Final data string:
          {string})
          You have $1000. Every time the system successfully predicts your next press, you lose $1.
          Otherwise, you earn $1. Print "enough" to leave the game. Let's go!""".lstrip()))
    cash = 1000
    test_string = ''

    while test_string != 'enough':
        test_string = input('\nPrint a random string containing 0 or 1:\n')
        if test_string != 'enough':
            test_string = process_string(test_string)
            payload = len(test_string) - 3
            if payload > 0:
                predicted_string = test_string[:3]
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
                cash += payload - 2 * vangued
                percent = round(vangued / payload * 100, 2)
                print(f'\nComputer guessed right {vangued} out of {payload} symbols ({percent} %)')
                print(f'Your capital is now ${cash}')
        else:
            print('Game over!')


if __name__ == '__main__':
    process_input()
