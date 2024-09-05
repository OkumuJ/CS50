import csv 


# Reading csv file in python  
# printing user the number of user for a specific languages in th csv file 

# Using one dictionary instead of many 
with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    count = {}


    for row in reader:
        favorite = row["language"]
        if favorite in count:
            count[favorite] += 1
            
        else: 
            count[favorite] = 1

for favorite in count:
    # check sorting on documentation
    print(f"{favorite}: {count[favorite]}")

    # most popula problem