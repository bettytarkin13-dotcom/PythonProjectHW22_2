#Bonus
#start
import random
import time

def get_random_between_1_10()->int:  # בוחרת מס אקראי בין 1-10
    return random.randint(1,10)
def get_random_operation()->str:  #בוחרת פעולה אקראית מתוך הרשימה
    return random.choice(["+","-","*","%"])

def calc_result(num1: int, operator: str, num2: int) -> int:
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "%":
            return num1 % num2

num1=get_random_between_1_10()
operator=get_random_operation()
num2=get_random_between_1_10()

result=calc_result(num1,operator,num2)
print("*****************************************************")
print("question:")
print(f"{num1} {operator} {num2}=?")
user_result=int(input("what the result is:"))

print("******************************************************")
time.sleep(5)

if user_result==result:
    print("correct!")
else:
    print(f"wrong..the answer was {result}")

#stop