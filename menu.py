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

def main():
    menu_item = get_menu_dictionary("file.txt")
    total = 0

    while True:
        #prompt user for item
        item = input("Item: ")

        #determine if we need to end the program
        if item.lower() == "end":
            break
        
        #get the item price and add to total
        #use try except to catch an error if the item is not in the dictionary
        try:
            total += menu_item[item.title()]
        except:
            continue

        #display total
        print(f"Total: ${total:.2f}")


main()