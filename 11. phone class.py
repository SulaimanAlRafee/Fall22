class Phone:
  def __init__(self, manufacturer, model, storage, price, color):
    self.manufacturer = manufacturer
    self.model = model
    self.storage = storage
    self.quantity = 0
    self.price = price
    self.color = color

  def print(self):
    print("Phone Info")
    print("---------------")
    print("Made by:", self.manufacturer)
    print("Model:", self.model)
    print("Storage:", self.storage)
    print("Quantity available:", self.quantity)
    print("Price:", self.price)
    print("Color:", self.color)
