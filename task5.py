import csv
import json

names = ["Arun","Priya", "Rahul", "Divya", "Karthik"]

with open("names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")


print ("STUDENT NAMES:")
with open("names.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        print(number, line.strip())

students = [
    {"name": "Arun",  "marks": 55},
    {"name": "Priya", "marks": 60},
    {"name": "Rahul", "marks": 72},
    {"name": "Divya", "marks": 88},
    {"name": "Karthik", "marks": 45}
]

with open("students.csv", "w", newline="") as file:
    writer = csv.DictWriter(
        file, fieldnames=["name", "marks"]
    )
    writer.writeheader()
    writer.writerows(students)


    print("\nABOVE 60 MARKS:")
    with open("students.csv", "r") as file:
        reader = csv.DictReader(file)

        for student in reader:
            if int(student["marks"]) > 60:
                print(student["name"], student["marks"])


    with open("students.json", "w") as file:
        json.dump(students, file, indent=2)

        print("nJSON DATA:")

    with open("students.json", "r") as file:
        data = json.load(file)
        print(data)

        print("nMISSING FILE:")

    try:
         with open("missing.txt", "r") as file:
             print(file.read())

    except FileNotFoundError:
        print("missing.txt -> File not found")



                                
    




