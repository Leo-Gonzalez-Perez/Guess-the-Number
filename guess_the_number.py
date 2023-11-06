from random import randint

magic_nbr = randint(1, 101)
counter = 1
nbr = 0
name = input("Hi, your name?: ")

while counter < 9:
    print("----------------------------------------------")
    nbr = int(input("Between  1 y 100, What's the Magic Numbre?: "))
    if nbr not in range(1, 101):
        print("Your number is out of range")
    elif nbr < magic_nbr:
        print("Your number is less than Magic Number")
    elif nbr > magic_nbr:
        print("Your number is greater than Magic Number")
    else:
        break
    counter += 1

if nbr == magic_nbr:
    print("----------------------------------------------")
    print(f"You won {name}!!! in {counter} attempts")
    print(f"The Magic Number is: {magic_nbr}")
    print("End of game.")
elif nbr != magic_nbr:
    print("----------------------------------------------")
    print(f"You lost, {name}. The Magic Number was: {magic_nbr}")
    print("Game Over!")
print("----------------------------------------------")
