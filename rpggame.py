#!/usr/bin/env python


class Character:
  def __init__(self):
    pass
  def alive(self, enemy):
    while(self.health > 0):
      print("You have {} health and {} power.".format(self.health, self.power))
      print("The goblin has {} health and {} power.".format(enemy.health, enemy.power))
      print()
      print("What do you want to do?")
      print("1. fight goblin")
      print("2. do nothing")
      print("3. flee")
      print("> ", end=' ')
      raw_input = input()
      if raw_input == "1":
              # Hero attacks goblin
        enemy.health -= self.power
        print("You do {} damage to the goblin.".format(self.power))
        if enemy.health <= 0:
          print("The goblin is dead.")
      elif raw_input == "2":
        pass
      elif raw_input == "3":
        print("Goodbye.")
        break
      else:
              print("Invalid input {}".format(raw_input))

      if enemy.health > 0:
              # Goblin attacks hero
        self.health -= enemy.power
        print("The goblin does {} damage to you.".format(enemy.power))
        if self.health <= 0:
          print("You are dead.")

  def attack(self, enemy):
    enemy.health = enemy.health - self.power

  def print_status(self):
    print("You have {} health and {} power.".format(self.health, self.power))



class Hero(Character):
  def __init__(self):
    self.health = 10
    self.power = 5

  # def attack(self, enemy):
  #   enemy.health = enemy.health - self.power

  # def print_status(self):
  #   print("You have {} health and {} power.".format(self.health, self.power))



class Goblin(Character):
  def __init__(self):
    self.health = 6
    self.power = 2

  # def attack(self, enemy):
  #   enemy.health = enemy.health - self.power

  # def print_status(self):
  #   print("You have {} health and {} power.".format(self.health, self.power))

