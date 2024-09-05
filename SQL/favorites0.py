import csv 


# Reading csv file in python  
# printing user the number of user for a specific languages in th csv file 
with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    scratch, c, python = 0, 0, 0

    for row in reader:
        favorites = row["language"]
        if favorites == "Scratch":
            scratch +=1
        elif favorites == "C":
            c += 1
        elif favorites == "Python":
            python += 1


print(f"Scratch: {scratch}")
print(f"C: {c}")
print(f"Python: {python}")