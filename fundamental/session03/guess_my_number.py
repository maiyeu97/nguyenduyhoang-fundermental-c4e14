from random import randint
number = randint(0, 100)
guess= True       #flag

# while guess_wrong:(while True:)
while True:
    guess = int(input("Nhap so ban doan(0 -100):"))
    if guess < number:
        print("bigger")
    elif guess > number:
        print("smaller")
    else:
        print("Bingo")
        # guess_wrong = False (break)
        break
