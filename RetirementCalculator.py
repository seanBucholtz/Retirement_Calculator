# Sean Bucholtz
# Section 3
# 5/15/13
# Assignment 5: Retirement Planning - Variable Investment Model

# calculates the individual retirment amounts
def calc_final_balance(age, amount, percent):
    dec = percent/100
    bal = 0
    count = age
    while count < 70:
        count += 1
        bal = bal+amount
        bal += bal*dec
    return bal

# prints chart based on input value
def chart(amount):
    print('\nStarting \t\t Assumed Interest Rate')
    print(' Age\t   4%\t\t    6%\t\t    8%\t\t    10%')
    for age in range(20,65+1,5):
        print(' ' + str(age) + '\t', end='')
        for percent in [4,6,8,10]:
            print('$' + format(calc_final_balance(age, amount, percent),\
                               '8,.2f'), '\t',end='')
        print()
    print('\n\nProtect your future - When will you start saving for' +\
          ' retirement?')

# promts user from input and validates whether it is a number or not
def valid_num(prompt):
    try:
        num = float(input(prompt))
        return num
    except ValueError: # if num is not int or float displays error message
        print('\nOops! You did not enter a valid number of dollars')
        return False #returns false for conditional loop

# function abstractly receives user input value and verifys that it meets
# certain conditions
def value():
    amount = valid_num('\n\nHow many dollars towards your retirement' +\
                       ' would you like to save each year?: $')
    while amount == False or amount < 100:

        if amount < 100 and amount != False: # filters and repeats until >=100
            print('\nThe amount to be save needs to be greater than $100.')
            amount = valid_num('\nPlease enter a new amount: $')
            
        if amount == False: 
          # filters and repeats input if it is False (not int or float)
            amount = valid_num('\nPlease enter the number of dollars you' +\
                           ' would like to save: $')
    return amount

def main():
    print('Welcome to Retirement Forecaster...')
    amount = value()
    chart(amount)
    again = input('\nWould you like to forcast a new dollar amount? (Yes/No): ')
    # input validation loops
    while (again != 'Yes' and again != 'yes' and again != 'Y' and again != 'y'\
          and again != 'No' and again != 'no' and again != 'N' and \
           again != 'n') or (again == ''): # filters invalid input
        again = input('I do not understand "' + str(again) + \
                      '" Please respond with either Yes or No: ')
    while (again == 'Yes' or again == 'yes' or again == 'Y' or \
               again == 'y'): # repeats tables
        amount = value()
        chart(amount)
        again = input('\nWould you like to forcast a new dollar amount? (Yes/No): ')
    if (again == 'No' or again == 'no' or again == 'N' or \
           again == 'n'): # end session
        print('\nThank you for using Retirement Forecaster!')
        
main()

""" Test Results:

Output chart values match externally verified results and example chart:
    Calling -
    print('$' + format(calc_final_balance( 30, 3000, 6 ), '.2f'))
    print('$' + format(calc_final_balance( 20, 2000, 5.5 ), '.2f'))
    Results in the two (correct) values -
    $492143.05 & $519518.88
If these two outputs are correct, different arguements will also produce
correct results.

Input values != to type float or type int are handled and user is promted to
re-enter values unitl the value is type int or float >= 100.

Output is properly repeated at the user's discretion and all invalid inputs are
negotiated via input validation loops.

END of Results
"""
