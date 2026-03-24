import random

def grades(score1, score2, score3):
    score = (score1 + score2 + score3) / 3
    if score >= 90 and score <= 100:
        print("Your grade is A+")
    elif score >= 80 and score < 90:
        print("Your grade is A")
    elif score >= 70 and score < 80:
        print("Your grade is B")
    elif score >=60 and score < 70:
        print("Your grade is C")
    elif score >=50 and score < 60:
        print("Your grade is D")
    elif score >=40 and score <50:
        print("Your grade is E")
    elif score >=0 and score <40:
        print("Better luck next time!")
    else:
        print("Invalid score! Please enter a score between 0 and 100.")

score1, score2, score3 = random.randint(0,100), random.randint(0,100), random.randint(0,100)
print(f"Score 1: {score1}")
print(f"Score 2: {score2}")
print(f"Score 3: {score3}")
print("Your average score is:", (score1 + score2 + score3) / 3)
grades(score1, score2, score3)
