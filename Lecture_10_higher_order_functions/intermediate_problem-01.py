# Extracting the highest/maximum number from the entire list

from functools import reduce

numbers = [25,656,5648,648,68421,6182,510]

maximum = reduce(lambda x,y : x if x>y else y, numbers)
print(maximum)


