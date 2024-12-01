user_input = input("Enter a text: ")
# ask user for character
user_char = input("Enter a Character: ")
char_to_find = user_input.find(user_char)
print(char_to_find)
if char_to_find :
    print(f"The character {char_to_find} is found")
else:
    print(f"The character  {char_to_find} is not found")