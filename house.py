class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(f'Вы переехали на {new_floor} этаж, в доме {self.name}')
        else:
            print('Такого этажа не существует')

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name}, Количество этажей: {self.number_of_floors}'
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)
    def __radd__(self, value):
        return House(self.name, self.number_of_floors + value)
    def __iadd__(self, value):
        self.number_of_floors += value
        return self






h1 = House('ЖК Весенний', 18)
h2 = House('ЖК СНТ-АГРО', 2)
h1.go_to(8)
h2.go_to(5)
print(h1)
print(h2)
print(len(h1))
print(len(h2))
print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1 != h2)

h1 = h1 + 12
print(h1)

h1 += 17
print(h1)

h2 = 20 + h2
print(h2)







