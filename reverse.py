# REVERSE NUMBERS
def remove_zeros(number):
    # Convert the number to a string to handle leading zeros
    number_str = str(number)
    # Remove leading zeros using lstrip
    result = number_str.lstrip('0')
    # If the result is an empty string, it means the number was zero
    return result
  

def reverse_number(number):
    # Convert the number to a string and reverse it
    zero_removed = remove_zeros(number)
    reversed_str = str(zero_removed)[::-1]
    # Convert the reversed string back to an integer
    reversed_number = reversed_str
    # Return the reversed number
    return reversed_number

# # Test cases
print(reverse_number(501))

