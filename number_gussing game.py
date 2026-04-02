import random
number=random.randint(1,100)
guess=int(input("enter your guess: "))
counter=1
while guess!=number:
    if guess<number:
        print("too low")
    else:
        print("too high")
    guess=int(input("enter your guess: "))
    counter+=1
print(f"congratulations! you guessed the number in {counter} attempts.")
