# Ask the user for first number
# Ask user for second number
# Ask user for type of operation: add, subtract, multiply, or divide
# Perform calculation on both numbers
# Display result

def prompt(text):
    print(f"==> {text}")

def invalid_number(num_str):
    try:
        int(num_str)
    except ValueError:
        return True

    return False

prompt('Welcome to the Calculator!')

prompt('What is the first number?')
number1 = input()

while invalid_number(number1):
    print("That doesn't look like a valid number. Try again.")
    number1 = input()

prompt('What is the second number?')
number2 = input()

while invalid_number(number2):
    print("That doesn't look like a valid number. Try again.")
    number2 = input()

prompt("""What operation would you like to perform?
1) add 2) subtract 3) multiply 4) divide""")
operation = input()

while operation not in ['1', '2', '3', '4']:
    print("You must choose 1, 2, 3, or 4")
    operation = input()

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

print(f'The result is {output}')