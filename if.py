import random 




















#program that generates random number and has user guess what it is 

random_num = random.randint(0,100)
# update program to keep track of how many guesses user made and let them know 
while True: 
    guess = int(input("Guess a number between and 100: "))
    guess_count = 0 
    if guess < random_num:
     print("the number you want is higher") 
    elif guess > random_num:
        print("the number you want is lower")
    else: 
        print("congrats! you guessed it in {}")
    break 

