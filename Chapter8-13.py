import math


def stackOfBoxes(boxes):
    boxes = sortByHeight(boxes)
    heights = []
    auxStackOfBoxes(boxes, [math.inf, math.inf, math.inf], 0, heights)
    return max(heights)

def auxStackOfBoxes(boxes, lastEntered, totalHeight, heights):
    if len(boxes) == 0:
        heights.append(totalHeight)
        return

    if boxes[0][0] < lastEntered[0] and boxes[0][1] < lastEntered[1] and boxes[0][2] < lastEntered[2]:
        auxStackOfBoxes(boxes[1:], [boxes[0][0], boxes[0][1], boxes[0][2]], totalHeight + boxes[0][1], heights)

    auxStackOfBoxes(boxes[1:], lastEntered, totalHeight, heights)

def sortByHeight(boxes):
    return sorted(boxes, key=lambda x: x[1])[::-1]

# To improve this solution we can cache results that were already computed - using memoization
# And make sure that the insert and retrieve calls are symmetric


if __name__ == '__main__':
    print(stackOfBoxes([[8, 6, 2], [9, 3, 3], [10, 8, 4], [6, 1, 2]]))
    print(stackOfBoxes([[10, 8, 4], [6, 1, 2], [8, 1, 2], [3, 3, 3]]))
    print(stackOfBoxes([[12, 10, 4], [3, 3, 3], [10, 8, 4], [6, 1, 2], [8, 1, 2]]))