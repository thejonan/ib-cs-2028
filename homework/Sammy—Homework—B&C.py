import random
#Check_Cow Function
def evaluate_guess(digits, code):
    evaluation = [0, 0, 0, 0]
    for i in range(len(digits)):
       if digits[i] == code[i] or digits[i] == code[i-1] or digits[i] == code[i-2] or digits[i] == code[i-3]:
           if digits[i] == code[i]:
               evaluation[i] = "Bull"
           else:
               evaluation[i] = "Cow"
       else:
           evaluation[i] = "Miss"
    return evaluation

code = random.sample(range(1, 10), 4)

win = False
while win == False:
    digits = [int(x) for x in input("Input a 4-digit number: ")]
    if evaluate_guess(digits, code) == ["Bull", "Bull", "Bull", "Bull"]:
        print(evaluate_guess(digits, code))
        print("You win the game")
        win = True
    else:
        print(evaluate_guess(digits, code))