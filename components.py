# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        self.products.append(product)

    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        for product in self.products:
            print(product)

    def __str__(self):
        return self.name


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        # your code goes here!
        return "%s, %s, %s" % (self.name, self.description, self.price)



class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        self.products = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        self.products.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        total = 0
        for product in self.products:
          total += product.price
        return total


    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        for product in self.products:
           print (product)
        print ("The total price is %s"% (self.get_total_price()))

    def checkout(self):
        """
        Does the checkout.
        """
        self.print_receipt()
        c = input("Confirm? (yes/no) :")
        if c.lower() == 'yes':
            print("Your order has been placed.")

        else:
            print("Your order has been canceled.")

        

