"""

Answer to Question 6.6

- Looking at the case where C=1, if only one person has blue eyes, they will look at all the others,
and knowing that one person at least must have blue eyes they will deduce it is them and leave the same night.

- Regarding C=2, if only two people have blue eyes, each of them looks at the other blue-eyed person
and say 'I don't know if they are the only blue-eyed or not, so I will wait'. If they see them the next day,
they can assume the other person is not the only blue-eyed person or else they would have left.
So they deduce that they are the other person with blue eyes and leave the next day.

- Regarding C=n, this property is still true. All these people will wait for the n-th day to leave,
and if no one has left prior to that they can deduce that they have to leave on that day because there
are n blue-eyed people on the island, and they are one of these people.

In general, all people with blue eyes will leave on the same day, but will just wait until the n-th day to do so.

"""
