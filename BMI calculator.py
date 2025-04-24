def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt))
            if value < min_val or value > max_val:
                print(f"Please enter a value between {min_val} and {max_val}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid value.")

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!\n")

    weight = get_valid_input("Enter your weight in kilograms (20 - 300): ", 20, 300)
    height = get_valid_input("Enter your height in meters (1.0 - 2.5): ", 1.0, 2.5)

    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"BMI Category: {category}")
main()