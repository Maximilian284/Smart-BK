import csv
from random import randint

def load_data():
	with open("Anagrafica_conti.csv", "r") as file:
		csv_list = list(csv.reader(file))

	data = []

	for i in range(1, len(csv_list)):

		data.append({
			"id" : csv_list[i][0],
			"nome" : csv_list[i][1],
			"cognome" : csv_list[i][2],
			"numero_carta" : csv_list[i][3],
			"pin" : csv_list[i][4]
			})

	with open("Saldo_conti.csv", "r") as file:
		csv_list = list(csv.reader(file))

	for i in range(1, len(csv_list)):
		if data[i-1]["id"] == csv_list[i][0]:
			data[i-1]["saldo"] = int(csv_list[i][1])

	return data

# print example:
# |1    |Mario          |Rossi          |       1000|
def print_data(data):
	for i in data:
		print("|"+ str(i["id"])+" "*(5-len(str(i["id"])))+"|", end = "")
		print(i["nome"]+" "*(15-len(i["nome"]))+"|", end = "")
		print(i["cognome"]+" "*(15-len(i["cognome"]))+"|", end = "")
		print(" "*(20-len(str(i["saldo"])))+str(i["saldo"])+"|")

def save_data(data):
	with open("Anagrafica_conti.csv", "w") as file:
		file.write("id,nome,cognome\n")

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

def __identification__(data, numero_carta, pin):
	check_list = [[int(i["numero_carta"]), int(i["pin"]), data.index(i)] for i in data]

	for i in check_list:
		if i[0] == numero_carta and i[1] == pin: 
			return i[2]
	else: 
		return False

def add_transition(_id_, cash):
	with open("SaldoMovimento_conti.csv", "a") as file:
		file.write(str(_id_)+","+str(cash)+"\n")


def add_cash(data):
	numero_carta = int(input("Numero carta di credito > "))
	pin = int(input("Pin carta di credito > "))

	cash = 0
	index = __identification__(data, numero_carta, pin)
	if index != False: 
		cash = int(input("Inserisci il denaro > "))
		data[index]["saldo"] += cash

	add_transition(data[index]["id"], cash)

	save_data(data)

			

def request_cash():
	pass