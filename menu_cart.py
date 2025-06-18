"""
Function to load menu item and price into a dictionary
Input: (string)file_path
Output: (dictionary)menu 
"""
def get_menu_dictionary(file_name:str) -> dict:
    #open file.txt: create a file handler in read mode
    data_file = open("file.txt", "r")
    print(data_file)

    #create an empty dictionary to store item: price entries
    menu_items = {}

    #use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        #split the data ant the comma
        item_name_and_price = line_of_data.split(",")
        
        #get the menu item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        #create an entry in the dictionary for the item and price
        menu_items[item_name] = item_price
    
    data_file.close()
    return menu_items

def display_cart(cart:dict, menu_items:dict)->None:
    print("\nCart\n----")
    total = 0
    #loop through the cart to print the output
    for item, quantity in cart.items():
        total = total + (quantity * menu_items[item])
        print(f"{quantity} {item} @{menu_items[item]:.2f}: {quantity * menu_items[item]:.2f}")
    print(f"\nTotal: ${total:.2f}")

def main():
    menu_item = get_menu_dictionary("file.txt")
    #create a cart dictionary
    item_cart = {}

    while True:
        #prompt user for item
        item = input("\nItem: ")

        #determine if we need to end the program
        if item.lower() == "end":
            break

        #validate that item is in the menu_item dictionary
        if item not in menu_item:
            print(f"\nERROR: {item} not on the menu")
            continue

        #prompt user for quantity
        try:
            quantity = int(input("Quantity: "))
        except:
            print("\nERROR: enter number for quantity")
            continue

        #add item to cart. if item in cart already, quantity
        #if not in cart add item and quantity to cart
        if item not in item_cart:
            #create a new entry in the item_cart dictionary
            item_cart[item] = quantity
        else:
            #adds quantity to the value if the item's current quantity
            item_cart[item] += quantity

        #display total by calling the display cart function
        display_cart(item_cart, menu_item)

main()