per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада:'))
deposite_TKB = round((money * per_cent.get('ТКБ'))/100)
deposite_SKB = round((money * per_cent.get('СКБ'))/100)
deposite_VTB = round((money * per_cent.get('ВТБ'))/100)
deposite_SBER = round((money * per_cent.get('СБЕР'))/100)
deposite = [deposite_TKB, deposite_SKB, deposite_VTB,deposite_SBER]

print('Максимальная сумма, которую вы можете заработать —', max(deposite))
