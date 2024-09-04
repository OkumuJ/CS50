people = [
    {"name": "John", "num": "+254-764-637-0017"},
    {"name": "Jack", "num": "+254-798-678-0677"},
    {"name": "Stephanie", "num": "+254-775-910-8737"},
    {"name": "Milka", "num": "+254-701-639-7108"},
    
]

name = input("Name: ")

for person in people:
    if person ["name"] == name:
        number = person["num"]
        print (f"Found{number}")
        break
else :
    print("Not found")