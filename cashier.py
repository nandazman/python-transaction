import json
from tabulate import tabulate

class Transaction:
    """
    This class represents a transaction for a supermarket cashier system. Users can use this class to manage items in their transaction.

    Attributes:
    items (dict): A dictionary to store items in the transaction, where the keys are item names, and the values are dictionaries
                  containing 'quantity' and 'price' of the item in list format.

    Methods:
    - add_item(new_items): Add a new item to the transaction.
    - update_item_name(name, new_name): Update the name of an existing item in the transaction.
    - update_item_qty(name, new_quantity): Update the quantity of an existing item in the transaction.
    - update_item_price(name, new_price): Update the price of an existing item in the transaction.
    - delete_item(name): Delete an existing item from the transaction.
    - reset_transaction(): Delete all items from the transaction.
    - check_order(): Review the items in the transaction.
    - total_price(): Calculate the total price of the transaction with potential discounts.
    """

    def __init__(self):
        self.items = {}

    def add_item(self, new_items):
        """
        Add a new item to the transaction.

        Parameters:
        new_items (dict): new items consist dictionary that key as the name of item and value array
                        that have length 2. first index is quantity and second index is price.

        Returns:
        string: message with items that already stored and error if user has incorrect value
        """
        try:
            # store any error
            errors = []
            # store all corret format item
            success = {}
            if type(new_items) != dict:
                raise TypeError("format new items is not correct")
            
            for item in new_items:
                if item in self.items:
                    errors.append({
                        'item': item,
                        'reason': f"{item} already exist"
                    })
                    continue

                if type(new_items[item]) != list:
                    errors.append({
                        'item': item,
                        'reason': f"value of {item} is not quantity and price"
                    })
                    continue
                
                if len(new_items[item]) != 2:
                    errors.append({
                        'item': item,
                        'reason': f"value of {item} is not quantity and price"
                    })
                    continue
                
                quantity = new_items[item][0]
                if type(quantity) != int and type(quantity) != float:
                    errors.append({
                        'item': item,
                        'reason': f"quantity of {item} is not a number"
                    })
                    continue
                
                price = new_items[item][1]
                if type(price) != int and type(price) != float:
                    errors.append({
                        'item': item,
                        'reason': f"price of {item} is not a number"
                    })
                    continue

                self.items[item] = new_items[item]
                success[item] = new_items[item]
            
            print(f'new purchased items are: {json.dumps(success)}')
            if len(errors) > 0:
                print(f'fail purchased items are: {json.dumps(errors)}')
        except Exception as error:
            return print(error)
        

    def update_item_name(self, name, new_name):
        """
        Update the name of an existing item in the transaction.

        Parameters:
        name (str): The name of the item to be updated.
        new_name (str): The new name for the item.

        Returns:
        string: message with items that already updated
        """
        try:
            if name not in self.items:
                raise ValueError(f"cannot change name, {name} is not exist")

            self.items[new_name] = self.items[name]
            del self.items[name]
            print(f'updated purchased item from {name} to {new_name}')
        except Exception as error:
            return print(error)

    def update_item_qty(self, name, new_quantity):
        """
        Update the quantity of an existing item in the transaction.

        Parameters:
        name (str): The name of the item to be updated.
        new_quantity (int): The new quantity for the item.

        Returns:
        string: message with items that already updated
        """
        try:
            if name not in self.items:
                raise ValueError(f"cannot update quantity,{name} is not exist")

            prev_quantity = self.items[name][0]
            self.items[name][0] = new_quantity
            print(f'updated purchased item quantity {name} from {prev_quantity} to {new_quantity}')
        except Exception as error:
            return print(error)

    def update_item_price(self, name, new_price):
        """
        Update the price of an existing item in the transaction.

        Parameters:
        name (str): The name of the item to be updated.
        new_price (float): The new price for the item.

        Returns:
        string: message with items that already updated
        """
        try:
            if name not in self.items:
                raise ValueError(f"cannot update price {name} is not exist")

            prev_price = self.items[name][1]
            self.items[name][1] = new_price
            print(f'updated purchased item price {name} from {prev_price} to {new_price}')
        except Exception as error:
            return print(error)

    def delete_item(self, name):
        """
        Delete an existing item from the transaction.

        Parameters:
        name (str): The name of the item to be deleted.

        Returns:
        string: message with items that already updated
        """
        try:
            if name not in self.items:
                raise ValueError(f"cannot delete {name}, {name} is not exist")

            del self.items[name]
            print(f"new purchased item are {json.dumps(self.items)}")
        except Exception as error:
            return print(error)

    def reset_transaction(self):
        """
        Delete all items from the transaction.

        Returns:
        string: success message
        """
        self.items = {}
        print("All item has been deleted!")

    def check_order(self):
        """
        Review the items in the transaction.

        Returns:
        string: message with items that already stored
        """
        headers = ["No", "Name", "Quantitiy", "Price/Item", "Total Price"]
        table = []

        i = 0
        for item in self.items:
            i += 1
            quantity = self.items[item][0]
            price = self.items[item][1]
            total_price = quantity * price
            table.append([i, item, quantity, price, total_price])

        print(tabulate(table, headers, tablefmt="github"))

    def total_price(self):
        """
        Calculate the total price of the transaction with potential discounts.
        Discounts Rules:
        - If the total price is greater than or equal to 500.000, a 10% discount is applied.
        - If the total price is greater than or equal to 300.000, an 8% discount is applied.
        - If the total price is greater than or equal to 200.000, a 5% discount is applied.

        Returns:
        string: message with The total price after applying discounts.
        """
        MINIMUM_PRICE_TO_GET_DISCOUNT_FIVE_PERCET = 200_000
        MINIMUM_PRICE_TO_GET_DISCOUNT_EIGHT_PERCET = 300_000
        MINIMUM_PRICE_TO_GET_DISCOUNT_TEN_PERCET = 500_000

        total_price = 0
        for item in self.items:
            quantity = self.items[item][0]
            price = self.items[item][1]
            total_price += quantity * price
        
        if total_price < MINIMUM_PRICE_TO_GET_DISCOUNT_FIVE_PERCET:
            print(f'Total price that you have to pay is Rp. {total_price}')
            return
        
        discount = 0
        if total_price >= MINIMUM_PRICE_TO_GET_DISCOUNT_TEN_PERCET:
            discount = total_price * 0.1
        elif total_price >= MINIMUM_PRICE_TO_GET_DISCOUNT_EIGHT_PERCET:
            discount = total_price * 0.08
        else:
            discount = total_price * 0.05
        
        total_price_after_discount = total_price - discount
        print(f'Total price for all your purchase is Rp. {float(total_price)}')
        print(f'You got discount Rp. {discount} so you only have to pay Rp. {total_price_after_discount}')
        