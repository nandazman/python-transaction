from cashier import Transaction

transaction = Transaction()

print('Welcome To Andi Supermarket! How can I help ?')

def show_option():
    """
    Display a menu of options for the user to choose from.
    """
    print("""
(1) I want to add an item
(2) I want to update an item
(3) I want to delete an item
(4) I want to reset all my transaction
(5) I want to review my purchase
(6) I want to pay my transaction
    """)
    print("Select one of the options above by entering a number", end=" ")

def show_add_input():
    """
    Collect user input to add a new item to the transaction.
    """
    new_items = {}
    while True:
        try:
            print("What is the name of the item you want to input?", end=" ")
            name = (input()).strip()
            print(f"How many {name} do you want to purchase?", end=" ")
            quantity = int(input())
            print(f"How much does {name} cost?", end=" ")
            price = int(input())

            new_items[name] = [quantity, price]

            print("""Do you want to add another item? 
- Type 'Y' to add another item
- Press any other key to continue""", end=" ")
            another_item = (input()).lower()

            if another_item != 'y':
                break
        except:
            print("There is something wrong with your input. Make sure quantity and price are numbers.")

    transaction.add_item(new_items)

def show_update_input():
    """
    Collect user input to update an existing item in the transaction.
    """
    while True:
        print("Which item do you want to change?", end=" ")
        name_item = input()
        print(f"""
    (1) I want to update the name of {name_item}
    (2) I want to update the quantity of {name_item}
    (3) I want to update the price of {name_item}
        """)
        print("Select one of the options above by entering a number", end=" ")   
        selected_option = input()

        try:
            if selected_option == '1':
                print("What is the new item name?", end=" ")   
                new_name_item = input()
                transaction.update_item_name(name=name_item, new_name=new_name_item)
            elif selected_option == '2':
                print(f"What is the new quantity of {name_item} that you desire?", end=" ")   
                new_quantity = int(input())
                transaction.update_item_qty(name=name_item, new_quantity=new_quantity)
            elif selected_option == '3':
                print(f"What is the new price of {name_item} that you desire?", end=" ")   
                new_price = int(input())
                transaction.update_item_price(name=name_item, new_price=new_price)
            else:
                print('I believe you chose the wrong option. Please try again!')

            print("""Do you want to update another item? 
- Type 'Y' to update another item
- Press any other key to continue""", end=" ")
            another_item = (input()).lower()

            if another_item != 'y':
                break
        except:
            print("There is something wrong with your input. Make sure quantity and price are numbers.")

def show_delete_input():
    """
    Collect user input to delete an existing item from the transaction.
    """
    print("Which item do you want to delete?", end=" ")
    name_item = input()
    print(f"Are you sure you want to delete {name_item}? This process cannot be undone (Type 'Y' to delete)", end=" ")
    confirm = (input()).lower()

    if confirm == 'y':
        transaction.delete_item(name_item)

def reset_transaction_input():
    """
    Collect user input to reset all items in the transaction.
    """
    print("Are you sure you want to reset all transactions? (Type 'Y' to reset)", end=" ")
    confirm = (input()).lower()

    if confirm == 'y':
        transaction.reset_transaction()

while True:
    show_option()
    
    selected_option = input()
    if selected_option == '1':
        show_add_input()
    elif selected_option == '2':
        show_update_input()
    elif selected_option == '3':
        show_delete_input()
    elif selected_option == '4':
        reset_transaction_input()
    elif selected_option == '5':
        transaction.check_order()
    elif selected_option == '6':
        transaction.total_price()
        break
    else:
        print('I believe you chose the wrong option. Please try again!')
