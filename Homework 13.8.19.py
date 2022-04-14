print("Количество билетов:")
tickets = int(input())
Is_free = 0
for i in range(1,tickets+1):
    print(f"Возраст участника по {i}-му билету:")
    age_visitor = int(input())
    if age_visitor < 18:
        Is_free += 1
    if 18 <= age_visitor <=