from random import randint
from random import choices
from collections import Counter
from time import sleep


def wheel(spin):
    spin = randint(1, 5)
    print("You spun a " + str(spin))
    sleep(1)
    return spin


def chance(bet, guess, balance, result, spin):
    playerReturn = {"green": 1.3,
                    "yellow": 2.1,
                    "blue": 3.7,
                    "red": 8.5}
    win = playerReturn[guess] * bet * int(result[guess])
    wrong = spin - result[guess]
    loss = wrong * bet
    total = balance + win - loss
    print("You lost $" + str(loss))
    sleep(1)
    print("You won $" + str(win))
    sleep(1)
    print("Your total balance is now $" + str(total))
    result = {"lost": loss,
              "won": win,
              "balance": total}
    return result


def colourInput(colour):
    if colour == "Y" or colour == "y":
        guess = "yellow"
        return guess
    elif colour == "G" or colour == "g":
        guess = "green"
        return guess
    elif colour == "B" or colour == "b":
        guess = "blue"
        return guess
    elif colour == "R" or colour == "r":
        guess = "red"
        return guess
    else:
        colour = input("Choose either (Y) (G) (B) or (R)")
        return colourInput(colour)


def numCheck(num, name):
    if num.isnumeric():
        numInt = int(num)
        if numInt != 0:
            return numInt
        else:
            num = input("Your " + name + " has to be greater than zero")
            return numCheck(num, name)
    else:
        num = input("Your " + name + " has to be a whole number")
        return numCheck(num, name)


def wagerInput(wager, balance):
    if wager > balance:
        again = input("Try again, you can't bet more than you have!")
        wager = numCheck(again, "bet")
        return wagerInput(wager, balance)
    elif wager == balance:
        print("OK, All in!")
        sleep(1)
        return wager
    else:
        return wager


def start():
    money = input("What is your balance?")
    balance = numCheck(money, "balance")
    return balance


def restart(balance):
    while True:
        addBalance = input("Do you want to add to your balance? (Y/N)")
        if addBalance == "Y" or addBalance == "y":
            added = input("How much?")
            total = numCheck(added, "added amount") + balance
            return total
        elif addBalance == "N" or addBalance == "n":
            return balance
        print("Please enter either (N) or (Y)")


def repeat():
    colour = input("What colour Do you want to bet? (Y) (G) (B) (R)")
    guess = colourInput(colour)
    wager = input("How much do you bet on it?")
    wager = numCheck(wager, "bet")
    bet = wagerInput(wager, balance)


def begin(balance, spin):
    colour = input("What colour Do you want to bet? (Y) (G) (B) (R)")
    guess = colourInput(colour)
    wager = input("How much do you bet on it?")
    wager = numCheck(wager, "bet")
    bet = wagerInput(wager, balance)
    spin = wheel(spin)
    sample = choices(marbles, prob, k=spin)
    result = Counter(sample)
    print("Green:" + str(result["green"]))
    sleep(1)
    print("Yellow:" + str(result["yellow"]))
    sleep(1)
    print("Blue:" + str(result["blue"]))
    sleep(1)
    print("Red:" + str(result["red"]))
    answer = chance(bet, guess, balance, result, spin)
    balance = answer["balance"]
    return [balance, guess, bet, spin, result, answer]


spin = 0

marbles = ["green", "yellow", "blue", "red"]

prob = [0.4, 0.3, 0.2, 0.1]


def rules():
    print("The rules are simple:")
    sleep(1)
    print("You begin by depositing a balance, from which you bet from")
    sleep(2)
    print("Then you can choose any of the four coloured marbles each with different frequencies and return per dollar:")
    sleep(2)
    print("{Colour (Frequency, Return rate)}")
    sleep(1)
    print("Green (40%, 130%)")
    sleep(1)
    print("Yellow (30%, 210%)")
    sleep(1)
    print("Blue (20%, 370%)")
    sleep(1)
    print("Red (10%, 850%)")
    sleep(1)
    print("After that, the wheel spins between 1 and 3 for the number of marbles you can choose")
    sleep(2)
    print("For every marble you choose that is a different colour from your original bet...")
    sleep(2)
    print("you will lose the amount you bet for the round")
    sleep(2)
    print("But for every marble you choose that is the same colour as the colour you guessed...")
    sleep(2)
    print("you will gain the amount you bet multiplied by the return rate of your bet")
    sleep(2)
    print("This does mean that you may end up in debt to the house...")
    sleep(2)
    print("Let's Begin")
    sleep(2)


rules()

deposit = start()


while True:
    answer = begin(deposit, spin)
    balance = answer[0]
    while True:
        playAgain = input("Do you want to play again? (Y) (N)")
        if playAgain in ("y", "n", "Y", "N"):
            break
        print("Please enter either (Y) or (N)")
    if playAgain == "Y" or playAgain == "y":
        print("Values for this round (send them to me please): ")
        print("Starting balance: " + str(deposit))
        print("guess: " + str(answer[1]))
        print("bet amount: " + str(answer[2]))
        print("spin: " + str(answer[3]))
        print("result: " + str(answer[4]))
        print("win: " + str(answer[5]["won"]))
        print("loss: " + str(answer[5]["lost"]))
        print("Ending balance: " + str(answer[5]["balance"]))
        deposit = restart(balance)
    elif playAgain == "N" or playAgain == "n":
        playAgain = False
        print("Values for the last round (send them to me please): ")
        print("Starting balance: " + str(deposit))
        print("guess: " + str(answer[1]))
        print("bet amount: " + str(answer[2]))
        print("spin: " + str(answer[3]))
        print("result: " + str(answer[4]))
        print("win: " + str(answer[5]["won"]))
        print("loss: " + str(answer[5]["lost"]))
        print("Ending balance: " + str(answer[5]["balance"]))
        break