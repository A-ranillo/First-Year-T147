import re

text = " "
number = 1000
username = "admin"
userid = 12345
password = "a8e3l6$#"
email = "ex@ex.ex"

#Write the regular expression that will match the variable text content with an empty string
reg_empty = r'^[\s]$'
print("Task 2: ", bool(re.match(reg_empty, text)))

#Write the regular expression that will match the variable text content that has at least 10 characters
reg_min_10chars = r'^.{10,}+$'
print("Task 3: ", bool(re.match(reg_min_10chars, text)))

#Write the regular expression that will match the variable text with only non-alphanumerical characters.
reg_non_alphanumericalcar = r'^[\W]+$'
print("Task 4: ", bool(re.match(reg_non_alphanumericalcar, text)))

#Write the regular expression that will match the variable username with: Only alphabetical characters and underscores
reg_only_alpha = r'^[a-zA-Z_]+$'
print("Task 5: ", bool(re.match(reg_only_alpha, username)))

#Write the regular expression that will match the variable userid with only numeric characters
reg_only_digit = r'^[\d]+$'
print("Task 6: ", bool(re.match(reg_only_digit, str(userid))))

#Write the regular expression that will match the variable password with:
# At least 1 number
# At Least 1 alphabetic character
# At Least 1 special character (!”#$%&/)
reg_password = r'^(?=.*[0-9])(?=.*[a-zA-Z])(?=.*[!”#$%&/]).+$'
print("Task 7: ", bool(re.match(reg_password, password)))

# Write the regular expression that will match the variable email with a valid email. Please note that a valid email includes:
# At Least 1 alphabetic character before the at symbol
# Exactly 1 at symbol
# At Least 1 alphabetic character after the at symbol
# Exactly 1 period symbol
# At Least 1 alphabetic character after the period symbol
reg_email = r'[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$'
print("Task 8: ", bool(re.match(reg_email, email)))