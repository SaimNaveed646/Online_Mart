    #Importing date and time module for history
import datetime

#Global variables
product_list = []
bills = 0
d = {}


#Create account function
def create_account():
    fh = open("accounts.txt","a")
    fhh = open("account holders name.txt","a")
    print('\nEnter your information\n----------------------')
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    username = input("Choose a username: ")
    print("NOTE: Password must be between 7 and 12 characters and should also include at least one digit.")
    password = input("Choose your password: ")

    #Password validity check for digit
    number = 0
    for i in password:
        if i.isdigit():
            number += 1

    #Password validity check for length
    if len(password) >= 7 and len(password) <= 12 and number >= 1:
        #Saving username and password
        user_pass = {username:password}
        fh.write(f'{user_pass}\n')
        fhh.write(f'- {first_name} {last_name}\n')
        print("Account created successfully. You can login now :)\n")
        fh.flush()
        fhh.flush()
        main_menu()
    else:
        print("ERROR: Your password does not meet the requirements. Try again!")
        main_menu()
    fh.close()
    fhh.close()


#Login function
def login():
    #Opening accounts file
    with open('accounts.txt') as file:

        #Taking login input from user
        print('\nEnter your credentials\n----------------------')
        global login_user
        login_user = input("Enter your username: ")
        login_password = input("Enter your password: ")

        #Checking for valid id
        user_pass = {login_user:login_password}
        count = 0
        for line in file:
            line = eval(line.strip())
            if line == user_pass:
                count += 1
        if count == 1:
            print("Login successful. You can shop now :)\n")

            #Opening file for shopping history (in case of no previous history)
            file_name = f"{login_user}"
            file = open(f"{file_name}.txt", 'a')
            file.close()

            #Second menu function call
            menu()
        else:
            print("ERROR: Either account does not exist or invalid username/password. Try again!\n")
            main_menu()
    file.close()


#Welcome interface / Main Menu
def main_menu():
    print("Welcome to SuperMart!\nHappy Shopping :)\n---------------------")
    choice = input("Choose:\na)Sign Up\nb)Login and Shop\nc)Exit the application\n=> ")
    if choice == 'a' or choice == 'A':
        create_account()
    elif choice == 'b' or choice == 'B':
        login()
    elif choice == 'c' or choice == 'C':
        print("Thank you! :)")
    else:
        print("Invalid choice! Enter 'c' to exit.")
        main_menu()


#Product list function
def products():
    global product_list, bills, d
    fl = open('products list.txt')
    print(fl.read())
    pl = input('\na) Add products to cart\nb) Back to menu\n=> ')
    if pl == 'a':
        add_to_cart()
    elif pl == 'b':
        menu()
    else:
        print("Invalid choice. Enter '2' to return to menu")
        menu()
    fl.close()


#Second menu after login
def menu():
    global product_list, bills, d
    print("Select an option:\n1. Shop Now\n2. Your Cart\n3. Your Shopping History\n4. Checkout Now\n5. Back to main menu\n6. Exit the application")
    option = int(input('Enter your choice (1-6): '))
    if option == 1:
        products()
    elif option == 2:
        view_cart()
    elif option == 3:
        read_history()
    elif option == 4:
        checkout()
    elif option == 5:
        main_menu()
    elif option == 6:
        print('Thank You! :)')
    else:
        print('invalid choice ')
        menu()


def view_cart():
    global product_list, bills, d
    print('\nYour Cart\n---------')
    print('Products:', product_list)
    print('Your total bill is Rs.', bills)
    print('Items with prices:', d)
    print('1. Remove items from cart\n2. Checkout now\n3. Back to menu')

    #Taking customer response
    k = input('Enter your response: ')
    if k =='1':
        remove_from_cart()
    elif k == '2':
        checkout()
    elif k == '3':
        menu()
    else:
        print("Invalid choice")
        menu()


