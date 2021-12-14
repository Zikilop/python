from sys import argv

print(f"Выработка = {argv[1]}\nСтавка = {argv[2]}\nПремия = {argv[3]}\nЗарплата = {int(argv[1]) * int(argv[2]) + int(argv[3])}")

