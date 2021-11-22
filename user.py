from functions import *

data = load_data()

print("user")

while True:
  command = input("-> ")

  if command == "exit": quit()
  if command == "reload": data = load_data()
  if command == "add": add_cash(data)
  if command == "request": request_cash()