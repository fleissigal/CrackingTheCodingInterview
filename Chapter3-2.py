# Answer to question 3.2

"""
The stack will work in the following way: each node will keep, in addition to its value,
the value of the minimum node in the stack beneath it (including itself).
This way, to return the minimum we just return this additional saved value.

Push: we compare the minimum of the element below it with the new element, and update the min
for the new element. O(1)

Pop: We remove and return the element on top, no further action needed. The new min value is
already saved in the now most recent element. O(1)

Min: We return the min value that's saved with the most recent element. O(1)

"""