class Machine:
    def __init__(self):
        self.machine_state = {'water': 400, 'milk': 540, 'beans': 120, 'money': 550, 'cups': 9}
        self.recipe = {'espresso': {'water': 250, 'beans': 16, 'money': 4, 'cups': 1},
                       'latte': {'water': 350, 'milk': 75, 'beans': 20, 'money': 7, 'cups': 1},
                       'cappuccino': {'water': 200, 'milk': 100, 'beans': 12, 'money': 6, 'cups': 1}}
        self.drink_codes = {1: self.recipe['espresso'], 2: self.recipe['latte'], 3: self.recipe['cappuccino']}

    def run_machine(self):
        what_to_do = ''

        while what_to_do != 'exit':
            what_to_do = input('Write action (buy, fill, take, remaining, exit):\n')

            if what_to_do == 'buy':
                enough_resources = True
                what_to_buy = input('\nWhat do you want to buy? 1 - espresso, 2 - latte,3 - cappuccino, back - to main menu:\n')

                if what_to_buy == 'back':
                    continue

                current_drink = self.drink_codes[int(what_to_buy)]
                machine_state_check = self.machine_state.copy()

                for i in machine_state_check:  # Estimate new machine state after dispensing a drink
                    machine_state_check[i] -= current_drink.get(i, 0)

                    if machine_state_check[i] < 0:
                        print(f'Sorry, not enough {i}!\n')
                        enough_resources = False

                if enough_resources:  # Subtract coffee components from machine resources
                    print('I have enough resources, making you a coffee!\n')
                    for i in self.machine_state:
                        self.machine_state[i] -= current_drink.get(i, 0)
                    self.machine_state['money'] += current_drink['money'] * 2  # *2 due to automatic substr. of money

            elif what_to_do == 'fill':
                self.machine_state['water'] += int(input('\nWrite how many ml of water do you want to add:\n'))
                self.machine_state['milk'] += int(input('Write how many ml of milk do you want to add:\n'))
                self.machine_state['beans'] += int(input('Write how many grams of coffee beans do you want to add:\n'))
                self.machine_state['cups'] += int(input('Write how many disposable cups of coffee do you want to add:\n'))
                print()

            elif what_to_do == 'take':
                print(f"\nI gave you ${self.machine_state['money']}\n")
                self.machine_state['money'] = 0

            elif what_to_do == 'remaining':
                print(f'''\n\rThe coffee machine has:\n\r{self.machine_state['water']} of water
                \r{self.machine_state['milk']} of milk\n\r{self.machine_state['beans']} of coffee beans
                \r{self.machine_state['cups']} of disposable cups\n\r${self.machine_state['money']} of money\n''')


Machine().run_machine()
