class Animal:
  def __init__(self, name, age, type):
    self.name = name
    self.age = age
    self.type = type

  def print(self):
    print("------")
    print("Name: ",self.name)
    print("Age: ",self.age)
    print("Type: ",self.type)
    print("------")

animals = []
animals.append(Animal("Aria", 12, "Cat"))
animals.append(Animal("Smokey", 8, "Reptile"))
animals.append(Animal("Nono", 24, "Bird"))

def print_menu():
  print("------")
  print("Select from a list")
  print("1- Add animal")
  print("2- List all animals")
  print("3- List animal by type")
  print("------")

def print_all_animals():
  for animal in animals:
    animal.print()

def print_by_type():
  print("------") 
  the_type = input("Enter animal type:")
  for animal in animals:
    if animal.type == the_type:
      animal.print()
  print("------") 

def add_animal():
  print("------")
  name = input("Enter animal name:")
  age = int(input("Enter animal age:"))
  type = input("Enter animal type:")
  new_animal = Animal(name, age, type)
  animals.append(new_animal)
  
for i in range(1000):
  print_menu()
  result = int(input("Enter selection:"))
  if result == 1:
    add_animal()
  elif result == 2:
    print_all_animals()
  elif result == 3:
    print_by_type()
  else:
    print("Try again")
