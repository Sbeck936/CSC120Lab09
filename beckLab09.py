string = str(input("Enter a string:"))
my_dict = {}

for i in range(len(string)):
    my_dict[i] = string[i]
print("length of dictionary", len(my_dict))

key_input = int(input("Enter a integer:"))
if key_input in my_dict:
    result = my_dict.get(key_input, string[key_input])
    print(result)
else:
    print("Error: Key not found")

value_input = input("Enter value")
if value_input in my_dict.values():
    print("value found")
else:
    print("value not found")

add_value = input("Enter a value to add to the dictionary")
newEntry = {len(string): add_value}
my_dict.update(newEntry)
print(my_dict)

remove_value = int(input("Enter a key to remove a value"))
my_dict.pop(remove_value)
print(my_dict)

name = "beck"
my_dict[len(my_dict)] = name
print(my_dict)

digit_string = input("Enter a series of digits separated by commas")
digit_list = digit_string.split(',')
empty_string = ''
for digit in digit_list:
    digit = int(digit)
    if digit in my_dict.keys():
        empty_string = empty_string + my_dict[digit]
    else:
        empty_string = empty_string + '*'
print(empty_string)







