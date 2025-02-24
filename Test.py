print("test")

'''
x 10 
c 100 
m 1000
4x4m3c

4300

40 4000 300

3X

3C3X4

334

0 to 10,000

9M3C4X4

9344

9X9M9C9X9

9999

34X

iterate from last 
if integer append maintain a digit place like oneth, tenth, hundereth 
else if char check the prev char as well 

if 4th place then simply you expect x and some digit add to the result
'''

def convert_to_number(input_str):
    # Mapping of characters to their respective multipliers
    multiplier_map = {
        'M': 1000,
        'C': 100,
        'X': 10
    }
    
    # Initialize result
    result = 0
    
    # Temporary variable to hold the current number
    current_number = 0
    
    for char in input_str:
        if char.isdigit():
            # Build the current number
            current_number = current_number * 10 + int(char)
        elif char in multiplier_map:
            # Apply the multiplier and add to the result
            result += current_number * multiplier_map[char]
            current_number = 0  # Reset for the next number
        else:
            raise ValueError(f"Invalid character '{char}' in input")
    
    # Add any remaining number at the end (no multiplier)
    result += current_number
    
    return result

# Examples
print(convert_to_number("9M3C4X4"))  # Output: 9344
print(convert_to_number("34X"))      # Output: 340
print(convert_to_number("9X9M9C9X9"))      # Output: 340

