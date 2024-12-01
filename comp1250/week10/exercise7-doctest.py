import re
def task6(first_name, last_name):
    """
    returns flip first name and last name
    >>> task6("Philip", "Ranillo")
    'Ranillo,Philip'
    """
    return last_name + "," + first_name

def task5(postal_code):
    """
    checking if the postal code is correct format
    >>> task5("abc")
    False
    """
    pattern = r'^[a-zA-Z][0-9][a-zA-Z] [0-9][a-zA-Z][0-9]$'
    if re.match(pattern, postal_code):
        return True
    return False

def task4(num1, num2):
    """
    if the first number a factor of second number
    >>> task4(15,5)
    True
    """
    if num1%num2 ==0:
        return True
    else:
        return False

def task3():
    """
    printing and return
    >>> task3()
    Philip Bezalel Asher
    'Last Name: Ranillo'
    """
    print("Philip Bezalel Asher")
    return "Last Name: Ranillo"

def task2(text, num):
    """
    printing and checking if the input is correct
    >>> task2('Hello', -2)
    False
    >>> task2('World', 5)
    'WorldWorldWorldWorldWorld'
    """
    if not isinstance(text, str) or not isinstance(num, int) or num < 2:
        return False
    else:
        return text * num

def task1(arg1, arg2, arg3):
    """
    prints out the argument data type
    >>> task1(1, "hi", 1.1)
    ('int', 'str', 'float')
    """
    return type(arg1).__name__, type(arg2).__name__, type(arg3).__name__
