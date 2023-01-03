per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("money = "))
deposit= []
deposit = [number*money*0.01 for number in per_cent.values()]
print("deposit = ",deposit)
print("Максимальная сумма, которую вы можете заработать —",max(deposit))
