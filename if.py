#creating a program that checks if a number is even 
num = 20 
if num % 2 == 0:
    print("number is even")
else: 
    print("number is odd")

# creating a program to check if someone is eligible to vote
age = 20 
is_citizen = False

if age >=18 and is_citizen == True: 
    print("they can vote")
else:
    print("you can't vote")
# Program that generates random number and has user guess what it is
random_num = random.randint(0, 100)
# update program to keep track of how many guesses user made and let them know at the end
while True:
    guess = int(input("guess a number \n"))
    if guess < random_num:
        print("the number you want is higher")
    elif guess > random_num:
        print("the number you want is lower")
    else:
        print("congrats you guessed it")
        break















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

