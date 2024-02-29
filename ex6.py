from Cube import Cube
import pygal as pg
from pygal.style import LightenStyle, LightColorizedStyle,RotateStyle
def probability(statistic):
    cul_stat = dict()
    N = sum(statistic.values())
    for k, v in statistic.items():
        cul_stat[k] = (v / N).__round__(2)
    return cul_stat
def after_throwing_cubs(c1, c2, statistic):
    sum_score = c1.face + c2.face
    statistic[sum_score] += 1
    return statistic
def culc_theory(c1,c2):
    N=c1.sides*c2.sides
    min_sides=min(c1.sides,c2.sides)
    max_sides=max(c1.sides,c2.sides)
    prob_dict=dict.fromkeys([i for i in range(2, (cub1.sides + cub2.sides) + 1)],0)
    for val1 in range(1,min_sides+1):
        for val2 in range(1,max_sides+1):
            prob_dict[val1+val2]+=1
    for k,v in prob_dict.items():
        prob_dict[k]=(v / N).__round__(2)
    return prob_dict
def print_result(sides_count, probab,theor,n):
    sum_score = list(map(lambda x: '{:>4}'.format(x), sides_count.keys()))
    throw_count = list(map(lambda x: '{:>4}'.format(x), sides_count.values()))
    pr = list(map(lambda x: '{:>4}'.format(x), probab.values()))
    th = list(map(lambda x: '{:>4}'.format(x), theor.values()))
    print("Количество бросков = ", n)
    print("Сумма очков:         ", '   '.join(map(str, sum_score)))
    print("Число выпадений:     ", '   '.join(map(str, throw_count)))
    print("Вероятность:         ", '   '.join(map(str, pr)))
    print("Теория:              ", '   '.join(map(str, th)))
def get_graphic():
    dark_rotate_style = RotateStyle('#9e6ffe')
    hist = pg.Bar(style=dark_rotate_style)

    hist.title = f"Результаты моделирования двух кубиков по {cub1.sides} и {cub2.sides} граней {n} раз"
    hist.x_labels = sides_count.keys()
    hist.x_title = "Сумма очков"
    hist.y_title = "Число выпадений"

    hist.add('Сумма ', sides_count.values())
    hist.render_to_file("Результат.svg")

cub1 = Cube()
cub2 = Cube()

sides_count = dict.fromkeys([i for i in range(2, (cub1.sides+cub2.sides) + 1)], 0)

n = int(input("Введите число бросков: "))
for i in range(n):
    cub1.throw()
    cub2.throw()
    sides_count = after_throwing_cubs(cub1, cub2, sides_count)

probab=probability(sides_count)
theor=culc_theory(cub1,cub2)
print_result(sides_count,probab,theor,n)

get_graphic()

