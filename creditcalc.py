import math
import argparse


def estimate_remain_period():
    number = payment / (payment - i * principal)
    estimated_periods = math.log(number, (1 + i))
    estimated_periods = math.ceil(estimated_periods)
    number_of_years = estimated_periods // 12
    remain_months = estimated_periods % 12
    number_of_years = str(number_of_years) + ' years' if number_of_years > 0 else ''
    remain_months = str(remain_months) + ' months' if remain_months > 0 else ''
    a_n_d = ' and ' if (number_of_years != '' and remain_months != '') else ''
    print(f'It will take {number_of_years}{a_n_d}{remain_months} to repay this loan!')
    print(f'Overpayment = {payment * estimated_periods - principal}')


def estimate_monthly_payment():
    monthly_payment = principal * i * one_plus_i_pow_n / (one_plus_i_pow_n - 1)
    monthly_payment = math.ceil(monthly_payment)
    print(f'Your monthly payment = {monthly_payment}!')
    print(f'Overpayment = {monthly_payment * periods - principal}')


def estimate_loan_principal():
    estimated_principal = payment / (i * one_plus_i_pow_n / (one_plus_i_pow_n - 1))
    print(f'Your loan principal = {math.floor(estimated_principal)}!')
    print(f'Overpayment = {payment * periods - math.floor(estimated_principal)}')


def estimate_mth_differentiated_payment():
    count, overall = 0, 0
    for month in range(periods + 1):
        d = principal / periods + i * (principal - (principal * (month - 1)) / periods)
        rounded_d = math.ceil(d)

        if count > 0:
            overall += rounded_d
            print(f'Month {month}: payment is {rounded_d}')
        count += 1
    print(f'\nOverpayment = {overall - principal}')


parser = argparse.ArgumentParser(description='Enter type of credit, --principal, --periods, --intersect, --payment')
parser.add_argument('-ty', '--type', choices=['annuity', 'diff'], type=str)
parser.add_argument('-pa', '--payment', type=int)
parser.add_argument('-pr', '--principal', type=int)
parser.add_argument('-pe', '--periods', type=int)
parser.add_argument('-in', '--interest', type=float)
args = vars(parser.parse_args())

principal = args.get('principal')
payment = args.get('payment')
interest = args.get('interest')
periods = args.get('periods')
i = interest / (12 * 100) if interest else 0
one_plus_i_pow_n = (1 + i) ** periods if i and periods else 0


# Run script:
if args.get('type') == 'diff' and principal and periods and interest and not payment:
    estimate_mth_differentiated_payment()
elif args.get('type') == 'annuity' and interest:
    if principal and payment and not periods:
        estimate_remain_period()
    elif principal and periods and not payment:
        estimate_monthly_payment()
    elif payment and periods and not principal:
        estimate_loan_principal()
    else:
        print('Incorrect parameters')
else:
    print('Incorrect parameters')
