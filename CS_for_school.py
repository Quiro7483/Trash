import random

att = 0
score = 0

while att != 10:
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 5)
    print(number_1, "*", number_2, "=", end=" ")
    result = int(input())
    att = att + 1
    if result == number_1 * number_2:
        score = score + 1
    else:
        print("Think a bit more")

print(score)
if score == 10:
    print("Great")
elif 8 <= score <= 9:
    print("Good")
elif 5 <= score <= 7:
    print("Ok")
else:
    print("Quite bad")