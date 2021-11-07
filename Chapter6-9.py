"""

Answer to Question 6.9

Insights:
- All of the prime numbers doors will get closed once when we start with them
- Every door is toggled when we reach its divider, so when the number of dividers
(including 1 and itself) is even, it ends up closed, if odd it ends up open
- The only numbers with an odd number of dividers are perfect square roots, because
their dividers can be paired, except for their square root which pairs with itself,
giving us an odd number overall. For example, for 16, we have (1,16), (2,8), (4,4).
So we have the dividers 1,2,4,8,16 - and therefore the door will be left open

- Hence the answer is 10 doors will be left open - 1, 4, 9, 16, 25, 36, 49, 64, 81, 100.

"""
