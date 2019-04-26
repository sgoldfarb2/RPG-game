import random



class Character:
  def __init__(self):
    pass
  def alive(self, enemy):
    while(self.health > 0 and enemy.health > 0 or enemy.type == 'Zombie'):
      print("You have {} health and {} power.".format(self.health, self.power))
      print("Your enemy has {} health and {} power.".format(enemy.health, enemy.power))
      print("""
      -----------------------------
      Welcome to the Python's lair
      -----------------------------
      What do you want to do?
      1. Fight enemy
      2. Do nothing
      3. Flee and leave the game (CHICKEN!)
      4. Go to the store
      """)

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
        item_to_buy = int(input("""
        ---------------------
        Welcome to the store!
        ---------------------
        Which item would you like to buy?
        1. Supertonic - restores you to full health
        2. Armor - protects you 2 health points
        3. Evade - helps you avoid an attack
        4. Leave store
        """))
        if item_to_buy == 1:
            self.buy_supertonic()
        elif item_to_buy == 2:
           self.buy_armor()
        elif item_to_buy == 3:
            self.buy_evade()
        elif item_to_buy == 4:
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
        if self.armor_points > 0:
          self.health += self.armor_points
          enemy.attack(self)
        # self.health -= enemy.power
          print("Your enemy does {} damage to you.".format(enemy.power))
        else:
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
        # continue = input('Continue? Y/N: ')
        # if continue == 'Y':

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

  def buy_supertonic(self):
    if self.coins >= 2:
      self.health = 10
      self.coins -= 2
      print(f'You still have {self.coins} coin(s)')
    else:
      print(f'Sorry, you don\'t have enough coins, you only have {self.coins} left!')

  def buy_armor(self):
    if self.coins >= 2:
      self.armor_points = 2
      print(f'You have {self.armor_points} armor points')
      self.coins -= 2
      print(f'You still have {self.coins} coin(s)')
    else:
      print(f'Sorry, you don\'t have enough coins, you only have {self.coins} left!')

  def buy_evade(self):
    if self.coins >= 2:
      self.evade_points += 2
      print(f'You have {self.evade_points} evade points!')
      self.coins -= 2
      print(f'You still have {self.coins} coin(s)')
    else:
      print(f'Sorry, you don\'t have enough coins, you only have {self.coins} left!')






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




# class Store():
#   def __init__(self):
#     pass
#Hmm should my store have it's own class? Since only the hero uses it, does it NEED one?!




sabrina = Hero()
michael = Goblin()
steven = Medic()
barbara = Zombie()
winnie = Shadow()
sabrina.alive(michael)
# sabrina.alive(steven)


#edited my store so things can only be purchased if the user has enough points to buy them!
#supertonic and armor are working, still need to make evade points work. able to buy evade points, but not sure how to add the additional percentage to make them work better each time. Still thinking!

