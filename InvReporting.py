# constants
INDEX_NAME = 0
INDEX_QUANTITY = 1
INDEX_PRICE = 2

def processMenu():
    print('Welcome to the Product Inventory Reporting System')
    print('-------------------------------------------------')
    print('<1> Print all Products')
    print('<2> Search for a Product')
    print('<3> Search by List index number')
    print('<999> End the Program')

    while True:
        try:
            user_input = int(input('Please select an option from the menu: '))
            if user_input == 1 or user_input == 2 or user_input == 3 or user_input == 999:
                break
            print('** Error: Invalid menu option selected, try again\n')
            print('Welcome to the Product Inventory Reporting System')
            print('-------------------------------------------------')
            print('<1> Print all Products')
            print('<2> Search for a Product')
            print('<3> Search by List index number')
            print('<999> End the Program')
        except:
            print('** Error: Menu selection must be an integer\n')
            print('Welcome to the Product Inventory Reporting System')
            print('-------------------------------------------------')
            print('<1> Print all Products')
            print('<2> Search for a Product')
            print('<3> Search by List index number')
            print('<999> End the Program')

    return user_input


def printList(products):
    print('Inventory Report')
    print('----------------')
    print(format('  Index', '20') + format('Product', '18') + format('Quantity', '18') + 'Price')
    print(format('  -----', '20') + format('-------', '18') + format('--------', '18') + '-----')

    total_quantity = 0
    total_price = 0
    index = 0
    for i in range(len(products)):
        name = products[i][INDEX_NAME]
        quantity = products[i][INDEX_QUANTITY]
        price = products[i][INDEX_PRICE]
        print('  ' + format(index, '5d') + (19*' ') + name + (11*' ') + format(quantity, '8d') + (9*' ') + format(price, '6.2f'))
        total_quantity += int(quantity)
        total_price += float(price)
        index = int(index)
        index += 1
    print('Total Inventory count:  ' + str(total_quantity))
    print('Total value of inventory:  ' + format(total_price, '.4f'))


def productInList(products, name):
    for i in range(len(products)):
        row = products[i][INDEX_NAME]
        if name == row:
            return products[i]
    else:
        return False


def productIndex(products, number):
    try:
        number = int(number)
        return products[number]
    except:
        return False


def main():
    file_var = open('Products.txt', 'r')
    lines = file_var.readlines()
    file_var.close()

    products = []
    for line in lines:
        product = line.split(', ')
        product[INDEX_QUANTITY] = int(product[INDEX_QUANTITY])
        product[INDEX_PRICE] = float(product[INDEX_PRICE])
        products += [product]

    user_input = processMenu()
    while user_input != 999:
        if user_input == 1:
            printList(products)
        elif user_input == 2:
            name = input('Enter a product to find: ')
            result = productInList(products, name)
            if result == False:
                print('Product not found')
            else:
                print(name + ' Found')
                print(format('Product', '18') + format('Quantity', '18') + 'Price')
                print(format('-------', '18') + format('--------', '18') + '-----')
                result_name = result[INDEX_NAME]
                result_quantity = str(result[INDEX_QUANTITY])
                result_price = result[INDEX_PRICE]
                print(format(result_name, '18') + format(result_quantity, '18') + format(result_price, '5.2f'))

        elif user_input == 3:
            index_number = input('Enter an index to find: ')
            result = productIndex(products, index_number)
            if result == False:
                    print('Product not found')
            else:
                print(str(index_number) + ' Found')
                print(format('Product', '18') + format('Quantity', '18') + 'Price')
                print(format('-------', '18') + format('--------', '18') + '-----')
                result_name = result[INDEX_NAME]
                result_quantity = str(result[INDEX_QUANTITY])
                result_price = result[INDEX_PRICE]
                print(format(result_name, '18') + format(result_quantity, '18') + format(result_price, '5.2f'))
        print('\n')
        user_input = processMenu()

    print('Program ending, have a nice day!')


if __name__ == '__main__':
    main()
