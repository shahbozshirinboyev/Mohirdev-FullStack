from person import Person

person0 = Person('umid', "mamatov", 23, 'mamatovu@gmail.com', 23, 10, 1997)
print(person0.get_info())
number = person0.get_life_path_number()
print(person0.get_info_by_number(number))