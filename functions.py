import csv
from random import randint


def load_data():
	with open("Anagrafica_conti.csv", "r") as file:
		csv_list = list(csv.reader(file))

	data = []

	for i in range(1, len(csv_list)):

		data.append({
			"id" : int(csv_list[i][0]),
			"nome" : csv_list[i][1],
			"cognome" : csv_list[i][2],
			"numero_carta" : int(csv_list[i][3]),
			"pin" : int(csv_list[i][4])
			})

	with open("Saldo_conti.csv", "r") as file:
		csv_list = list(csv.reader(file))

	for i in range(1, len(csv_list)):
		if data[i-1]["id"] == int(csv_list[i][0]):
			data[i-1]["saldo"] = int(csv_list[i][1])

	return data


def load_transactions():
	with open("SaldoMovimento_conti.csv", "r") as file:
		csv_list = list(csv.reader(file))

	transactions = []

	for i in range(1, len(csv_list)):

		transactions.append({
			"id" : int(csv_list[i][0]),
			"movimento" : int(csv_list[i][1])
			})

	return transactions


def print_data(data):
	for i in data:
		print("|"+ str(i["id"])+" "*(5-len(str(i["id"])))+"|", end = "")
		print(i["nome"]+" "*(15-len(i["nome"]))+"|", end = "")
		print(i["cognome"]+" "*(15-len(i["cognome"]))+"|", end = "")
		print(" "*(20-len(str(i["saldo"])))+str(i["saldo"])+"|")


def print_transactions(transactions):
	for i in transactions:
		print("|"+ str(i["id"])+" "*(5-len(str(i["id"])))+"|", end = "")
		print(" "*(15-len(str(i["movimento"])))+str(i["movimento"])+"|")


def save_data(data):
	with open("Anagrafica_conti.csv", "w") as file:
		file.write("id,nome,cognome,numero_carta,pin\n")

		for i in range(len(data)):
			file.write(str(data[i]["id"])+","+data[i]["nome"]+","+data[i]["cognome"]+","+str(data[i]["numero_carta"])+","+str(data[i]["pin"])+"\n")

	with open("Saldo_conti.csv", "w") as file:
		file.write("id,saldo\n")

		for i in range(len(data)):
			file.write(str(data[i]["id"])+","+str(data[i]["saldo"])+"\n")


def add_user(data):
	_id_ = int(data[len(data)-1]["id"]) + 1 
	nome = input("Nome > ")
	cognome = input("Cognome > ")
	saldo = int(input("Saldo > "))

	numero_carta = randint(10000, 99999)
	carte = [i["numero_carta"] for i in data]
	while numero_carta in carte: numero_carta = randint(10000, 99999)

	pin = randint(100, 999)

	add_transactions(_id_, saldo)

	print(numero_carta, pin)

	data.append({
		"id" : _id_,
		"nome" : nome,
		"cognome" : cognome,
		"numero_carta" : numero_carta,
		"pin": pin,
		"saldo" : saldo
		})

	return data


def login(data):
	numero_carta = int(input("Numero carta di credito > "))
	pin = int(input("Pin carta di credito > "))

	for i in data:
		if i["numero_carta"] == numero_carta and i["pin"] == pin:
			print("Ciao "+i["nome"]+" "+i["cognome"]+", il saldo corrente è di "+str(i["saldo"])+"€") 
			return data.index(i)
	else: 
		print("Identificazione non avvenuta.")
		return -1


def add_transactions(_id_, cash):
	with open("SaldoMovimento_conti.csv", "a") as file:
		file.write(str(_id_)+","+str(cash)+"\n")


def add_cash(data, index):
	cash = int(input("Inserisci il denaro che vuoi depositare > "))
	data[index]["saldo"] += cash

	print("Il saldo corrente è di "+str(data[index]["saldo"])+"€")

	add_transactions(data[index]["id"], cash)

	save_data(data)


def request_cash(data, index):
	while True:
		cash = int(input("Inserisci il denaro che vuoi ritirare > "))

		if data[index]["saldo"] >= cash:
			data[index]["saldo"] -= cash

			print("Il saldo corrente è di "+str(data[index]["saldo"])+"€")

			break
		else:
			print("Stai cercando di ritirare piu' denaro del tuo denaro corrente.")

	add_transactions(data[index]["id"], -cash)

	save_data(data)


def get_balance(data):
	_id_ = int(input("Inserisci l'id > "))

	for i in data:
		if i["id"] == _id_: 
			print_data([i])
			break
	else:
		print("Non esiste corrispondenza tra l'id di input e il database.")


def get_transactions(data):
	_id_ = int(input("Inserisci l'id > "))

	transactions = load_transactions()
	t = []

	for i in transactions:
		if i["id"] == _id_:
			t.append(i)
	
	if len(t) != 0:
		print_transactions(t)
	else:
		print("Non esiste corrispondenza tra l'id di input e il database.")
