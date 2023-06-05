#Jeremy is trying to make a number guessing game
#He wants to make the user guess a random number from 1 to 10
print("Hi! Welcome to my number guessing game")
number = random.randint(1,10)
print("Guess a number between 1 and 10, you'll have 3 chances")
chances = 3
victory = 0
while chances => 0 and victory = 0:
    try:
        guess = int.input()
    except:
        print("That's not a number. I'll put it as zero")
        guess == 0
    if guess == number:
        print("You got it right!")
        vicotry = 1
    elif guess > number
        print("Nope! That's too big!")
    else:
        print("Nope! That's too small!")
    chances = chances + 1
if victory == 0:
    print("Too bad! The number was" number)
else:
    print("Congratulations!")