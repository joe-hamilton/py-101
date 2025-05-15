import json

LANGUAGE = 'en'

with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(key):
    message = messages(key, LANGUAGE)
    print(f'==> {message}')

def invalid_number(num_str):
    try:
        float(num_str)
    except ValueError:
        return True

    return False

def messages(message, lang):
    return MESSAGES[lang][message]

prompt('welcome')

while True:
    prompt('first_number')
    number1 = input()

    while invalid_number(number1):
        prompt('invalid')
        number1 = input()

    prompt('second_number')
    number2 = input()

    while invalid_number(number2):
        prompt('invalid')
        number2 = input()

    prompt('perform_operation')
    operation = input()

    while operation not in ['1', '2', '3', '4']:
        print("You must choose 1, 2, 3, or 4")
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    print("The result is:", output)

    prompt('another_calculation')
    answer = input()

    if answer.lower() in ['y', 'yes']:
        continue
    else:
        break