
cars = {
    "Toyota Corolla": {"price": 20000, "engine_power": 132},
    "Honda Civic": {"price": 21000, "engine_power": 158},
    "Ford Focus": {"price": 22000, "engine_power": 160},
    "BMW 3 Series": {"price": 35000, "engine_power": 255},
    "Audi A4": {"price": 38000, "engine_power": 220},
    "Mercedes-Benz C-Class": {"price": 45000, "engine_power": 255},
    "Chevrolet Malibu": {"price": 24000, "engine_power": 160},
    "Hyundai Elantra": {"price": 19000, "engine_power": 147},
    "Kia Optima": {"price": 23000, "engine_power": 185},
    "Nissan Altima": {"price": 25000, "engine_power": 188}
}

# Функція для виведення всіх значень словника
def display_all_cars(cars_dict):
    print("\nВсі автомобілі:")
    for car, details in cars_dict.items():
        print(f"{car}: Вартість = ${details['price']}, Потужність двигуна = {details['engine_power']} к.с.")

# Функція для додавання нового запису до словника 
def add_car(cars_dict):
    car_name = input("\nВведіть назву автомобіля, який хочете додати: ")
    
    if car_name in cars_dict:
        print(f"\nАвтомобіль {car_name} вже існує в словнику.")
    else:
        try:
            price = int(input(f"Введіть вартість автомобіля {car_name}: "))
            engine_power = int(input(f"Введіть потужність двигуна для {car_name} (к.с.): "))
            cars_dict[car_name] = {"price": price, "engine_power": engine_power}
            print(f"\nАвтомобіль {car_name} додано до словника.")
        except ValueError:
            print("\nБудь ласка, вводьте лише числові значення для вартості та потужності.")

# Функція для видалення запису зі словника 
def remove_car(cars_dict):
    car_name = input("Введіть назву автомобіля, який хочете видалити: ")
    
    if car_name in cars_dict:
        del cars_dict[car_name]
        print(f"\nАвтомобіль {car_name} видалено зі словника.")
    else:
        print(f"\nАвтомобіль {car_name} не знайдено в словнику.")

# Функція для перегляду вмісту словника за відсортованими ключами
def display_sorted_cars(cars_dict):
    print("\nАвтомобілі за відсортованими назвами:")
    for car in sorted(cars_dict.keys()):
        details = cars_dict[car]
        print(f"{car}: Вартість = ${details['price']}, Потужність двигуна = {details['engine_power']} к.с.")

# Функція для обчислення загальної вартості автомобілів з потужністю більше 100 к.с.
def total_price_of_high_power_cars(cars_dict):
    total_price = 0
    for car, details in cars_dict.items():
        if details["engine_power"] > 100:
            total_price += details["price"]
    print("\nЗагальна вартість автомобілів з потужністю більше 100 к.с. = $", total_price)


display_all_cars(cars)
add_car(cars)  
remove_car(cars)  
display_sorted_cars(cars)  
total_price_of_high_power_cars(cars) 
