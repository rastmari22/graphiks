import matplotlib
from matplotlib.dates import AutoDateLocator, AutoDateFormatter
import matplotlib.pyplot as plt
from datetime import datetime
dates=[]
subscribers=[]
y2_val=[]
with open("data.txt", "r") as f:
    file=f.readlines()#.encode('utf-8').decode('utf-8-sig')
    for line in file:
        line=line.strip().split()
        dmY=datetime.strptime(line[1], '%d-%m-%Y')
        dates.append(dmY)
        subscribers.append(int(line[2]))


cumulative_total_subscribers = [sum(subscribers[:i+1]) for i in range(len(subscribers))]

print(cumulative_total_subscribers)
matplotlib.rcParams['font.family'] = 'Times New Roman'
fig, (axs1,axs2)=plt.subplots(2,1,figsize=(10,5), facecolor='lightskyblue',
                       layout='constrained')

axs1.plot(dates,subscribers,
            label='Ежемесячные подключения',
            c='b',
            marker='D',ms=3)

axs2.plot(dates,cumulative_total_subscribers,
            label='Нарастающий итог',
            c='r',
            marker='o',ms=3)

for ax in(axs1,axs2):
    ax.grid()
    ax.set_ylabel("Кол-во человек")
    ax.xaxis.set_major_formatter(AutoDateFormatter(AutoDateLocator()))

plt.show()

# i=i.decode('utf-8-sig')