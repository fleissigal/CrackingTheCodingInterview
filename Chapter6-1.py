"""

Answer to Question 6.1

We take pills from each bottle, i pills from the ith bottle, and put them all on the scale.
Then we find the heavy bottle's number with the following formula:

HB = (W - 210) * 10

Explanation: If all pills weighted 1.0 grams, then the scale would show 210 grams
since we are taking 210 pills in total (1 + 2 + 3 + ... + 20 = 210).
Now one bottle contributed more grams since its pills are heavier. And we can know
which one it is by the additional weight: bottle 1 contributed 1 pill, if it's the heavy bottle then
it contributed an additional 0.1 grams, so the total weight would be W = 210.1.
Bottle 2 contributed 2 pills, if it's the heavy bottle then it contributed an additional 0.1 + 0.1 grams,
so the total weight would be W = 210.2. And in general, let's denote the heavy bottle with i,
it contributed 0.1 * i grams, so the total weight would be W = 210 + i * 0.1. To get i we can
just use the formula above.

"""