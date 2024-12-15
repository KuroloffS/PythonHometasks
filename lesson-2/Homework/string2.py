#lesson2 #string #problem2
car_names = ['Malibu', 'Lasetti']
txt = 'LMaasleitbtui'
def extract_car_names(text, car_names):
    found_cars = []
    for car in car_names:
        if all(char in text for char in car):
            found_cars.append(car)
    return found_cars
result = extract_car_names(txt, car_names)
print("Found car names:", result)