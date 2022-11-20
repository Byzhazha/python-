import time
import random
def divisible(n):
    list4 = []
    for h in range(1, 100):
        if n % h == 0:
            list4.append(h)
    return random.choice(list4)
right = 0
global i, accuracy
list1 = []
start = time.perf_counter()
sign_list = ["+", "-", "*", "/"]
for i in range(9999999):
    dif1 = 120 - (time.perf_counter() - start)
    if dif1 <= 60:
        break
    sign = random.choice(sign_list)
    num1 = random.randint(0, 100)
    if sign == "/":
        num2 = divisible(num1)
    else:
        num2 = random.randint(0, 100)
    print(f'{num1}{sign}{num2}=')
    number = eval(input())
    result2 = eval(f"{num1}{sign}{num2}")
    dif2 = 60 - (time.perf_counter() - start)
    if number == eval(f"{num1}{sign}{num2}"):
        print("Correct!Time remain {:.2f} seconds.".format(dif2))
        right += 1
    else:
        print("Wrong!Time remain {:.2f} seconds.".format(dif2))
    a = (f'{num1}{sign}{num2}=' + str(eval(f"{num1}{sign}{num2}")))
    list1.append(a)
accuracy = right / i * 100
print("{} questions and your correct rate is {}%".format(i, accuracy))
print("\n".join(list1))

