print("Количество билетов:")
tickets = int(input())
is_free = 0
young = 0
older = 0
for i in range(1,tickets+1):
    print(f"Возраст участника по {i}-му билету:")
    age_visitor = int(input())
    if 18 > age_visitor:
        is_free += 1
    if 18 <= age_visitor < 25:
        young += 1
    if 25 <= age_visitor:
        older += 1
if tickets > 3:
    print(f"Общая стоимость: {int((young * 990 + older * 1390)*0.9)}руб.")
else:
    print(f"Общая стоимость: {young * 990 + older * 1390}руб.")
