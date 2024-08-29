my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
first_three_string = my_string[:3] 
rest_string = my_string[3:]
new_string = rest_string + first_three_string
# Use a template literal to print the original and modified string in a descriptive phrase.
print("You misspelled", new_string, "it should be spelled",  my_string)


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
user_letter_count = int(input("Letters to be relocated: "))
user_removed_letters = my_string[:user_letter_count]
user_string_left = my_string[user_letter_count:]
user_new_string = user_string_left + user_removed_letters
print("You misspelled", user_new_string, "it should be spelled", my_string)
# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
user_letter_count = int(input("Letters to be relocated: "))
if user_letter_count < 0:
    print("Error, letter count needs to be greater than 0")
elif user_letter_count > len(my_string):
    user_letter_count = 3 
    print("Number greater than 10 was entered, your number was defaulted to 3 due to the error.")
    print("You misspelled", user_new_string, "it should be spelled", my_string)
else:   
    user_removed_letters = my_string[:user_letter_count]
    user_string_left = my_string[user_letter_count:]
    user_new_string = user_string_left + user_removed_letters
    print("You misspelled", user_new_string, "it should be spelled", my_string)