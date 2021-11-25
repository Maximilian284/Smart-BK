from functions import *

print("bank")

while True:
  data = load_data()
  command = input("-> ")

  if command == "exit": quit()
  if command == "print": print_data(data)
  if command == "save": save_data(data)
  if command == "add": add_user(data)
  if command == "get balance": get_balance(data)
  if command == "get transactions": get_transactions(data)
