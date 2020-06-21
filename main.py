class Animal:
  hungry = True
  name = ''
  color = ''
  weight = 0
  can_eat = 0
  animal_name = ''
  sound = ''

  def __init__(self, name, color, weight):
    self.color = color
    self.name = name
    self.weight = weight

  def feed(self):
    self.hungry = False
    self.weight += self.can_eat
    return 'Not hungry anymore'

  def make_sound(self):
    return self.sound





class Bird(Animal):
  lays_egg = True
  eggs_left = 1

  def collect_eggs(self):
    eggs_left = 0



class Goose(Bird):
  sound = "Some_goose_sound"
  can_eat = 0.4 #kg/day
  animal_name = 'Гусь'


class Hen(Bird):
  sound = "cockadoodledoo"
  can_eat = 0.1
  animal_name = 'Курица'


class Duck(Bird):
  sound = "quack!"
  can_eat = 0.2
  animal_name = 'Утка'



class Milking(Animal):
  got_milk = True
  milk_capacity = 0 #litres/day

  def milk(self):
    if self.milk_capacity > 0:
      self.got_milk = True
      self.milk_capacity /= 2



class Cow(Milking):
  sound = 'moo'
  milk_capacity = 15
  animal_name = 'Корова'
  can_eat = 8



class Goat(Milking):
  sound = 'ugly_goat_sound'
  milk_capacity = 6
  animal_name = 'Коза'
  can_eat = 4


class Sheep(Animal):
  sound = 'Baa'
  animal_name = 'Овца'
  is_sheared = False
  wool_weight = 5
  can_eat = 2

  def shear(self):
    self.wool_weight = 0
    self.is_sheared = True


def get_heaviest(*animals):
  count = 0
  who_wins = ''
  for species in animals:
      if count < species.weight:
        count = species.weight
        who_wins = species.animal_name + ' "' + species.name + '"'
  print(f'Самая тяжёлая - {who_wins}')


def sum_weight(*animals):
  count = 0
  for species in animals:
    count += species.weight
  print(f'Общий вес - {count}')

  


  
white_goose = Goose('Белый', 'white', 2.5)
grey_goose = Goose('Серый', 'grey', 3.3)
goat1 = Goat('Рога', 'black', 80)
goat2 = Goat('Копыта', 'white', 60)
goat1.milk()
goat2.milk()
cow1 = Cow('Манька', 'red', 750)
cow1.milk()
sheep1 = Sheep('Барашек', 'grey', 40)
sheep2 = Sheep('Кудрявый', 'white', 55)
hen1 = Hen('Ко-ко', 'orange', 0.7)
hen2 = Hen('Кукареку', 'brown', 0.65)
duck1 = Duck('Кряква', 'black', 1.5)

if not sheep1.is_sheared:
  sheep1.shear()
  print (f'{sheep1.name} пострижен')


get_heaviest(goat1, grey_goose, cow1)
sum_weight(white_goose, grey_goose, goat1, goat2, cow1, sheep1, sheep2, hen1, hen2, duck1)
print(duck1.make_sound())



