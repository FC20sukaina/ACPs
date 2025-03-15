def sumOfTupleItems(numTuple):
    tupleSum = 0
    for tup in numTuple:
        tupleSum = tupleSum + tup
    return tupleSum
    
numTuple = (16, 31, 24, 98, 123, 78, 56, 67, 72)
print("Tuple items = ", numTuple)

tSum = sumOfTupleItems(numTuple)
print("/n The sum of numTuple Tuple items = ", tSum)