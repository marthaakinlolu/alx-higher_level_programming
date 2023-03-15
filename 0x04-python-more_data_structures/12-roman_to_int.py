#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        # Return 0 if the input is None or not a string
        return 0

    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Initialize the result to 0
    result = 0

    for i in range(len(roman_string)):
        # Get the integer value of the current Roman numeral
        current_value = roman_dict.get(roman_string[i])

        # If the next numeral is of greater value, subtract the current value
        if i < len(roman_string) - 1 and roman_dict.get(roman_string[i+1]) > current_value:
            result -= current_value
        else:
            result += current_value

    return result
