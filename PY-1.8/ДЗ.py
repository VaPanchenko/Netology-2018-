class Animals:
    def __init__(self, name, size, paws, hoofs, wings):
        self.name = name
        self.size = size
        self.paws = paws
        self.hoofs = hoofs
        self.wings = wings


    def __str__(self):
        return str ({
            'name': self.name,
            'size': self.size,
            'paws': self.paws,
            'hoofs': self.hoofs,
            'wings': self.wings,
        })

class Birds(Animals):
    name_bird = ['Утки', 'Куры', 'Гуси']

    def __init__(self, name_bird):
        self.name_bird = name_bird
        Animals.__init__ ( self, name_bird, 'Small', 2, 'None', 'Yes' )


class Animal(Animals):
    name_animal = ['Коровы', 'Козы', 'Овцы', 'Свиньи']

    def __init__(self, name_animal):
        self.name_animal = name_animal
        Animals.__init__ ( self, name_animal, 'Big', 4, 'Yes', 'None' )


ducks = Birds('Утки')
chickens = Birds('Куры')
geese = Birds('Гуси')
Cows = Animal('Коровы')
Goats = Animal('Козы')
Sheep = Animal('Овцы')
Pigs = Animal('Свиньи')

print ( '\n Класс Пернатые:',
        '\n Утки: {}'.format(ducks),
        '\n Куры: {}'.format(chickens),
        '\n Гуси: {}'.format(geese))

print ( '\n Класс Животные:',
        '\n Коровы: {}'.format(Cows),
        '\n Козы: {}'.format (Goats),
        '\n Овцы: {}'.format (Sheep),
        '\n Свиньи: {}'.format(Pigs))

