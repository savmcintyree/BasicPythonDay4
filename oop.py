
class Cart():
    def __init__(self):
        self.my_list= {}
        self.cart_inventory={'Apples','Oranges','Kiwis','Milk','Bread'}

    def welcome_screen(self):
        while True:
            user = input ('\nWelcome to Kroger!\nCurrent Stock: Apples, Oranges, Kiwis, Milk, Bread\nWould you like to: 1)Continue or 2)Quit?')
            if user == '1':
                self.options()
            if user == '2':
                self.quit()

    def add_item(self):
        print('\nWhat would you like to add to your cart?')
        item = input('\nEnter an item:')
        if item not in self.cart_inventory:
            print("\nNot in Inventory.")
        else:
            qnty = int(input('How many would you like?: '))
            if item in self.my_list:
                    self.my_list[item] += qnty
            else:
                 self.my_list[item] = qnty
            print('\nItem(s) successfully added')

    def remove_item(self):
        item = input('\nRemove an item: ')
        if item in self.my_list:
            qnty = int(input('How many would you like to remove?'))
            if qnty <= self.my_list[item]:
                self.my_list[item] -= qnty
                print('\nItem(s) successfully removed.')
            else:
                print('\nYou do not have that amount of selected item(s) in cart')
        else:
            print('\nYou do not have that item in your cart')

    def view_cart(self):
        print('\nCart Inventory: ')
        for item in self.my_list:
            print(f'\n{self.my_list[item]} {item}(s)')

    def checkout(self):
        while True:
            checkout = input ('\nWould you like to checkout? If so please 1) Continue with payment 2)Return to cart or 3) Quit\n')
            if checkout == '3':
                return self.quit()
            elif checkout == '2':
                return self.view_cart()
            elif checkout == '1':
                print('\nPayment successful. Have a nice day!\n')
                self.welcome_screen()

    def quit(self):
        print('\nSession has ended.\n')

    def options(self):
        while True:
            user = input('\n1)Add item \n2)Remove item \n3)View cart \n4)Checkout \n5)Quit')
            if user == '1':
                self.add_item()
            elif user == '2':
                self.remove_item()
            elif user == '3':
                self.view_cart()
            elif user == '4':
                self.checkout()
            elif user == '5':
                self.quit()
                break
            else:
                print('Invalid answer please try again')

User = Cart()
User.welcome_screen()
