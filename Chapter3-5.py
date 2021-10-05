from collections import deque


def rearrange_stacks(orig_stack, tmp_stack, item):
    items_rem = 0
    while orig_stack[-1] < item:
        tmp_stack.append(orig_stack.pop())
        items_rem += 1
        if len(orig_stack) == 0:
            break
    orig_stack.append(item)
    for i in range(items_rem):
        orig_stack.append(tmp_stack.pop())


def sort(stack):
    ts = deque()
    if len(stack) < 2:
        return
    while len(stack) > 1:
        ts.append(stack.pop())
    while len(ts) > 0:
        next_item = ts.pop()
        if next_item < stack[-1]:
            stack.append(next_item)
        else:
            rearrange_stacks(stack, ts, next_item)



if __name__ == '__main__':
    stack = deque()

    stack.append(3)
    stack.append(1)
    stack.append(4)
    stack.append(5)
    stack.append(10)
    stack.append(2)
    stack.append(9)

    print(stack)
    print("\n")

    sort(stack)

    print(stack)
    print("\n")

    sec_stack = deque()
    sort(sec_stack)
    print(sec_stack)
    print("\n")

    third_stack = deque()
    third_stack.append(3)
    sort(third_stack)
    print(third_stack)
    print("\n")

    fourth_stack = deque()
    fourth_stack.append(3)
    fourth_stack.append(2)
    fourth_stack.append(1)
    sort(fourth_stack)
    print(fourth_stack)
    print("\n")

    fifth_stack = deque()
    fifth_stack.append(1)
    fifth_stack.append(2)
    fifth_stack.append(3)
    sort(fifth_stack)
    print(fifth_stack)
    print("\n")