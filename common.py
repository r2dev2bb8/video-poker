from typing import Generic

# counts the highest duplicity reached 
# eg. countMaxOccurences(list("11222")) -> 3, countMaxOccurences(list("123")) -> 1
def countMaxOccurences(ilst: list) -> int:
    # Edge case
    if len(ilst) <= 1:
        return 1
    # Base case
    if len(ilst) == 2:
        return int(ilst[0] == ilst[1]) + 1
    # Count maximum duplicity of first character
    times = 1
    for i in range(2, len(ilst)):
        ocurrencesofi = ilst.count(ilst[0] * i)
        if ocurrencesofi == 0:
            break
        times = i
    # Get the highest between the current max duplicity and the max duplicity of
    # everything but the first character
    return max([times, countMaxOccurences(ilst[1:])])

# count number of pairs
def numPairs(ilst: list) -> int:
    pair = 0
    blacklist = []
    for c in ilst:
        # if the character isn't in blacklist
        # increment pair based upon whether there is a pair
        if c not in blacklist:
            haspair = ilst.count(c * 2) == 1
            pair += int(haspair)
            blacklist.append(c)
    # if there are 4 occurences of anything, should return 2
    for c in blacklist:
        if ilst.count(c*4) == 1:
            return 2
    return pair

# returns a generator; I don't know how to type annotate that
# format of (returned value, pass status)
def testCountMaxOccurences() -> Generic:
    tests = [
        list("1222331"),
        list("123421"),
        list("736122")
    ]
    expectedresults = [
        3,
        1,
        2
    ]

    for index, t in enumerate(tests):
        result = countMaxOccurences(t)
        yield result, result == expectedresults[index] 

def main():
    for ispass in testCountMaxOccurences():
        print(ispass)

if __name__ == "__main__":
    main()