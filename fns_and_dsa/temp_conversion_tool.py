FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
  """
  Convert a temperature from Fahrenheit to Celsius.
  """
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
  """
  Convert a temperature from Celsius to Fahrenheit.
  """
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
  """
  Main function to prompt user input and perform temperature conversion.
  """
  while True:
    try:
      # Prompt the user for temperature
      temperature = float(input("Enter the temperature to convert: "))
      break  # Exit the loop if valid input is received

    except ValueError:
      # Handle non-numeric input
      print("Invalid temperature. Please enter a numeric value.")

  # Prompt the user for the unit
  unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

  if unit == "C":
    # Convert Celsius to Fahrenheit
    converted = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {converted:.2f}°F")
  elif unit == "F":
    # Convert Fahrenheit to Celsius
    converted = convert_to_celsius(temperature)
    print(f"{temperature}°F is {converted:.2f}°C")
  else:
    # Invalid unit input
    raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
  main()