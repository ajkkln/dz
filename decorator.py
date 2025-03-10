class Coffee:
    def cost(self):
        return 5

class MilkDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost() + 2

# Пример использования
simple_coffee = Coffee()
print(f"Cost of simple coffee: {simple_coffee.cost()}")  # Вывод: 5

milk_coffee = MilkDecorator(simple_coffee)
print(f"Cost of coffee with milk: {milk_coffee.cost()}")  # Вывод: 7
