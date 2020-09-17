processed_string = ''


def input_1010(processed_string):
    string = input('Print a random string containing 0 or 1:')
    for i in string:
        if i in ('0', '1'):
            processed_string += i
    print(processed_string)
    len_str = len(processed_string)
    if len_str < 100:
        print(f'Current data length is {len_str}, {100 - len_str} symbols left')
        input_1010(processed_string)
    else:
        print('Final data string:\n' + processed_string)

input_1010(processed_string)