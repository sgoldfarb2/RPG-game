import random
class Character:
  def __init__(self):
    pass
  def alive(self, enemy):
    while(self.health > 0 and enemy.health > 0 or enemy.type == 'Zombie'):
      print("You have {} health and {} power.".format(self.health, self.power))
      print("Your enemy has {} health and {} power.".format(enemy.health, enemy.power))
      print()
      print("What do you want to do?")
      print("1. fight enemy")
      print("2. do nothing")
      print("3. flee")
      print("4. Go to the store")
      print("> ", end=' ')
      raw_input = input()
      if raw_input == "1":
              # Hero attacks goblin
        self.attack(enemy)
        # print("You do {} damage to the goblin.".format(self.power))
        # if enemy.health <= 0:
        #   print("The goblin is dead.")
      elif raw_input == "2":
        pass
      elif raw_input == "3":
        print("Goodbye.")
        break
      elif raw_input == "4":
        pass
      else:
              print("Invalid input {}".format(raw_input))

      # if enemy.health > 0:
      #         # Goblin attacks hero
      #   self.health -= enemy.power
      #   print("The goblin does {} damage to you.".format(enemy.power))
      #   if self.health <= 0:
      #     print("You are dead.")

  def attack(self, enemy):
    enemy.health = enemy.health - self.power

  def print_status(self):
    print("You have {} health and {} power.".format(self.health, self.power))



class Hero(Character):
  def __init__(self):
    self.health = 10
    self.power = 2
    self.coins = 0
    self.weapons = []
    self.armor_points = 0
    self.evade_points = 0

  def attack(self, enemy):
    probability = random.randint(1, 5)
    if probability < 5:
      enemy.health = enemy.health - self.power
      print("You do {} damage to your enemy.".format(self.power))
      if enemy.health <= 0:
        print("The enemy is dead.")
      if enemy.health > 0:
              # Goblin attacks hero
        enemy.attack(self)
        # self.health -= enemy.power
        print("Your enemy does {} damage to you.".format(enemy.power))
      if self.health <= 0:
          print("You are dead.")
    else:
      enemy.health = enemy.health - self.power * 2
      print("You do {} damage to your enemy.".format(self.power * 2))
      if enemy.health <= 0:
        print("Your enemy is dead.")
        self.collect_bounty(enemy)
      if enemy.health > 0:
              # Goblin attacks hero
        enemy.attack(self)
      if self.health <= 0:
          print("You are dead.")

  def collect_bounty(self, enemy):
    if enemy.type == 'Goblin':
      self.coins += 2
    elif enemy.type == 'Medic':
      self.coins += 1
    elif enemy.type == 'Shadow':
      self.coins += 5
    print(f'Congrats! You now have {self.coins} coins!')





class Goblin(Character):
  def __init__(self):
    self.health = 6
    self.power = 3
    self.type = 'Goblin'





class Medic(Character):
  def __init__(self):
    self.health = 12
    self.power = 2
    self.type = 'Medic'

  def attack(self, enemy):
    probability = random.randint(1, 5)
    print(f'Our probability number is: {probability}')
    if probability < 5:
      enemy.health = enemy.health - self.power
    else:
      self.health = self.health + 2
      enemy.health = enemy.health - self.power




class Shadow(Character):
  def __init__(self):
    self.health = 1
    self.power = 2
    self.type = 'Shadow'

  def attack(self, enemy):
    probability = random.randint(1, 11)
    print(f'Our probability number is: {probability}')
    if probability < 10:
      self.health = self.health
      enemy.health = enemy.health - self.health
    else:
      self.health = self.health - enemy.health
      enemy.health = enemy.health - self.health




class Zombie(Character):
  def __init__(self):
    self.health =10
    self.power = 2
    self.type = 'Zombie'




  def print_status(self):
    print("You have {} health and {} power.".format(self.health, self.power))




class Store():
  def __init__(self):
    pass

  def buy_supertonic(self, hero):
    hero.health = 10

  def buy_armor(self, hero):
    hero.armor_points = 2

  def buy_evade(self, hero):
    hero.evade_points += 2



sabrina = Hero()
michael = Goblin()
steven = Medic()
barbara = Zombie()
winnie = Shadow()
sabrina.alive(michael)

#stuck at the store, not sure how to go in to the store!