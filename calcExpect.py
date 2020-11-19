def frequency1(probWin, probLose, x):
    probW = {"freq": (probWin / 4) * probWin,
             "value": 1 * x + (-1) * 0}

    probL = {"freq": (probLose / 4) * probWin,
             "value": 0 * x + (-1) * 1}

    return [probW, probL]


def frequency2(probWin, probLose, x):
    prob2L = {"freq": ((probLose ** 2) / 4) * probWin,
              "value": 0 * x + (-1) * 2}

    probLW = {"freq": ((probLose * probWin * 2) / 4) * probWin,
              "value": 1 * x + (-1) * 1}

    prob2W = {"freq": ((probWin ** 2) / 4) * probWin,
              "value": 2 * x + (-1) * 0}

    return [prob2L, probLW, prob2W]


def frequency3(probWin, probLose, x):
    prob3L = {"freq": ((probLose ** 3) / 4) * probWin,
              "value": 0 * x + (-1) * 3}

    prob2LW = {"freq": ((probLose ** 2 * probWin * 3) / 4) * probWin,
               "value": 1 * x + (-1) * 2}

    probL2W = {"freq": ((probLose * probWin ** 2 * 3) / 4) * probWin,
               "value": 2 * x + (-1) * 1}

    prob3W = {"freq": ((probWin ** 3) / 4) * probWin,
              "value": 3 * x + (-1) * 0}

    return [prob3L, prob2LW, probL2W, prob3W]


def frequency4(probWin, probLose, x):
    prob4L = {"freq": ((probLose ** 4) / 4) * probWin,
              "value": 0 * x + (-1) * 4}

    prob3LW = {"freq": ((probLose ** 3 * probWin * 4) / 4) * probWin,
               "value": 1 * x + (-1) * 3}

    prob2L2W = {"freq": ((probLose ** 2 * probWin ** 2 * 6) / 4) * probWin,
                "value": 2 * x + (-1) * 2}

    probL3W = {"freq": ((probLose * probWin ** 3 * 4) / 4) * probWin,
               "value": 3 * x + (-1) * 1}

    prob4W = {"freq": ((probWin ** 4) / 4) * probWin,
              "value": 4 * x + (-1) * 0}

    return [prob4L, prob3LW, prob2L2W, probL3W, prob4W]


freqGreen = [frequency1(0.4, 0.6, 1.3), frequency2(0.4, 0.6, 1.3), frequency3(0.4, 0.6, 1.3), frequency4(0.4, 0.6, 1.3)]

freqYellow = [frequency1(0.3, 0.7, 2.1), frequency2(0.3, 0.7, 2.1), frequency3(0.3, 0.7, 2.1),
              frequency4(0.3, 0.7, 2.1)]

freqBlue = [frequency1(0.2, 0.8, 3.7), frequency2(0.2, 0.8, 3.7), frequency3(0.2, 0.8, 3.7), frequency4(0.2, 0.8, 3.7)]

freqRed = [frequency1(0.1, 0.9, 8.5), frequency2(0.1, 0.9, 8.5), frequency3(0.1, 0.9, 8.5), frequency4(0.1, 0.9, 8.5)]

totalFreq = [freqGreen, freqYellow, freqBlue, freqRed]

totalEX = 0

totalProb = 0

greenEX = 0

greenProb = 0

yellowEX = 0

yellowProb = 0

blueEX = 0

blueProb = 0

redEX = 0

redProb = 0


for a in totalFreq:
    for b in a:
        for c in b:
            totalProb = totalProb + (c["freq"])
            totalEX = totalEX + (c["value"] * c["freq"])

for a in freqGreen:
    for b in a:
        greenEX = greenEX + (b["value"] * b["freq"])
        greenProb = greenProb + (b["freq"])

for a in freqYellow:
    for b in a:
        yellowEX = yellowEX + (b["value"] * b["freq"])
        yellowProb = yellowProb + (b["freq"])

for a in freqBlue:
    for b in a:
        blueEX = blueEX + (b["value"] * b["freq"])
        blueProb = blueProb + (b["freq"])

for a in freqRed:
    for b in a:
        redEX = redEX + (b["value"] * b["freq"])
        redProb = redProb + (b["freq"])

print("Green Expected Value: " + str(greenEX))
print("Green Frequency: " + str(greenProb))
print("Yellow Expected Value: " + str(yellowEX))
print("Yellow Frequency: " + str(yellowProb))
print("Blue Expected Value: " + str(blueEX))
print("Blue Frequency: " + str(blueProb))
print("Red Expected Value: " + str(redEX))
print("Red Frequency: " + str(redProb))


print("Total Expected Value: " + str(totalEX))
print("Total Frequency: " + str(totalProb))