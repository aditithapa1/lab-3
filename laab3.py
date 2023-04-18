# Initialize an empty dictionary to store the shopping cart
shoppingCart = {}

# Function to add a product to the shopping cart
def add_product():
    if len(shoppingCart) >= 5:
        print("Cart is full")
    else:
        num_items = int(input("Enter number of items to be added: "))
        if num_items + len(shoppingCart) > 5:
            print("Cart is full, can only add up to {} items".format(5 - len(shoppingCart)))
        else:
            for i in range(num_items):
                product_name = input("Enter product name: ")
                brand_name = input("Enter brand name: ")
                shoppingCart[product_name] = brand_name
                print("Product added to cart successfully!")

# Function to search a product in the shopping cart
def search_product():
    product_name = input("Enter product name: ")
    if product_name in shoppingCart:
        print("Product: {}, Brand: {}".format(product_name, shoppingCart[product_name]))
    else:
        print("No product exists with this name")

# Function to delete a product from the shopping cart
def delete_product():
    if len(shoppingCart) == 0:
        print("Cart is empty, no item is found")
    else:
        product_name = input("Enter product name: ")
        if product_name in shoppingCart:
            del shoppingCart[product_name]
            print("Product deleted from cart successfully!")
        else:
            print("Product not found in the cart")

# Main loop for the menu-driven program
while True:
    print("WELCOME TO THE AMANDO SHOPPING SITE")
    print("1. Add product to the cart.")
    print("2. Search the product.")
    print("3. Delete the product from the cart.")
    print("4. Quit.")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        add_product()
    elif choice == '2':
        search_product()
    elif choice == '3':
        delete_product()
    elif choice == '4':
        print("Thank you for using the AMANDO SHOPPING SITE!")
        break
    else:
        print("Invalid choice, please try again.")
