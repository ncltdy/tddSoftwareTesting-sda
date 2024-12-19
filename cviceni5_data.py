class Warehouse:
    def __init__(self, capacity: float):
        if capacity <= 0:
            raise ValueError
        self.capacity = capacity
        self.free_space = capacity
        self.products = []


    def add(self, product):
        if self.free_space < product.volume:
            return -1
        self.free_space -= product.volume
        self.products.append(product)
        return round(self.free_space,2)

    def print_inventory(self):
        for product in self.products:
            print(product)


class Product:
    def __init__(self, name: str, volume: float):
        if volume <= 0:
            raise ValueError
        self.name = name
        self.volume = volume

    def __repr__(self):
        return f"Product(name = {self.name}, Volume = {self.volume})"

    def __str__(self):
        return f"{self.name} ma objem {self.volume}"

if __name__ == "__main__":
    sklad_Praha = Warehouse(1000.45547)

    auto1 = Product("Fordka", 3.332)

    print(sklad_Praha.add(auto1))
    print(sklad_Praha.add(auto1))

