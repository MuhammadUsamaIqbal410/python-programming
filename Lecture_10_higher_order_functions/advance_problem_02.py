# Converting the scores to percentage, eliminating the failed percentege, and then getting
# the average, highest and the lowest of all the grades using higher order function

from functools import reduce

scores = [102, 54, 98, 68,76, 97, 88]

percentage = list(map(lambda x : round((x/150) *100, 2), scores))
print(f"percentages : {percentage}")

passing = list(filter(lambda x : x >= 50, percentage))
print(f"Passing percentages are: {passing}")


def assign_grade(p):
    if p >= 90:   return f"{p}% → A"
    elif p >= 80: return f"{p}% → B"
    elif p >= 70: return f"{p}% → C"
    elif p >= 60: return f"{p}% → D"
    else:         return f"{p}% → F"

graded = list(map(assign_grade, passing))
print(f"Respective grades for passing percentages are: {graded}")

average = reduce(lambda x, y: x + y, passing) / len(passing)
print(f"Class Average   : {round(average, 2)}%")

highest = reduce(lambda x, y: x if x > y else y, passing)
print(f"Highest Score   : {highest}%")

lowest = reduce(lambda x, y: x if x < y else y, passing)
print(f"Lowest Passing  : {lowest}%")
