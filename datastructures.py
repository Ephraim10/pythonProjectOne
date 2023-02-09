# TUPLES
cars = ("Mercedes", "Toyota", "BMW", "Audi", "Range")
print(cars[1])
print(cars[4])
print(cars[0:3])
for gari in cars:
    print(gari)
# LISTS
students = ["Dennis", "Leah", "Glory", "Elsy", "Walter", "Jared"]
students.append("Michelle")
students.append("Quinton")
students.append("Donald")
students[3] = "Wairimu"
print([1])
print([3])
print(students[2:4])
for std in students:
    print(std)
# DICTIONARIES
vehicles = {"V1": "BMW", "V2": "Ford", "V3": "Mitsubishi", "V4": "Probox"}
print(vehicles["V4"])
# printing all keys of a dictionary
for key in vehicles.keys():
    print(key)

# printing all the values of a dictionary
for value in vehicles.values():
    print(value)
