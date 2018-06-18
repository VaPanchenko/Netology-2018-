class Animals:

    def __init__(self, name, size, paws, hoofs, wings):
        self.name = name
        self.size = size
        self.paws = paws
        self.hoofs = hoofs
        self.wings = wings

    def __str__(self):
        return str({
            'name': self.name,
            'size': self.size,
            'paws': self.paws,
            'hoofs': self.hoofs,
            'wings': self.wings,
        })


class Birds(Animals):

    def __init__(self, name_bird):
        self.name_bird = name_bird
        super().__init__(name_bird, 'Small', 2, 'None', 'Yes')


class Animal(Animals):

    def __init__(self, name_animal):
        self.name_animal = name_animal
        super().__init__(name_animal, 'Big', 4, 'Yes', 'None')


ducks = Birds('Утки')
chickens = Birds('Куры')
geese = Birds('Гуси')
cows = Animal('Коровы')
goats = Animal('Козы')
sheep = Animal('Овцы')
pigs = Animal('Свиньи')

print('\n Класс Пернатые:',
      '\n', ducks.name, '{}'.format(ducks),
      '\n', chickens.name, '{}'.format(chickens),
      '\n', geese.name, '{}'.format(geese))

print('\n Класс Животные:',
      '\n', cows.name, '{}'.format(cows),
      '\n', goats.name, '{}'.format(goats),
      '\n', sheep.name, '{}'.format(sheep),
      '\n', pigs.name, '{}'.format(pigs))
