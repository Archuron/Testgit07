# main.py

import badgenius.app as assignment2  # Import the app module as assignment2

if __name__ == '__main__':
    original_string = "ABCD1234EFGH5678IJKL90MNOPQ12RSTU34VWXYZ56"

    # Reduce the string
    reduced_string = assignment2.reduce_to_20_characters(original_string)
    print("Reduced String:", reduced_string)

    # Convert it back to the original string
    converted_string = assignment2.convert_to_40_characters(reduced_string)
    print("Converted String:", converted_string)
