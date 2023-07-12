conversion_factors = {
  'meter': 1.0,
  'kilometer': 1000.0,
  'centimeter': 0.01,
  'inch': 0.0254,
  'foot': 0.3048,
  'mile': 1609.34,
  'kilogram': 1.0,
  'gram': 0.001,
  'pound': 0.453592,
  'ounce': 0.0283495,
  'liter': 1.0,
  'milliliter': 0.001,
  'gallon': 3.78541,
  'quart': 0.946353,
  'pint': 0.473176,
}


def convert_units(value, from_unit, to_unit):
  if from_unit == to_unit:
    return value

  if from_unit in conversion_factors and to_unit in conversion_factors:
    factor = conversion_factors[from_unit] / conversion_factors[to_unit]
    result = value * factor
    return result

  return None


def evaluate_result(result):
  if result is None:
    return False

  return True


def main():
  print("Welcome to the Unit Converter App!")

  value = float(input("Enter the value to convert: "))
  from_unit = input("Enter the unit to convert from: ")
  to_unit = input("Enter the unit to convert to: ")

  result = convert_units(value, from_unit, to_unit)
  valid = evaluate_result(result)

  if valid:
    print(f"{value} {from_unit} = {result} {to_unit}")
  else:
    print("Invalid units selected.")


if __name__ == '__main__':
  main()
