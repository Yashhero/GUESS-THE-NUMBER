import random
import math
start = 1
end = 10
print("Guess a number between", start, "and", end)
x = random.randint(start, end)
print("\nYou have 4 chances to guess the correct number!\n")
count = 0
while count < math.log(end - start + 1, 2):
	count += 1
	guess = int(input("Guess a number:- "))
	if x == guess:
		print("Congratulations you did it in ",
			count," attempts!")
		break
	elif x > guess:
		print("Try a higher number")
	elif x < guess:
		print("Try lower number")
if count >= math.log(end - start + 1, 2):
	print("\nThe number is %d" % x)
	print("You just ran out of chances!\n")
