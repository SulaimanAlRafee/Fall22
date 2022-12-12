import class_info
animals = []

def add_animals():
  new_animal = class_info.Animal("Daisy", "Chimp", 12, "D9")
  animals.append(new_animal)
  new_animal1 = class_info.Animal("King", "Lion", 9, "L2")
  animals.append(new_animal1)
  new_animal2 = class_info.Animal("Queen", "Tiger", 18, "L3")
  animals.append(new_animal2)

add_animals()

for i in range(1000):
  animal_name = input("New Animal Name:")
  animal_kind = input("New Animal Kind:")
  animal_age = input("New Animal Age:")
  animal_location = input("New Animal Location:")
  a_new_animal = class_info.Animal(animal_name, animal_kind, animal_age, animal_location)
  animals.append(a_new_animal)
  for counter in range(len(animals)):
    animals[counter].print_with_location()
