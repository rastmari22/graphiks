import csv
from datetime import datetime
import matplotlib.pyplot as plt

dt = []
vol = []
min_prices = []
max_prices = []
fn = "SBER2.csv"

with open(fn) as file:
    dr = csv.DictReader(file, delimiter=';')
    for r in dr:
        vol.append(int(r["<VOL>"]) // 1000000)
        dt.append(datetime.strptime(r["<DATE>"], '%y%m%d').strftime('%b %d'))
        min_prices.append(float(r["<LOW>"]))
        max_prices.append(float(r["<HIGH>"]))

plt.rcParams["font.family"] = "Times New Roman"
fig, axs = plt.subplots(2, figsize=(12, 6))


axs[0].set_title("Изменение цены на акции Сбербанка с 1.02.23 по 28.02.23")
axs[0].fill_between(dt, min_prices, max_prices, color='lightblue', label='Price Range')
axs[0].tick_params(axis='x', rotation=45)
axs[0].set_xlabel("Дата")
axs[0].set_ylabel("Цена, руб.")
axs[0].grid()


axs[1].set_title("Суммарный объем сделок")
axs[1].bar(dt, vol, color='lightgreen', edgecolor='black')
axs[1].tick_params(axis='x', rotation=45)
axs[1].set_xlabel("Дата")
axs[1].set_ylabel("Сумма, млн руб.")

plt.tight_layout()

plt.show()
