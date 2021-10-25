"""

Answer to Question 5.5

It returns True if n is a power of 2 and False otherwise.

Explanation: It returns True if n has one or zero 1's and False otherwise.

The reason is that when we subtract 1 from n, the rightmost 1 gets flipped to 0,
and all the 0's to the right of it get flipped to 1's. If we AND the result with
n we get that in all the places where the original rightmost 1 was and to its right
the complete result will be 0's.

However, to the left of this 1, if we have only 0's then subtracting 0's
(because the number we subtract is 000...00001) will give us 0's in the result,
which will cause the total result to be 0 and give True.

But if we have one more 1, then subtracting 0 from it we will get a 1, and ANDing it with
another 1 in the original n we will get 1 in this place, which will return False.

So if we return True if n has only one 1, it means that n must be a power of 2 since all
of the numbers that adhere to this rule are 0, 1, 2, 4, 8, 16, and so on.

"""