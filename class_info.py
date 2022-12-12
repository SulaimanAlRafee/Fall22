class Animal:
  def __init__ (self, name, kind, age, location):
    self.name = name
    self.kind = kind
    self.age = age
    self.location = location

  def print (self):
    print("Animal info")
    print("-----------")
    print("Name: ", self.name)
    print("Age: ", self.age)
    print("Kind: ", self.kind)
    print("-----------\n")

  def print_with_location (self):
    print("Animal info")
    print("-----------")
    print("Name: ", self.name)
    print("Age: ", self.age)
    print("Kind: ", self.kind)
    print("Location: ", self.location)
    print("-----------\n")
