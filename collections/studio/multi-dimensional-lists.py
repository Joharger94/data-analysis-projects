food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_cabinet =sorted(food.split(','))
equipment_cabinet = sorted(equipment.split(','))
pets_cabinet = sorted(pets.split(','))
sleep_aids_cabinet = sorted(sleep_aids.split(','))

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [food_cabinet, equipment_cabinet, pets_cabinet, sleep_aids_cabinet]
print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.

# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.

# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”

select_cargo_bin = int(input("Select cargo hold bin (0 - 3): "))
if select_cargo_bin < 0:
    print("Error, number choosen can not be negative")
elif select_cargo_bin > 3:
    print("Error, number choosen can not be higher than 3")
else:
    choosen_cargo_bin = cargo_hold[select_cargo_bin]
    print("The cargo hold contains:", choosen_cargo_bin)
    item_in_bin = input("Enter the item to search bin for: ")
    if item_in_bin in choosen_cargo_bin:
        print("Cabinet", select_cargo_bin, "does contain", item_in_bin)
    else:
        print("Cabinet", select_cargo_bin, "does not contain", item_in_bin)
        
def is_even(num): 
   return num % 2 == 0

num = 42
print(is_even(43))
def string_repeater(a_string):
   repeated = a_string + a_string
   print(repeated)

string_repeater('Bob')