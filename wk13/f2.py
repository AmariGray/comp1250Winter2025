def next_value_in_sequence(user_data: str)->str:
    """
    Determine what is the next value in sequence
    example: if the user_data is a number
             the next value should be number + 1

             if the user_data is a letter
             the next value should be the following letter

    :param user_data: a number or a letter
    :return: a string value presenting the next value

    >>> next_value_in_sequence('10')
    '11'
    >>> next_value_in_sequence('a')
    'b'
    >>> next_value_in_sequence('M')
    'n'

    """
    value_to_increase_by = 1
    if user_data.isdigit():
        converted = int(user_data)
        converted += value_to_increase_by
        next_value = str(converted)
    else:
        first_letter = user_data[0].lower()
        letter_as_number = ord(first_letter)
        if letter_as_number >= 97 and letter_as_number <= 122:
            letter_as_number += value_to_increase_by
            next_value = chr(letter_as_number)
        else:
            # IndexError  # for collections
            # IOError  # for files
            raise ValueError(f"{first_letter} is not inwithin range")
    return next_value
