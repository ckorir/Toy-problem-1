def solve(a):
    # Assign vowels
    vowels = "aeiou"
    consonant_values = {char: ord(char) - ord('a') + 1 for char in "abcdefghijklmnopqrstuvwxyz" if char not in vowels}

    def get_consonant_value(substring):
        return sum(consonant_values[char] for char in substring)
    
    max_value = 0
    current_consonant = ""

    for char in a:
        if char not in vowels:
            current_consonant += char
        else:
            max_value = max(max_value, get_consonant_value(current_consonant))
            current_consonant = ""

    # Check the last consonant substring if it's the highest
    max_value = max(max_value, get_consonant_value(current_consonant))

    return max_value

# Get user input
value = input("Enter a word in lowercase: ")

# Call function for calculating
result = solve(value)
print(f"Highest value of consonant is: {result}")

