import string

# helper messages
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]


def is_one_digit(v):  # is one digit function
    if v.is_integer() and -10 < v < 10:
        return True
    return False


def check(v1, v2, v3):  # check function
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and (v3 in ["*", "-", "+"]):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)

# function to check if the input number is valid number or M (for memory) 
# this function will exclude invalid number like strings and symbols
def is_valid_number(number):
    if number == "M":
        return True
    if number[0] not in string.digits and number[0] != '-':
        return False
    cnt_periods = 0
    for i in range(1, len(number)):
        if number[i] == '.' and cnt_periods <= 0:
            cnt_periods += 1
        elif number[i] not in string.digits:
            return False
    return True

# function that force user to enter a valid input
def get_valid_input():
    print(msg_0)
    calc = input()
    x, operation, y = calc.split()

    while not (is_valid_number(x) and is_valid_number(y)):
        print(msg_1)
        print(msg_0)
        calc = input('')
        x, operation, y = calc.split()
        while operation not in ['+', '-', '*', '/']:
            print(msg_2)
            print(msg_0)
            calc = input()
            x, operation, y = calc.split()
            if not (is_valid_number(x)) or not (is_valid_number(y)):
                break
    return [x, operation, y]

# calculator function
def calculator():
    answer_1 = ""
    _memory = 0
    result = 0
    answer_1 = ""
    _memory = 0
    
    while answer_1 != "n":
        x, operation, y = get_valid_input()
        while True:
            if x == "M":  
                x = _memory  # give x memory value if it's equal M
            if y == "M":
                y = _memory  # give y memory value if it's equal M

            x = float(x)  # convert x to float type
            y = float(y)  # convert y to float type

            check(x, y, operation)  # run check function
            if operation == "+":
                result = x + y
                print(result)
                break
            elif operation == "-":
                result = x - y
                print(result)
                break
            elif operation == "*":
                result = x * y
                print(result)
                break
            else: 
                if int(y) == 0:  # if y == 0 in case of division force user to enter a valid equation
                    print(msg_3)
                    x, operation, y = get_valid_input()
                    continue
                result = x / y
                print(result)
                break

        store_1 = ""  # ask user if he wants to store the result of calculation or not
        while store_1 != "y" and store_1 != "n":  # loop until user enter y or n
            print(msg_4)
            store_1 = input()
        
        if store_1 == "y":
            store_2 = ""
            if is_one_digit(result):
                msg_index = 10
                while store_2 != "y" and store_2 != "n":
                    print(msg_[msg_index])
                    store_2 = input()
                    if store_2 == "y":
                        if msg_index < 12:
                            msg_index += 1
                            store_2 = "c"
                        else:
                            _memory = result
                            break
                    elif store_2 == "n":
                        break
            else:
                _memory = result

        answer_1 = ""  # ask user if he wants to continue the calculations or not
        while answer_1 != "y" and answer_1 != "n":
            print(msg_5)
            answer_1 = input()


calculator()
