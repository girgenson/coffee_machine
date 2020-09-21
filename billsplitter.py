import random


how_many_people_want_to_join = int(input('Enter the number of friends joining (including you):\n'))
if how_many_people_want_to_join <= 0:
    print('No one is joining for the party')
else:
    friends = {}
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(how_many_people_want_to_join):
        friends[input()] = 0
    total_bill = input('Enter the total bill value:\n')
    if input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n') == 'Yes':
        how_many_people_want_to_join -= 1
        random_name = random.choice(list(friends))
        print(f'{random_name} is the lucky one!')
        friends[random_name] = 0
    else:
        print('No one is going to be lucky')
        random_name = None
    divided_bill = round(float(total_bill) / how_many_people_want_to_join, 2)
    for i in friends:
        if i == random_name:
            continue
        friends[i] += divided_bill
    print(friends)
