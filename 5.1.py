import random

rolls = []
count_6 = 0
count_1 = 0
double_6 = 0

for i in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)
    if roll == 6:
        count_6 += 1
    if roll == 1:
        count_1 += 1

for i in range(len(rolls) - 1):
    if rolls[i] == 6 and rolls[i + 1] == 6:
        double_6 += 1

print("All rolls:", rolls)
print("Number of 6s:", count_6)
print("Number of 1s:", count_1)
print("Number of times two 6s came in a row:", double_6)
