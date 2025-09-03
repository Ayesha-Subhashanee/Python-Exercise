#asks the user to enter the names of five cities one by oneand stores them into a list structure
cities = []
#Create a loop
for i in range(0, 5):
    city = input("Enter the name of a city: ")
    cities.append(city)

print("\n\nThe cities you entered:")
for city in cities:
    print(city)