user_text = input("Enter a text: ").lower()
vowels = ['a','e','i','o','u']
if user_text in vowels:
    print(f"{user_text} has a vowel")
else:
    print(f"{user_text} does not have vowel")