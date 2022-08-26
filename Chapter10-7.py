"""

Answer to question 10.7

We have 4B non-negative integers. There is a total of 2^31 possible non-negative integers, which
is 2B, which means there are duplicates.
We will create a bit vector with the 1GB memory that we have, which will have 8 bits * 1B = 8B bits.
Each of the values in it will be 0 (at initialization).
We will go through the input, and for each integer n we will set the bit vector at index n to be 1 (turned on).
Then we will go through the entire vector and return the index of the first 0.

Time complexity: O(n) while n is the number of integers in the input, in this case 4B.

FOLLOWUP

This time we only have 80M bits, and up to 1B unique non-integer values in the input.
We will create a bit vector with 80M boolean values, initializing all of them to 0.
We will then go over all of the integers in the input and store 1 at the indices in the vector that
correspond to integers 1 through 80M. Then we will go over the entire vector and look for a 0.
If we can find a 0, return it and finish. Otherwise repeat the process with the range shifted,
this time from 80,000,001 through 160M, and so on.
At some point we are guaranteed to find a 0 in the bit vector, which represents an integer that did not
show up in the input.

Time complexity: O(n) too (we do more passes potentially, but up to 13).

"""
