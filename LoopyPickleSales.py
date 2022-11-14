# print welcome
print('Welcome to my Pickle Ordering system')

# ask for input from user
name = input('Please enter your store\'s name (or "exit" to stop the program):\n')

# while the user has not typed exit - main loop
while 'exit' != name:
    num_pickles = int(input('How many pickles would you like to order?\n'))
    # input validation for number of pickles
    while num_pickles < 1:
        print('ERROR: you have to order at least 1 pickle')
        num_pickles = int(input('How many pickles would you like to order?\n'))

    tax_exempt = input('Are you tax exempt? (Y/N): ')
    # input validation for tax-exempt answer
    while 'Y' != tax_exempt and 'N' != tax_exempt:
        print('ERROR: please answer Y or N')
        tax_exempt = input('Are you tax exempt? (Y/N): ')

    # convert input to boolean variables -- programming assignment 3 code
    tax_exempt = tax_exempt == 'Y'

    # discount rates
    if num_pickles <= 1000:
        discount_rate = 0
    elif num_pickles <= 2000:
        discount_rate = 0.1
    elif num_pickles <= 3000:
        discount_rate = 0.15
    elif num_pickles > 3000:
        discount_rate = 0.2

    # shipping costs
    shipping_cost = 100.0
    if num_pickles > 2000:
        shipping_cost = 150.0

    PICKLE_PRICE = 0.29
    TAX_RATE = 0.0875

    # calculations
    gross_price = PICKLE_PRICE * num_pickles
    discount_amount = gross_price * discount_rate
    discounted_price = gross_price - discount_amount
    if tax_exempt:
        sales_tax = 0.0
    else:
        sales_tax = TAX_RATE * discounted_price

    total_price = discounted_price + sales_tax + shipping_cost

    # print orders
    print('\n\n\n\n')
    print('Pickle order for', name)
    print('===================')
    print('Total Pickles Cost:  ', gross_price)
    print('Discount amount:     ', discount_amount)
    print('Tax:                 ', sales_tax)
    print('Shipping Cost:       ', shipping_cost)
    print('Total:               ', total_price)

    name = input('Please enter your store\'s name (or "exit" to stop the program):\n')

print('Program ending, have a nice day')
