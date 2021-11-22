from functions import *

data = load_data()

print("bank")

while True:
  command = input("-> ")

  if command == "exit": quit()
  if command == "reload": data = load_data()
  if command == "print": print_data(data)
  if command == "save": save_data(data)
  if command == "add": add_user(data)
  if command == "update": pass

