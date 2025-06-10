# Write a pounds to kilogram converter program
# A user will be prompted for their weight in pounds and the 
# program will output weight in kgs

#GET INPUT WEIGHT FROM THE USER
#convert weight to a float
#validate that weight is a number.
#if weight is not a number, reprompt the user until the input is correct
def get_positive_float_input():
    while True:
        try:
            user_weight = float(input("Enter your weight in pounds: "))
            #validate that user_weight is positive. If not positive, reprompt the user
            if user_weight <= 0:
                print("ERROR: Enter a value greater than 0")
                continue
            else:
                break
        except:
            print("ERROR: Please enter a number")
    
    return user_weight


def main():
    #get the weight from the user. Call the get_positive_float_input function
    user_weight = get_positive_float_input()

    #PROCESSING
    #use a conversion to convert lbs to kilos: 2.205 lbs = 1kg
    LBS_TO_KG_CONVERSION = 2.205
    user_weight_in_kg = user_weight / LBS_TO_KG_CONVERSION

    #OUTPUT
    #print the output to the user in a nice format to 2 decimal places
    print(f"You weigh {user_weight_in_kg:.2f}kgs.")

#call the main function
main()