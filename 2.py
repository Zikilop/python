def print_info(name, surname, year, city, email, number):
    print(f"Имя -- {name}, Фамилия -- {surname} Год рождения -- {year}, Город проживания -- {city}, Email -- {email}, Телефон -- {number}")
    return

print_info(name=input("Введите имя: "), surname=input("Введите фамилию: "), year=input("Введите год рождения: "), city=input("Введите город проживания: "), email=input("Введите email: "), number=input("Введите телефон: "))
