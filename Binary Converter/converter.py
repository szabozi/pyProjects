"""
Given a list containing a binary representation of a anumber and an optional argument representing the base.
Convert the number to the specified base, if no base is specified the default to decimal, base 10.
Return the result as a string.
"""


def binary_converter(binary: list[int], base: str) -> str:
    # convert the binary list to a string
    binary_str = ''.join(str(bit) for bit in binary)

    # convert the binary string to decimal (base 10)
    decimal = int(binary_str, 2)

    # perform conversion based on the specified base
    if base == 'b':  # Binary
        result = binary_str
    elif base == 'o':  # Octal
        result = format(decimal, 'o')
    elif base == 'x':  # Hexadecimal
        result = format(decimal, 'x')
    else:  # Decimal (default)
        result = str(decimal)

    return result


binary_number = [0, 1, 0, 1, 0, 1, 1, 0]
binary_result = binary_converter(binary_number, base='b')
decimal_result = binary_converter(binary_number, base='d')
octal_result = binary_converter(binary_number, base='o')
hexadecimal_result = binary_converter(binary_number, base='x')

print("Binary: ", binary_result)
print("Decimal: ", decimal_result)
print("Octal: ", octal_result)
print("Hexadecimal: ", hexadecimal_result)
