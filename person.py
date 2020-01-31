import datetime 
from datetime import date 

class Person:
    def __init__(self, name, race, birthdate, heightInches, weightLbs):
        self.name = name
        self.race = race
        self.birthdate = birthdate
        self.heightInches = heightInches
        self.weightLbs = weightLbs
        self.age = self.getAge()
        self.isMinor = (self.age < 18) if True else False

    def __str__(self):
        return "Name: %s - Race: %s - Age: %d - Height: %d inches - Weight: %.1f lbs - Minor: %s" % (self.name, self.race, self.age, self.heightInches, self.weightLbs, self.isMinor)

    def getAge(self):
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day)) 
        return age 
    

people = []
minors = []
adults = []

people.append(Person("Chuck", "White", datetime.datetime(2005, 1, 21), 120, 150))
people.append(Person("Terry", "White", datetime.datetime(1960, 12, 31), 100, 200.53))
people.append(Person("Cameron", "White", datetime.datetime(2005, 2, 7), 100, 141.5))
people.append(Person("Terri", "White", datetime.datetime(1963, 12, 25), 90, 120.53))


def sortByName(person):
    return person.name

# testArray = ['Orange', 'Apple', 'Banana', 'Stawberry', 'Pear', 'Grape']
print("Unsorted: ", people)
for person in people:
    print(person)
people.sort(key=sortByName)
print("Sorted: ", people)

#Todo: Sort testArray

# for person in people:
#     if(person.isMinor):
#         minors.append(person)
#     else:
#         adults.append(person)

# print("Minors: ")
# for minor in minors:
#     print(minor)

# print("\nAdults:")
# for adult in adults:
#     print(adult)




