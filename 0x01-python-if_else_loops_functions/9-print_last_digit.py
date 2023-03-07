#!/usr/bin/python3
def print_last_digit(number):
    str_num = str(abs(number))
    last_char = str_num[-1]
    print(int(last_char))
