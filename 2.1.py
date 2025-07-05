def format_number(number, format_type):
    formatted = format(number, format_type)
    return formatted
result = format_number(145, 'o')
print("The number 145 in octal format is:", result)
print("We used 'o' as the format type, which stands for 'octal' (base 8 number system).")
