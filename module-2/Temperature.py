def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

fahrenheit = celsius_to_fahrenheit(celsius)

def main():
    print("Temperature Converter: Celsius to Fahrenheit")
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()
