# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart, Store

site_name = "Mood"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    for store in stores:
        print(store)
    

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    for store in stores:
        if store.name == store_name:
          return store
    return False

def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    print_stores()
    my_store = input("Pick a store by typing its name. Or type 'checkout' to pay your bills.")
    if my_store =='checkout':
        #my_store.pick_products()
        return 'checkout'

    elif get_store(my_store):
        return get_store(my_store)
    else:
        print("We don't have a store with that name!")

def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    picked_store.print_products()


    my_product = input("What would you like to add to the cart? ")
    while my_product.lower() != 'back':
        for product in picked_store.products:
            if product.name == my_product:
                cart.add_to_cart(product)

        my_product = input("What else would you like? ")

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    store = pick_store()
    #pick_store()
    while store != 'checkout':
        pick_products(cart, store)
        store = pick_store()
            
    cart.checkout()

def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
