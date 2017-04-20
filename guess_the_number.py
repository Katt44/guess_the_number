#Pseudo code:
#part 1
# Set up conditonals to have the user guess a number
# I want to let the user when their number is to big or too small
#Part 2
# Set up  conditionals that the user guess a number that is randomly generated.
# part 3
# I want it to do part 1 but be able to take a range of numbers from user.


# Part 1


#secret_num = 23

#user_guess = int(raw_input("Guess a number between 1 and 25: "))

#if user_guess > secret_num:
#	print "Your number is too big!"
#elif user_guess < secret_num:
#	print "your number is too small!"
#elif user_guess == secret_num:
#	print "Yay thats the number!"
#else: 
#	print "Something went wrong!"



# Part 2

import random 
# how does this import work? importing from where?
user_name = raw_input("Hello there! Whats your name? ")
print "Hi " + user_name  + " We're gonna play a number guessing game!"
print "lets play!" # whats the syntax for  a string to break into a new line without creating a new print

number = random.randint(3,45)


for n in range(8): # why range 8?
	print "Okay" + user_name + " take a guess pick a number between 4 and 44"
	user_guess = int(raw_input("> "))

	if user_guess > number:
		print user_name + " your number is to big! Try again!"
	elif user_guess < number:
		print user_name + " your number is too small! Try again!"
	elif user_guess == number:
		print "You did it " + user_name + "! Good Job!"
		break
	else:
		print "Nope."
		print "Just nope. its fucked"









