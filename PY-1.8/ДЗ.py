class Animals:

    def __init__(self, name, animals_type, size, paws, hoofs, wings):
        self.name = name
        self.size = size
        self.paws = paws
        self.hoofs = hoofs
        self.wings = wings
        self.animals_type = animals_type

    def __str__(self):
        return str({
            'name': self.animals_type,
            'size': self.size,
            'paws': self.paws,
            'hoofs': self.hoofs,
            'wings': self.wings,
        })


class Birds(Animals):

    def __init__(self, name_bird, animals_type):
        self.name_bird = name_bird
        self.animals_type = animals_type

        super().__init__(name_bird, animals_type, 'Small', 2, 'None', 'Yes')


class Animal(Animals):

    def __init__(self, name_animal, animals_type):
        self.name_animal = name_animal
        self.animals_type = animals_type

        super().__init__(name_animal, animals_type, 'Big', 4, 'Yes', 'None')


class Chicken(Birds):
    bird_type = 'Куры'

    def __init__(self, name):
        super(Chicken, self).__init__(name, Chicken.bird_type)


class Ducks(Birds):
    bird_type = 'Утки'

    def __init__(self, name):
        super(Ducks, self).__init__(name, Ducks.bird_type)


class Geese(Birds):
    bird_type = 'Гуси'

    def __init__(self, name):
        super(Geese, self).__init__(name, Geese.bird_type)


class Cows(Animal):
    animal_type = 'Коровы'

    def __init__(self, name):
        super(Cows, self).__init__(name, Cows.animal_type)


class Goats(Animal):
    animal_type = 'Козы'

    def __init__(self, name):
        super(Goats, self).__init__(name, Goats.animal_type)


class Sheep(Animal):
    animal_type = 'Овцы'

    def __init__(self, name):
        super(Sheep, self).__init__(name, Sheep.animal_type)


class Pigs(Animal):
    animal_type = 'Свиньи'

    def __init__(self, name):
        super(Pigs, self).__init__(name, Pigs.animal_type)


ducks = Ducks('Утки')
chickens = Chicken('птеродактель')
geese = Geese('Гуси')
cows = Cows('Коровы')
goats = Goats('Козы')
sheep = Sheep('Овцы')
pigs = Pigs('Свиньи')


print('\n Класс Пернатые:',
      '\n', ducks.name, '{}'.format(ducks),
      '\n', chickens.name, '{}'.format(chickens),
      '\n', geese.name, '{}'.format(geese))

print('\n Класс Животные:',
      '\n', cows.name, '{}'.format(cows),
      '\n', goats.name, '{}'.format(goats),
      '\n', sheep.name, '{}'.format(sheep),
      '\n', pigs.name, '{}'.format(pigs))
