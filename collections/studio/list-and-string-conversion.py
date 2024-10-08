proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.
for sublist in strings: 
    if ',' in sublist:
        print(sublist, 'is separated by comma')
    elif ';' in sublist:
        print(sublist,'is separated by semicolon') 
    elif ' ' in sublist:
        print(sublist, 'is separated by space')
    else:
        print('No separator found')
# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
for sublist in strings:
    if ',' in sublist:
        comma = sublist.split(',')
        comma.reverse()
        reversed_comma = ','.join(comma)
        print(reversed_comma)


# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
for sublist in strings:
    if ';' in sublist:
        semicolon = sublist.split(';')
        semicolon.reverse()
        reversed_semicolon = ';'.join(semicolon)
        print(reversed_semicolon)


# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
for sublist in strings:
    if ' ' in sublist:
        space = sublist.split(' ')
        space.reverse()
        reversed_space = ' '.join(space)
        print(reversed_space)


# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
for sublist in strings:
    if ', ' in sublist:
        comma = sublist.split(', ')
        comma.reverse()
        reversed_comma = ','.join(comma)
        print(reversed_comma)