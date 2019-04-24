#!/usr/bin/env python

# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee


# class Character:
#   def __init__(self, health, power):
#     self.health = health
#     self.power = power





# class Hero(Character):
#   def __init__(self, health, power):
#     self.health = health
#     self.power = power

#   def alive(self):
#     while self.alive():
#       print("You have {} health and {} power.".format(self.health, self.power))
#       print("The goblin has {} health and {} power.".format(enemy.health, enemy.power))
#       print()
#       print("What do you want to do?")
#       print("1. fight goblin")
#       print("2. do nothing")
#       print("3. flee")
#       print("> ", end=' ')
#       raw_input = input()
#       if raw_input == "1":
#             # Hero attacks goblin
#           goblin_health -= hero_power
#           print("You do {} damage to the goblin.".format(hero_power))
#             if goblin_health <= 0:
#                 print("The goblin is dead.")
#       elif raw_input == "2":
#             pass
#       elif raw_input == "3":
#             print("Goodbye.")
#             break
#       else:
#             print("Invalid input {}".format(raw_input))

#       if goblin_health > 0:
#             # Goblin attacks hero
#             hero_health -= goblin_power
#             print("The goblin does {} damage to you.".format(goblin_power))
#       if hero_health <= 0:
#                 print("You are dead.")

#   def attack(self, enemy):
#     enemy.health = enemy.health - self.power

#   def print_status(self):
#     print("You have {} health and {} power.".format(self.health, self.power))



# class Goblin(Character):
#   def __init__(self, health, power):
#     self.health = health
#     self.power = power


#   def alive(self):
#     while self.alive():
#       print("You have {} health and {} power.".format(self.health, self.power))
#       # print("The goblin has {} health and {} power.".format(enemy.health, enemy.power))
#       print()
#       print("What do you want to do?")
#       print("1. fight goblin")
#       print("2. do nothing")
#       print("3. flee")
#       print("> ", end=' ')
#       raw_input = input()
#         if raw_input == "1":
#             # Hero attacks goblin
#           goblin_health -= hero_power
#           print("You do {} damage to the goblin.".format(enemy.power))
#             if self.health <= 0:
#                 print("The goblin is dead.")
#         elif raw_input == "2":
#             pass
#         elif raw_input == "3":
#             print("Goodbye.")
#             break
#         else:
#             print("Invalid input {}".format(raw_input))

#         if goblin_health > 0:
#             # Goblin attacks hero
#             enemy.health -= self.power
#             print("The goblin does {} damage to you.".format(goblin_power))
#         if enemy.health <= 0:
#                 print("You are dead.")


#   def attack(self, enemy):
#     enemy.health = enemy.health - self.power

#   def print_status(self):
#     print("You have {} health and {} power.".format(self.health, self.power))


# sabrina = Hero(10, 5)
# michael = Goblin(12, 1)
# sabrina.alive()



# # def main():
# #     hero_health = 10
# #     hero_power = 5
# #     goblin_health = 6
# #     goblin_power = 2

# #     while goblin_health > 0 and hero_health > 0:
# #         print("You have {} health and {} power.".format(hero_health, hero_power))
# #         print("The goblin has {} health and {} power.".format(goblin_health, goblin_power))
# #         print()
# #         print("What do you want to do?")
# #         print("1. fight goblin")
# #         print("2. do nothing")
# #         print("3. flee")
# #         print("> ", end=' ')
# #         raw_input = input()
# #         if raw_input == "1":
# #             # Hero attacks goblin
# #             goblin_health -= hero_power
# #             print("You do {} damage to the goblin.".format(hero_power))
# #             if goblin_health <= 0:
# #                 print("The goblin is dead.")
# #         elif raw_input == "2":
# #             pass
# #         elif raw_input == "3":
# #             print("Goodbye.")
# #             break
# #         else:
# #             print("Invalid input {}".format(raw_input))

# #         if goblin_health > 0:
# #             # Goblin attacks hero
# #             hero_health -= goblin_power
# #             print("The goblin does {} damage to you.".format(goblin_power))
# #             if hero_health <= 0:
# #                 print("You are dead.")

# # main()

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



class Hero(Character):
  def __init__(self):
    self.health = 10
    self.power = 5

  def attack(self, enemy):
    enemy.health = enemy.health - self.power

  def print_status(self):
    print("You have {} health and {} power.".format(self.health, self.power))



class Goblin(Character):
  def __init__(self):
    self.health = 6
    self.power = 2

  def attack(self, enemy):
    enemy.health = enemy.health - self.power

  def print_status(self):
    print("You have {} health and {} power.".format(self.health, self.power))



