import sys

operation_symbols = ["+","-","*","/",""]
# 0: +
# 1: -
# 2: *
# 3: /

operation_combinations = []

# this reads the arguments from the command line
def read_arguments():
    arguments = sys.argv
    numbers = []
    for i in arguments[1:]:
        numbers.append(int(i))
    return numbers

def generate_number_combinations():
    global number_combinations
    number_combinations = []
    for i in numbers:
        for j in numbers:
            for k in numbers:
                for l in numbers:
                    for m in numbers:
                        for n in numbers:
                            if len({i, j, k, l, m, n}) == 6: # this removes any duplicates
                                number_combinations.append([i, j, k, l, m, n])

def generate_operation_combinations():
    operation_numbers = [0,1,2,3]
    for i in operation_numbers:
        for j in operation_numbers:
            for k in operation_numbers:
                for l in operation_numbers:
                    for m in operation_numbers:
                        operation_combinations.append([i,j,k,l,m])

def calc_result(number_arr, operation_arr):
    return eval(to_string(number_arr, operation_arr))

# adds the contents of numbers and operatons to the expression and then returns it
def to_string(number_arr,operation_arr):
    expression = ""
    for i in range(5):
        expression += str(number_arr[i]) + operation_symbols[operation_arr[i]] # convertind operation in numbers to symbol
    expression += str(number_arr[5])
    return expression

def verify_int(number): # was going to do more so made subroutine
    return number.isdigit()

def split_expression_into_steps(numbers, operators, steps):
    if len(numbers) == 1: # base case
        return steps
    i, operator = find_next_step(operators)
    i, numbers, operators, steps = combine(i, numbers, operators, steps, operator)

    return split_expression_into_steps(numbers, operators, steps)

def find_next_step(operators):
    # find first * or /
    for i, operator in enumerate(operators):
        if operator in [2,3]:
            return i, operator
    # then fall back on + or -
    for i, operator in enumerate(operators):
        if operator in [0,1]:
            return i, operator

def combine(i, numbers, operators, steps, operator):
    expression = str(numbers[i]) + operation_symbols[operator] + str(numbers[i + 1]) # making up expression with number before and after the operator
    result = eval(expression) # calculating result
    steps.append((expression, result)) # adding it to list
    operators.pop(i)  # removing completed operator
    numbers.pop(i)  # removing number
    numbers[i] = result # replacing second number with the result
    return i, numbers, operators, steps

generate_operation_combinations()

numbers = []
while 1:
    # if there is arguments and this is the first time it has run, then the arguments are read (Assumed to be correct for now)
    # if no arguments or not first time running, input is taken from user

    if numbers == [] and len(sys.argv) == 8:
        numbers = read_arguments()
        target = numbers.pop(-1)
    else:
        numbers = []
        print("----------------------------")
        for i in range(6):
            valid_input = False
            while not valid_input:
                inputted_number = input("Enter number " + str(i + 1) + ":\t")
                if verify_int(inputted_number):
                    numbers.append(int(inputted_number))
                    valid_input = True

        valid_input = False
        while not valid_input:
            inputted_number = input("Enter the target number: ")
            if verify_int(inputted_number):
                target = int(inputted_number)
                valid_input = True

    number_combinations = []
    generate_number_combinations()

    for numbers in number_combinations:
        for operators in operation_combinations:
            if calc_result(numbers,operators) == target:
                steps = split_expression_into_steps(numbers[:], operators[:], []) # this enters numbers and operators as copies os originals are not touched
                print("--------------------------")
                for expression, result in steps:
                    print(f"  {expression} = {result}")
