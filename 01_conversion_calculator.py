# Function to generate decorated headings
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")

# Display instructions
def instructions():
    statement_generator("Instructions", "-")
    print(
        """
Instructions:
- Enter the amount you want to convert.
- Enter the unit you are converting from.
- Enter the unit you want to convert to.
- You can only convert within the same category (e.g., mass to mass).

Available Units:
- Distance: mm, cm, m, km (millimetres, centimetres, metres, kilometres)
- Mass: mg, g, kg, t (milligrams, grams, kilograms, tonnes)
- Time: s, min, h, d (seconds, minutes, hours, days)
    """
    )
statement_generator("The Conversion Calculator", "-")

# Display instructions if requested
want_instructions = input("\nPress <enter> to read the instructions or any key to continue: ")
if want_instructions == "":instructions()

# Display instructions
def instructions():
    statement_generator("Instructions", "-")
    print(
        """
Instructions:
- Enter the amount you want to convert.
- Enter the unit you are converting from.
- Enter the unit you want to convert to.
- You can only convert within the same category (e.g., mass to mass).

Available Units:
- Distance: mm, cm, m, km (millimetres, centimetres, metres, kilometres)
- Mass: mg, g, kg, t (milligrams, grams, kilograms, tonnes)
- Time: s, min, h, d, y (seconds, minutes, hours, days, years)
    """
    )

# Check that the input is in the dictionary
def unit_checker(question):
    while True:
        unit = input(question)
        if unit in distance_dict or unit in mass_dict or unit in time_dict:
            return unit
        else:
            print("Invalid unit! Please enter the abbreviation (Check available units in instructions).  ")

# Number checker that checks if the input is valid and higher than 0
def num_checker(question):
    while True:
        user_input = input(question).lower().strip()

        # Check if the user wants to exit
        if user_input =="xxx":
            return "xxx"

        try:
            response = float(user_input)
            if response > 0:
                return response
            else:
                print("Please enter a number higher than 0")
        except ValueError:
                print("Please enter a valid number or 'xxx' to quit.")

# Main Routine:
# Dictionary of supported units with their category and base unit factors
distance_dict = {
    "mm" : 0.001,
    "cm" : 0.01,
    "m"  : 1.0,
    "km" : 1000,
}
mass_dict = {
    "mg" : 0.001,
    "g"  : 1.0,
    "kg" : 1000,
    "t"  : 1000000.0,
}
time_dict = {
    "ms"  : 1/60000,
    "s"   : 1/60,
    "min" : 1.0,
    "h"   : 60.0,
    "d"   : 1440,
    "y"   : 525600.0,
}

# Main loop
while True:
    statement_generator("Unit Converter", "-")

# Get the amount and if "xxx" is entered, break
    amount = num_checker("\nPlease enter the amount to convert: ")
    if amount == "xxx":
        
        break

    # Get the from_unit and to_unit
    from_unit = unit_checker("Enter the current unit: ").lower()
    to_unit = unit_checker("Enter the unit to convert to: ").lower()

    # Check which dictionary the unit is from and convert
    if from_unit in distance_dict and to_unit in distance_dict:
        base_amount = amount * distance_dict[from_unit]
        answer = base_amount / distance_dict[to_unit]
        print(f"\nResult: {amount} {from_unit} = {answer} {to_unit}")

    elif from_unit in mass_dict and to_unit in mass_dict:
        # Convert to base unit (grams), then to target unit
        base_amount = amount * mass_dict[from_unit]
        answer = base_amount / mass_dict[to_unit]
        print(f"\nResult: {amount} {from_unit} = {answer} {to_unit}")

    elif from_unit in time_dict and to_unit in time_dict:
        # Convert to base unit (seconds), then to target unit
        base_amount = amount * time_dict[from_unit]
        answer = base_amount / time_dict[to_unit]
        print(f"\nResult: {amount} {from_unit} = {answer} {to_unit}")

    else:
        print(
            "\nError: Invalid units or converting across different categories."
        )

# Ask if user wants to keep going or quit
    keep_going = input("\nPress <enter> to convert another amount, or any key to quit: ")
    if keep_going != "":
        break

print("\nThank you for using the Ultimate Conversion Calculator! ")