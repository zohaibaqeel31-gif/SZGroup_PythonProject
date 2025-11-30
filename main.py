def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero.")
                else:
                    print(f"Result: {num1} / {num2} = {divide(num1, num2)}")

            next_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if next_calculation.lower() == "no":
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    calculator()




import random

def play_game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it.")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid whole number.")
            continue

        attempts += 1

        # Give feedback
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Great job! You guessed the number in {attempts} attempts.")
            break


def main():
    while True:
        play_game()

        # Ask if they want to play again
        answer = input("Would you like to play again? (yes/no): ").strip().lower()
        if answer not in ("yes", "y"):
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    main()
