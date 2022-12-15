import phone_class

phones = []

def add_phones():
  new_phone = phone_class.Phone("Apple", "14 Max Pro", 256, 340, "White")
  phones.append(new_phone)
  new_phone = phone_class.Phone("Apple", "14 Max Pro", 256, 345, "Black")
  phones.append(new_phone)
  new_phone = phone_class.Phone("Apple", "14 Pro", 512, 325, "Black")
  phones.append(new_phone)
  new_phone = phone_class.Phone("Apple", "14 Pro", 512, 326, "Blue")
  phones.append(new_phone)
  new_phone = phone_class.Phone("Samsung", "S22+", 256, 280, "Gold")
  phones.append(new_phone)
  new_phone = phone_class.Phone("Samsung", "S22", 256, 260, "Black")
  phones.append(new_phone)
  new_phone = phone_class.Phone("Samsung", "S22U", 256, 325, "Red")
  phones.append(new_phone)

def show_menu():
  print("-------")
  print("Select an item from the menu:")
  print("1-Show all phones")
  print("2-Add new phone")
  print("3-Search for phones by price")
  print("4-Search for phones by name")
  print("5-Show total price for all phones")
  print("6-Add new inventory")
  print("0-Exit")
  print("-------")
def search_for_phone_by_price():
  lower_price = int(input("Please enter lower price:"))
  higher_price = int(input("Please enter maximum price:"))
  for i in range(len(phones)):
    if phones[i].price >= lower_price and phones[i].price <= higher_price:
      phones[i].print()

def search_for_phone_by_name():
  name = input("Please enter phone make:")
  for i in range(len(phones)):
    if phones[i].manufacturer.find(name) > -1:
      phones[i].print()  
def add_phone():
    print("Please enter new phone information:")
    print("-------")
    made_by = input("Please enter company name:")
    model = input("Please enter model name:")
    storage = int(input("Please enter storage:"))
    price = int(input("Please enter price:"))
    color = input("Please enter color:")
    new_phone = phone_class.Phone(made_by, model, storage, price, color)
    phones.append(new_phone)

def print_all_phones():
  for i in range(len(phones)):
    phones[i].print()   

def find_total_price():
  total = 0
  for i in range(len(phones)):
    total = total + phones[i].price
  print("-------")
  print("Total price = ", total)
  print("-------")
def add_to_inventory():
  for i in range(len(phones)):
    print(i," - ", phones[i].manufacturer, " - ", phones[i].model)
  which_phone = int(input("Which phone to add to?"))
  how_many = int(input("How many did you add?"))
  phones[which_phone].quantity = phones[which_phone].quantity + how_many
    

add_phones()
for i in range(10000):
  show_menu()
  result = int(input("What is your selection: "))
  if result == 0:
    break
  elif result == 1:
    print_all_phones()
  elif result == 2:
    add_phone()
  elif result == 3:
    search_for_phone_by_price()
  elif result == 4:
    search_for_phone_by_name()
  elif result == 5:
    find_total_price() 
  elif result == 6:
    add_to_inventory()    
