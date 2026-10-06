import json

cities = {
    "Kolkata": 15000000,
    "Delhi": 33000000,
    "Mumbai": 21000000
}

with open("FileHandling/Cities.json", "w") as f:
    json.dump(cities, f, indent=2)

with open("FileHandling/Cities.json", "r") as f:
    cities = json.load(f)

print("Cities and populations:")
for city, population in cities.items():
    print(f"{city}: {population}")

new_city = input("\nEnter a new city: ")
new_population = int(input("Enter population: "))

cities[new_city] = new_population

with open("FileHandling/Cities.json", "w") as f:
    json.dump(cities, f, indent=2)

print("\nCity added successfully!")