# Define a function named is_two. It should accept one input and return 
# True if the passed input is either the number or the string 2, False otherwise

def is_two(input):
    return input == 2 or input == '2'

print(is_two(2))
print(is_two(4))

# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

def is_vowel(input):
    vowels = 'aeiouAEIOU'
    return input in vowels

is_vowel('a')
is_vowel('c')

# Define a function named is_consonant. It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(input):
    return not is_vowel(input)

is_consonant('a')
is_consonant('c')

# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word if the word starts with a consonant.

def capitalize_consonant(input):
    vowels = 'aeiouAEIOU'
    if input and input[0] not in vowels:
        return input[0].upper() + input[1:]
    else:
        return input
    
capitalize_consonant('football')

capitalize_consonant('apple')

# Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip

def calculate_tip(tip_percentage, bill_total):
    if 0 <= tip_percentage <= 1:
        return tip_percentage * bill_total
    else:
        return "Invalid tip percentage"
    
calculate_tip(0.20, 67)

# Define a function named apply_discount. It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.

def apply_discount(original_price, discount_percentage):
    if 0 <= discount_percentage <= 1:
        return original_price - (original_price * discount_percentage)
    else:
        return "Invalid discount percentage"
    
apply_discount(56, 0.12)
apply_discount(145, 0.25)

# Define a function named handle_commas. It should accept a string 
# that is a number that contains commas in it as input, and return a number as output.

def handle_commas(number_str):
    
    number_str = number_str.replace(',', '')
    try:
        number = float(number_str)
        return number
    except ValueError:
        return "Invalid input"

handle_commas('2,333,444')

# Define a function named get_letter_grade. It should accept a number and 
# return the letter grade associated with that number (A-F).

def get_letter_grade(numerical_grade):
    if 90 <= numerical_grade <= 100:
        return 'A'
    elif 80 <= numerical_grade < 90:
        return 'B'
    elif 70 <= numerical_grade < 80:
        return 'C'
    elif 60 <= numerical_grade < 70:
        return 'D'
    elif  0 <= numerical_grade < 60:
        return 'F'
    else:
        return 'Invalid grade input'

get_letter_grade(78)
get_letter_grade(95)

# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

def remove_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return ''.join(char for char in input_string if char not in vowels)

remove_vowels('Data Science Codeup')

# Define a function named normalize_name. It should accept a string and return a 
# valid python identifier, that is: anything that is not a valid python identifier 
# should be removed leading and trailing whitespace should be removed everything 
# should be lowercase spaces should be replaced with underscores for example: Name will become name 
# First Name will become first_name % Completed will become completed

def normalize_name(input_string):
    
    normalized_string = input_string.strip().lower().replace(" ", "_")
    normalized_string = ''.join(char for char in normalized_string if char.isalnum() or char == '_')

    return normalized_string

normalize_name('Ryan Anthony Poole')

# Write a function named cumulative_sum that accepts a list of numbers and 
# returns a list that is the cumulative sum of the numbers in the list. cumulative_sum([1, 1, 1]) 
# returns [1, 2, 3] cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(numbers):
    cumulative = []
    total = 0
    
    for num in numbers:
        total += num
        cumulative.append(total)

    return cumulative

cumulative_sum([4,5,6,7])

# Create a function named twelveto24. It should accept a string in the format 
# 10:45am or 4:30pm and return a string that is the representation of the time 
# in a 24-hour format. Bonus write a function that does the opposite

def twelveto24(time_str):
    if time_str[-2:].lower() == 'am':
        if time_str[:2] == '12':
            return '00' + time_str[2:-2]
        else:
            return time_str[:-2]
    else:  
        if time_str[:2] == '12':
            return time_str[:-2]
        else:
            hour = int(time_str[:2]) + 12
            return str(hour) + time_str[2:-2]

twelveto24('07:30am')
twelveto24('07:30pm')

# Create a function named col_index. It should accept a spreadsheet 
# column name, and return the index number of the column. col_index('A') returns 1 
# col_index('B') returns 2 col_index('AA') returns 27

def col_index(column_name):
    column_name = column_name.upper()
    index = 0

    for char in column_name:
        index = index * 26 + (ord(char) - ord('A') + 1)

    return index

print(col_index('A'))
print(col_index('B'))
print(col_index('AZ'))