#Add items to cart function
def add_to_cart():
    global product_list, bills, d
    while True:
        item = int(input("Enter your choice number ('0' to go back): "))
        if item == 1:
            bill = 200
            d['Apples'] = bill
            bills = bills + bill
            product_list = product_list + ['Apples']
        elif item == 2:
            bill = 150
            d['Bananas'] = bill
            bills = bills + bill
            product_list = product_list + ['Bananas']
        elif item == 3:
            bill = 120
            bills = bills + bill
            d['Potatoes'] = bill
            product_list = product_list + ['Potatoes']
        elif item == 4:
            bill = 150
            d['Tomatoes'] = bill
            bills = bills + bill
            product_list = product_list + ['Tomatoes']
        elif item == 5:
            bill = 200
            d['Milk'] = bill
            bills = bills + bill
            product_list = product_list + ['Milk']
        elif item == 6:
            bill = 300
            bills = bills + bill
            d['Eggs'] = bill
            product_list = product_list + ['Eggs']
        elif item == 7:
            bill = 80
            bills = bills + bill
            d['Butter'] = bill
            product_list = product_list + ['Butter']
        elif item == 8:
            bill = 100
            d['Cheese'] = bill
            bills = bills + bill
            product_list = product_list + ['Cheese']
        elif item == 9:
            bill = 50
            d['Bread'] = bill
            bills = bills + bill
            product_list = product_list + ['Bread']
        elif item == 10:
            bill = 100
            bills = bills + bill
            d['Cupcakes'] = bill
            product_list = product_list + ['Cupcakes']
        elif item == 11:
            bill = 100
            bills = bills + bill
            d['Muffins'] = bill
            product_list = product_list + ['Muffins']
        elif item == 12:
            bill = 100
            bills = bills + bill
            d['Rusk'] = bill
            product_list = product_list + ['Rusk']
        elif item == 0:
            break
        else:
            print("Invalid choice.")
            menu()
    print("Item(s) added to cart.")
    menu()


#Remove items from cart function
def remove_from_cart():
    global product_list, bills, d
    print("Products:", product_list)
    print("Total cost:", bills)
    print("Items with prices:", d)
    if len(product_list) == 0:
        print('No item in cart')
        menu()
    else:
        while True:
            item = input("Enter item name to remove (Enter 'n' to go back): ")
            item=item.capitalize()
            if item == 'Apples':
                bill = 200
                del d['Apples']
                product_list.remove('Apples')
                bills = bills - bill
            elif item == 'Bananas':
                bill = 150
                del d['Bananas']
                bills = bills - bill
                product_list.remove('Bananas')
            elif item == 'Potatoes':
                del d['Potatoes']
                bill = 120
                bills = bills - bill
                product_list.remove('Potatoes')
            elif item == 'Tomatoes':
                bill = 150
                del d['Tomatoes']
                product_list.remove('Tomatoes')
                bills = bills - bill
            elif item == 'Milk':
                bill = 200
                del d['Milk']
                bills = bills - bill
                product_list.remove('Milk')
            elif item == 'Eggs':
                del d['Eggs']
                bill = 300
                bills = bills - bill
                product_list.remove('Eggs')
            elif item == 'Butter':
                del d['Butter']
                bill = 80
                bills = bills - bill
                product_list.remove('Butter')
            elif item == 'Cheese':
                bill = 100
                del d['Cheese']
                product_list.remove('Cheese')
                bills = bills - bill
            elif item == 'Bread':
                bill = 50
                del d['Bread']
                bills = bills - bill
                product_list.remove('Bread')
            elif item == 'Cupcakes':
                del d['Cupcakes']
                bill = 100
                bills = bills - bill
                product_list.remove('Cupcakes')
            elif item == 'Muffins':
                del d['Muffins']
                bill = 100
                bills = bills - bill
                product_list.remove('Muffins')
            elif item == 'Rusk':
                del d['Rusk']
                bill = 100
                bills = bills - bill
                product_list.remove('Rusk')
            elif item == 'n' or item == 'N':
                break
            else:
                print("Invalid choice.")
                menu()
        print("Item(s) removed from cart")
        menu()


#Checkout function
def checkout():
    global product_list, bills, d
    print("Your products in cart:", product_list)
    print("Total cost:", bills)
    print("Item with prices:", d)
    ch = input("Confirm checkout? [Y/N]\n=> ")
    if ch == 'Y' or ch == 'y':
        print("Enter your card details\n----------------------")
        ck = input("Enter credit card number: ")
        cl = input("Enter card PIN: ")
        print("Payment successful :)\nYour order will be delivered in 2 hours\n")

        #File write (Shopping history)
        write_history()
        menu()

    #No checkout
    elif ch == 'N' or ch == 'n':
        cg = input("1. Go to cart\n2. Go back to menu\n=> ")
        if cg == '1':
            view_cart()
        elif cg == '2':
            menu()
        else:
            print("Invalid input. Going back to menu!")
            menu()
    else:
        print("Invalid input. Going back to menu!")
        menu()


#Shopping history saving function
def write_history():
    global product_list, bills, d
    file_name = f"{login_user}"
    file = open(f"{file_name}.txt", 'a')
    current_datetime = datetime.datetime.now()
    file.write(f"Products: {product_list}\nTotal Bill: {bills}\nCheckout completed at {current_datetime}\n")
    file.close()


#Shopping history view function
def read_history():
    global product_list, bills, d
    file_name = f"{login_user}"
    file1 = open(f"{file_name}.txt")
    print("\nShopping History\n----------------")
    print(file1.read())
    menu()
    file1.close()
