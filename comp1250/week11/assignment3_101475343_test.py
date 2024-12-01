def letters_extraction_o_machine(text):
    """
    >>> letters_extraction_o_machine("Numbers Are Overrated!")
    ('n', 'u', 'm', 'b', 'e', 'r', 's', 'a', 'o', 'v', 't', 'd')
    """
    result = "".join(char for char in text.lower() if re.match(r'[a-zA-Z]', char))
    holder = []
    for i in result:
        if i not in holder:
            holder.append(i)

    return tuple(holder)