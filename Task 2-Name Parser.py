# day2_name_parser.py

# Function to clean and format names
def format_names(input_string):
    # Split input by commas
    names = input_string.split(",")
    
    # Clean each name: strip spaces and capitalize properly
    cleaned = [name.strip().capitalize() for name in names if name.strip()]
    
    # Remove duplicates by converting to set, then back to list
    unique_names = list(set(cleaned))
    
    return unique_names

# Ask user for comma-separated names
raw_input = input("Enter a comma-separated list of names: ")

# Process names using our function
names_list = format_names(raw_input)

# Display cleaned names separated by " | "
print(f"\nCleaned Names: {' | '.join(names_list)}")

# Show total number of unique names
print(f"Total unique names: {len(names_list)}")

# Bonus Features
if names_list:
    # Shortest and longest names
    shortest = min(names_list, key=len)
    longest = max(names_list, key=len)
    print(f"Shortest name: {shortest}")
    print(f"Longest name: {longest}")
    
    # Sort names alphabetically
    sorted_names = sorted(names_list)
    print(f"Alphabetical order: {', '.join(sorted_names)}")
    
    # Print names with index numbers
    print("\nNames with index:")
    for idx, name in enumerate(sorted_names, start=1):
        print(f"{idx}. {name}")
