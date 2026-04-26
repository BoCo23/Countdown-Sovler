operation_symbols = ["+","-","*","/",""]
# 1: +
# 2: -
# 3: *
# 4: /

operation_combinations = []

def generate_number_combinations():
    number_combinations_with_dups = []
    global number_combinations
    for i in numbers:
        for j in numbers:
            for k in numbers:
                for l in numbers:
                    for m in numbers:
                        for n in numbers:
                            if len({i, j, k, l, m, n}) == 6:
                                number_combinations_with_dups.append([i, j, k, l, m, n])
    # removing duplicates
    number_combinations = list({tuple(a) for a in number_combinations_with_dups})
    number_combinations = [list(a) for a in number_combinations]

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

def to_string(number_arr,operation_arr):
    sum = ""
    for i in range(5):
        sum += str(number_arr[i]) + operation_symbols[operation_arr[i]]
    sum += str(number_arr[5])
    return sum

def verify_int(number):
    return number.isdigit()

def split_sum_into_steps(numbers, operators, steps):
    for i,operator in enumerate(operators):
        print(operation_symbols[operator])
        if operator == 2 or operator == 3:
            i, numbers, operators, steps = combine(i, numbers, operators, steps, operator)
            if len(numbers) == 1:
                return steps
            split_sum_into_steps(numbers, operators, steps)

def combine(i, numbers, operators, steps, operator):
    sum = str(numbers[i]) + operation_symbols[operator] + str(numbers[i + 1])
    steps.update({sum: eval(sum)})
    operators.pop(i)  # removing completed operator
    numbers.pop(i)  # removing elements
    numbers.insert(i, steps[next(reversed(steps))])
    print(steps)
    return i, numbers, operators, steps
generate_operation_combinations()

while 1:
    numbers = []
    number_combinations = []
    steps = {}
    print("----------------------------")
    for i in range(6):
        valid_input = False
        while not valid_input:
            inputted_number = input("Enter number " + str(i+1) + ":\t")
            if verify_int(inputted_number):
                numbers.append(int(inputted_number))
                valid_input = True

    valid_input = False
    while not valid_input:
        inputted_number = input("Enter the target number: ")
        if verify_int(inputted_number):
            target = int(inputted_number)
            valid_input = True

    generate_number_combinations()

    for numbers in number_combinations:
        for operators in operation_combinations:
            if calc_result(numbers,operators) == target:
                print(to_string(numbers,operators))
                print(split_sum_into_steps(numbers,operators,steps))
