while True:
    try:
        temp = float(input("Enter the temperature in fahrenheit: "))
        celsius = (temp - 32) * 5/9
    except ValueError:
        print("Please only use numbers for your input. Try again. ")
    else:
        print(f"{temp} degrees Fahremheit is {celsius} degrees Celsius.")
    finally:
        print("Thank you for using the weather forecast application.")

