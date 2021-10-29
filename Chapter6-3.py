"""

Answer to Question 6.3

A viable solution is not possible.

Each domino covers exactly 1 white square and 1 black square,
since two adjacent squares are always of different colors. Let's prove by contradiction.
Let's assume there is a viable solution. it means that 31 dominos cover exactly 31 black squares
and 31 white squares. It means that on the chessboard, there are exactly 1 black square and
1 white square left, which are the corner squares. However, the two diagonally opposite corner squares
are always of the same color in a chessboard, which means that actually those corner squares
are both of the same color. This contradicts what we found, therefore our assumption that
there is a viable solution is wrong.

"""