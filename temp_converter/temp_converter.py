#!/usr/bin/python3

"""
Author: Armaan Khan
Course Number: Csc-138
Date: 2024-09-17
Class Section: EN


# Function to convert Fahrenheit to Celsius using the correct formula
def f2c(f):
    """
    Convert Fahrenheit temperature to Celsius using the correct formula.
    
    Parameters:
    f (float): Temperature in Fahrenheit.
    
    Returns:
    float: Temperature in Celsius.
    """
    return (f - 32) * 5 / 9

# Main function to demonstrate conversion
def main():
    f = 100 # Fahrenheit temperature to convert
    c = f2c(f)  # Convert Fahrenheit to Celsius
    print(f"{f}F is {c:.2f}C")  # Output the temperature in Celsius

# Incorrect conversion function for demonstration purposes
def f2c_raw(f):
    """
    Incorrect conversion function for Fahrenheit to Celsius.
    
    This function is incorrect and is provided for demonstration purposes only.
    """
    return f - 32 * 5 / 9

# Correct conversion function for Fahrenheit to Celsius
def f2c_op(f):
    """
    Correct conversion function for Fahrenheit to Celsius.
    
    Parameters:
    f (float): Temperature in Fahrenheit.
    
    Returns:
    float: Temperature in Celsius.
    """
    return (f - 32) * 5 / 9

if __name__ == "__main__":
    main()
