This is an explanation of the mathematics Behind the Calc python program and its calculation of expected value.


The program runs functions that calculate every possible outcome along with its absolute return value and its probability.
Because each colour has a different probability, return rate, etc., they are all calculated separately. Traditionally, expected value would be calculated by multiplying the amount gain of an outcome multiplied by its probability of occurring and subsequently adding up the resulting values together. The program works in the same way. By spinning a one for example, there are only two possible outcomes; the colour picked corresponds with your bet or it doesn't (Win or Lose). For a spin of two there are three outcomes: lose twice, win once and lose once, or win twice. You can spin up to a four resulting in a total of 14 possible outcomes for every colour. Each colour will have the same 14 outcomes, just with differing probabilities and absolute return values. So a function is sent a colour's specific probability of being picked, not getting picked, and return rate. Then it calculates the colour's expected values through it. By repeating this process over for every colour, the program then adds up all expected values to result at the total expected value.

Proof Checking:
There are two necessary and sufficient conditions that the program would have to fulfil to prove that it functions at intended.
Firstly: The sum of all 56 outcomes must have a result of 1.
Secondly: The sum of each colour's 14 outcomes must be equal to the colour's holistic probability

In order to test these conditions, I set the program to output the sum of all the outcome's frequencies as well as the sum of all of a colour's frequencies.

Program Result:
Green Expected Value: -0.07999999999999992
Green Frequency: 0.39999999999999997
Yellow Expected Value: -0.05249999999999995
Yellow Frequency: 0.3
Blue Expected Value: -0.029999999999999933
Blue Frequency: 0.20000000000000004
Red Expected Value: -0.012499999999999987
Red Frequency: 0.1
Total Expected Value: -0.17499999999999977
Total Frequency: 0.9999999999999999

As we can see, the total frequency rounds to 1, which fulfils the first condition. The frequency of each colour also round to the player's probability of picking the colour, which fulfils the second condition. Thus, it can be said that the program (calcExpect.py) works as it should.


From this, I am able to prove the following simplified E(X) equation:

R ( W ) + ( −1 * ( L )) = 1 - E(X)

R: Return Rate
W: Win probability
L: Lose probability
E(X): Expected value


By inputting the values for green, I get the same result as shown in the program:
1.3 ( 0.4 ) + ( −1 * ( 0.6 )) = 1 - E(X)
E(X) = -0.08

This equation works regardless of which colour's values are inputted.