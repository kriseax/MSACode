#Function to get the name of the season
#Input: (int)month_number
#Output: (string)name of the month
def get_season_name(month_number:int):
    if(month_number == 12 or month_number == 1 or month_number ==2):
        return "Winter"
    elif(month_number == 3 or month_number == 4 or month_number == 5):
        return "Spring"
    elif(month_number == 6 or month_number == 7 or month_number == 8):
        return "Summer"
    else:
        return "Fall"
    
def get_season_name_2(month_number:int):
    if month_number in [12, 1, 2]:
        return "Winter"
    elif month_number in [3, 4, 5]:
        return "Spring"
    elif month_number in [6, 7, 8]:
        return "Summer"
    else:
        return "Fall"


#Function to get the month number
#Input: None
#Output: (int)number of the month
def get_month_number():
    while True:
        try:
            month_number = int(input("Enter month number: "))
            if(month_number <= 0 or month_number > 12):
                print("ERROR: Enter a number between 1 -12")
                continue
            else:
                break
        except:
            print("ERROR: Enter a number")
            continue
    return month_number

def main():
    while True:
        #Call the get_month_number function to promt and get the month number from the user
        month_number = get_month_number()
        #Call the get_season_name function to get the name of the season
        #print the output
        season_name = get_season_name_2(month_number)
        print(f"It is {season_name}")

        #ask the user if they want to run the program again
        do_again = input("Would you like to run the program again? (Press y to continue): ")
        #if y or Y rerun the program, otherwise end the program
        if do_again == "Y" or do_again == "y":
            continue
        else:
            break

main()