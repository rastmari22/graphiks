import csv
import numpy as np
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
filename1 = 'GAZP.csv'
filename2 = 'SBER_.csv'
asset1_prices = []
asset2_prices = []

with open("GAZP_221230_231230.csv", 'r') as file:
    data = csv.DictReader(file, delimiter=';')
    for row in data:
        asset1_prices.append(int(row["<VOL>"]) // 1000000)

with open(filename2, 'r') as file:
    data = csv.DictReader(file, delimiter=';')
    for row in data:
        asset2_prices.append(int(row["<VOL>"]) // 1000000)


plt.scatter(asset1_prices, asset2_prices,)
plt.xlabel('Цены актива 1')
plt.ylabel('Цены актива 2')
plt.title('Диаграмма рассеяния цен на различные финансовые активы')

import numpy as np
from sklearn.linear_model import LinearRegression
slr = LinearRegression()
slr.fit(asset1_prices, asset2_prices)
y_pred = slr.predict(asset1_prices)
print('Slope: {:.2f}'.format(slr.coef_[0]))
print('Intercept: {:.2f}'.format(slr.intercept_))

as1=np.array(asset1_prices)


coefficient = np.polyfit(asset1_prices, asset2_prices, 1)
polynomial = np.poly1d(coefficient)
plt.plot(asset1_prices, np.poly1d(coefficient), color='red')


correlation_coefficient = np.corrcoef(asset1_prices, asset2_prices)[0, 1]
print('Коэффициент корреляции:', correlation_coefficient)

plt.show()