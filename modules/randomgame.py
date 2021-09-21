from random import randint

answer = randint(1, 10)

def random_guess():
 while True:
    try:
        guess = input("guessa number 1 to 10 ")
        if 0 < int(guess) < 11:
            if int(guess) == answer:
                print("you are a genius")
                break
        else:
            print("Hey bozo! I said 1 to 10")
    except ValueError:
        print("Please enter a number")
        continue

random_guess()    
