
def powerSet(s):

    currentSet = set()
    if len(s) == 0:
        return [currentSet]

    result = []
    auxPowerSet(s, result, currentSet)
    return result

def auxPowerSet(s, res, currSet):
    # Base case
    if len(s) == 0:
        res.append(currSet)
        return

    # Recursion
    nextElement = s.pop()
    auxPowerSet(s.copy(), res, currSet.copy()) # New set without the new element
    currSet.add(nextElement)
    auxPowerSet(s.copy(), res, currSet.copy()) # New set with the new element



if __name__ == '__main__':

    s0 = {3, 5, 1, 4}
    print(powerSet(s0))
    s0 = {}
    print(powerSet(s0))
    s0 = {2}
    print(powerSet(s0))
    s0 = {2, 19}
    print(powerSet(s0))
