# badgenius/app.py

# Create a dictionary to represent the substitution mapping
substitution_dict = {
    'aa': 'A', 'ab': 'B', 'ac': 'C', 'ad': 'D',
    'ba': 'E', 'bb': 'F', 'bc': 'G', 'bd': 'H',
    'ca': 'I', 'cb': 'J', 'cd': 'K', 'da': 'L',
    'db': 'M', 'dc': 'N', 'dd': 'O'
}

# Function to reduce a string into a 20-character string
def reduce_to_20_characters(original_string):
    reduced_string = ""
    for i in range(0, len(original_string), 2):
        pair = original_string[i:i + 2]
        reduced_string += substitution_dict.get(pair, '')  # Use the dictionary for substitution

    return reduced_string

# Function to convert a 20-character string back to the original string
def convert_to_40_characters(reduced_string):
    original_string = ""
    for i in range(0, len(reduced_string), 2):
        pair = reduced_string[i:i + 2]
        original_string += substitution_dict.get(pair, '')

    return original_string
