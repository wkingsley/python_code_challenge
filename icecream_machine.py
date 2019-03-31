# 3. Ice Cream Machine
class IceCreamMachine:

  def __init__(self, ingredients, toppings):
    self.ingredients = ingredients
    self.toppings = toppings

  def scoops(self):
    if not self.ingredients or not self.toppings:
      return []
    else:
      mix = []
      for ingredient in self.ingredients:
        for topping in self.toppings:
          mix.append([ingredient, topping])
      return mix

# machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce","orange"])
print(machine.scoops())