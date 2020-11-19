from random import randint
from random import choices
from collections import Counter

totLoss = 0
totWin = 0
totDifference = 0
totSpin = 0
totGreen = 0
totYellow = 0
totBlue = 0
totRed = 0
tots = 0
data = []
for x in range(0, 1000):
    marbles = ["green", "yellow", "blue", "red"]
    prob = [4, 3, 2, 1]
    rand = randint(1, 4)
    if rand == 1:
        colour = "green"
    elif rand == 2:
        colour = "yellow"
    elif rand == 3:
        colour = "blue"
    elif rand == 4:
        colour = "red"
    else:
        print("something went wrong")
    spin = randint(1, 4)
    sample = choices(marbles, prob, k=spin)
    result = Counter(sample)
    playerReturn = {"green": 1.3,
                    "yellow": 2.1,
                    "blue": 3.7,
                    "red": 8.5}
    win = playerReturn[colour] * result[colour]
    loss = spin - result[colour]
    difference = win - loss
    answer = {"loss": loss,
              "win": win,
              "difference": difference,
              "spin": spin,
              "colour": colour,
              "result": result}
    totLoss = totLoss + answer["loss"]
    totWin = totWin + answer["win"]
    totDifference = totDifference + answer["difference"]
    totSpin = totSpin + answer["spin"]
    totGreen = totGreen + result["green"]
    totYellow = totYellow + result["yellow"]
    totBlue = totBlue + result["blue"]
    totRed = totRed + result["red"]
    data.append(difference)
    tots += 1
    x += 1

frequency = Counter(data)
print(frequency)
print(sum(frequency.values()))

total = {"loss": totLoss,
         "win": totWin,
         "difference": totDifference,
         "spin": totSpin,
         "green": totGreen,
         "yellow": totYellow,
         "blue": totBlue,
         "Red": totRed}

average = {"loss": totLoss / totSpin,
           "win": totWin / totSpin,
           "difference": totDifference / tots,
           "spin": totSpin / tots,
           "green": totGreen / totSpin,
           "yellow": totYellow / totSpin,
           "blue": totBlue / totSpin,
           "Red": totRed / totSpin}
print(str(average))
print(tots)