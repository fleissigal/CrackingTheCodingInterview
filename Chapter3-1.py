# Answer to question 3.1

"""
Assuming the length/size of the array is fixed, we would like to divide the array into 3 equal parts,
while each of these parts has its own space to act as a stack in the same way I implemented the stack
data structure using an array.

What happens when one of the stacks is full but needs to add another element?
In this case, we will make room for this new element by shifting the stack that comes after it (assuming
it has an empty cell at the end) by moving this entire stack's contents by one step and reducing its allocated
size by one cell. If this next stack is also full, we will shift the stack that comes after this
one (we assume there will be space somewhere in the array for the new element), including reducing
its size by one, and then shift the second stack which now has room to shift, in order to make room
for the original stack which got pushed a new element.

Another idea is to treat the array as a cycle, which makes it easier to shift stacks around (for example,
if the stack that comes first keeps being empty, we can "move" it forward and let the stack that comes
at the end use the first cell(s) of the array cyclically to store its contents, in case it get full.

As far as implementation, for the case where we would like to allocate each stack a fixed space, we
use the exact same implementation of stack that we did, with the following exceptions:
1. We now have 3 indices for each of the stacks.
2. All of the functions now get the stack number as an additional argument.
3. This time if a stack gets full (which we check), we simply return an exception rather than expanding
the stack.

"""