from functions import *

print("user")

user = -1

while True:
  data = load_data()
  command = input("-> ")

  if command == "exit": quit()
  if command == "login": user = login(data)
  if command == "logout": user = -1

  if user != -1:
    if command == "add": add_cash(data, user)
    if command == "request": request_cash(data, user)