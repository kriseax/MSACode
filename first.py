# Print hello world to console
print("Hello World!")

#create a variable to store my name
first_name = "Kristofferson"

#print "My name is Kristofferson"
print("My name is", first_name)

#create a variable to store my last name
last_name = "Culmer"

#write a statement to display "My full name is firstname lastname"
print("My full name is", first_name, last_name, sep="---")

# varaibles to store your age, height, weight, and assign them values
age = 17
weight = 188.4
height = 74

#print a sentence with age, weight, height
print(f"My name is {first_name} {last_name}\nI am {age} years old and I weigh {weight}lbs")

age = "17"
#get and print the data type for age, weight, and height
print(type(age))
print(type(weight))
print(type(height))

#write 3 print statements using string interpolation (fstring) to print 
#descriptive sentences fotr the data types
#Variable age is an int
print(f"Variable age is a {type(age)}")
print(f"Variable weight is a {type(weight)}")
print(f"Variable height is a {type(height)}")

number_1 = 5
number_2 = 7
total = number_1 + number_2
print(f"Total: {total}")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"Total: {total}")





