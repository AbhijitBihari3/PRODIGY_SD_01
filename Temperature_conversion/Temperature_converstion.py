def celsius_to_fahrenheit(celsius):
   return celsius*9/5+32


def celsius_to_kelvin(celsius):
   return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
   return (fahrenheit-32)*5/9


def fahrenheit_to_kelvin(fahrenheit):
   return (fahrenheit-32)*5/9+273.15


def kelvin_to_celsius(kelvin):
   return kelvin-273.15


def kelvin_to_fahrenheit(kelvin):
   return (kelvin-273.15)*1.8+32



def main():
    try:
        temperature = float(input("Enter the temperature: "))
        temperature_unit = input("Enter the unit (celsius, kelvin, fahrenheit): ")

        if temperature_unit == 'celsius':
            fahrenheit = celsius_to_fahrenheit(temperature)
            kelvin = celsius_to_kelvin(temperature)
            print(f"{temperature} Celsius is {fahrenheit:.2f} Fahrenheit and {kelvin:.2f} Kelvin")

        elif temperature_unit == 'fahrenheit':
            celsius = fahrenheit_to_celsius(temperature)
            kelvin = fahrenheit_to_kelvin(temperature)
            print(f"{temperature} Fahrenheit is {celsius:.2f} Celsius and {kelvin:.2f} Kelvin")

        elif temperature_unit == 'kelvin':
            celsius = kelvin_to_celsius(temperature)
            fahrenheit = kelvin_to_fahrenheit(temperature)
            print(f"{temperature} Kelvin is {celsius:.2f} Celsius and {fahrenheit:.2fr̥} Fahrenheit")

        else:
            print("Invalid unit. Please enter celsius, kelvin, or fahrenheit.")

    except ValueError:
        print("Invalid input. Please enter a valid temperature.")

if __name__ == "__main__":
    main()






