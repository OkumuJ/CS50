from cs50 import get_int 

scores = []

for _ in range(5):
    score = get_int ("Scores: ")
    scores.append(score)
    
average = sum(scores)/ len(scores)
# print (f"Average: {average.3f}")
print (f"Average: {average}")