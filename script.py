money = int(input("Сумма вклада: "))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
s = round((round((per_cent.get('ТКБ'))/100, 5))*money, 2)
k = round((round((per_cent.get('СКБ'))/100, 5))*money, 2)
l = round((round((per_cent.get('ВТБ'))/100, 5))*money, 2)
f = round((round((per_cent.get('СБЕР'))/100, 5))*money, 2)
deposit = [s, k, l, f]
print(deposit)
sort_deposit = sorted(deposit)
max_deposit = sort_deposit[-1]
print("Максимальная сумма которую вы можете заработать: ", max_deposit)