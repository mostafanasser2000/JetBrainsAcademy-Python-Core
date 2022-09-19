import random  # Stage2


def create_random_equation():
    random.seed()
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operator = random.choice(["*", "+", "-"])
    print(f'{num1} {operator} {num2}')
    return calc(num1, num2, operator)


def create_random_square():
    random.seed()
    num = random.randint(11, 29)
    print(num)
    return num ** 2


def calc(num1, num2, operator):
    result = 0
    if operator == '+':
        result = int(num1) + int(num2)
    elif operator == '-':
        result = int(num1) - int(num2)
    elif operator == '*':
        result = int(num1) * int(num2)
    return result


def get_valid_number():
    while True:
        try:
            number = int(input())
            return number
        except ValueError:
            print("Incorrect format.")


def save_result(user_name, answers, level):
    results = open("results.txt", "a")
    if results is None:
        results = open("results.txt", "w")
    description = ""
    if level == 1:
        description = "simple operations with numbers 2-9"
    else:
        description = "integral squares 11-29"

    record = f'{user_name}: {answers}/5 in level {level} ({description}).'
    results.write(record)
    results.close()


print("Which level do you want? Enter a number:")
print("""1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")

level = get_valid_number()
while level not in [1, 2]:
    level = get_valid_number()

correct_answers = 0
answer = None
for i in range(5):
    if level == 1:
        answer = create_random_equation()
    else:
        answer = create_random_square()
    user_answer = get_valid_number()
    if user_answer == answer:
        print("Right!")
        correct_answers += 1
    else:
        print("Wrong!")

print(f"Your mark is {correct_answers}/5.")
print("save the result? Enter yes or no.")
ans = input()
if ans.lower() in ["yes", "y"]:
    name = input("What is your name?\n")
    save_result(name, correct_answers, level)
    print('The results are saved in "results.txt".')




