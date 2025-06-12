#This file will demonstrate lists in python
def main():
    #We don't want to do this
    #name1 = "John"
    #name2 = "mary"

    #create a list of names
    names = ["John", "Mary", "Alice", "Bob"]
    list_of_integers = [10, 16, 24, 42, 14, 9]
    random_datatype_list = ["Cyd", 15, 22.3, "Frank"]

    print(names)

    #add an item to the names list
    names.append("Jane")
    list_of_integers.append(5)
    list_of_integers.append(32)

    print(names)
    print(list_of_integers)

    #get the number of items in a list
    print("\nNumber of items in the names list")
    number_of_items = len(names)
    print(f"Number of items in names list: {number_of_items}")

    #Get the values from our list
    #get the first value from the list of integers
    print(f"\nFirst item in integer list: {list_of_integers[0]}")

    #get the fourth value from the list of integers
    print(f"\nFourth item in integer list: {list_of_integers[3]}")

    #print all item from the list of integers
    print("\nInteger list items")
    for item in list_of_integers:
        print(item)

    print("\nInteger list items using the item indexes")
    #get the number of items in the integer list
    number_of_integer_items = len(list_of_integers)

    for index in range(number_of_integer_items):
        print(f"Item {index}: {list_of_integers[index]}")




main()