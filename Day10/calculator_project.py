import art
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multipy(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

operator = {
    '+':addition,
    '-':subtraction,
    '*':multipy,
    '/':divide,
}
# print(operator['-'](8, 2))
def calculator():
    print(art.logo)
    continued = True
    num1 = float(input("What is the first number?: "))

    while continued:

        for sym in operator:
            print(sym)
        symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        result = operator[symbol](num1, num2)

        print(f"{num1} {symbol} {num2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

        if choice == 'y':
            num1 = result
        elif choice == 'n':
            continued = False
            print('\n' * 20)
            calculator()
        else:
            print('Invalid command.')
            break


calculator()