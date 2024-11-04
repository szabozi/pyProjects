import random

"""
Calculations
"""


def calculation(user_math_operator: str, user_practice_count: int) -> list[str]:
    user_count = user_practice_count
    user_math = user_math_operator
    random_number_a = random.randint(1, 9)
    random_number_b = random.randint(1, 9)
    results_list = []

    for number in range(user_count):
        if user_math == '+':
            calculation_result = int(input(f"{random_number_a} + {random_number_b} = "))
            if calculation_result == (random_number_a + random_number_b):
                print("Correct!")
                results_list.append(f'{random_number_a} + {random_number_b} = {calculation_result} CORRECT!')
            else:
                print("Incorrect..")
                results_list.append(f'{random_number_a} + {random_number_b} = {calculation_result} INCORRECT..')

    return results_list


userMathChoise = ''
userPracticeCount = 0

while True:
    try:
        userMathChoise = str(input("What do you want to practice (type: +, -, * , /): "))
    except ValueError:
        if userMathChoise != '+' or userMathChoise != '-' or userMathChoise != '*' or userMathChoise != '/':
            print(f"Wrong input for math operator: '{userMathChoise}'")

    try:
        userPracticeCount = int(input("How many times do you wish to practice that math operation: "))
    except ValueError:
        print(f"Input {userPracticeCount} invalid. Not a number (integer).")

    break


practice_results = calculation(user_math_operator=userMathChoise, user_practice_count=userPracticeCount)
print("Here are your results:")
for results in practice_results:
    print(results)


